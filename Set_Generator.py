import svgwrite

def generate_set(feature_number=4,feature_variety=3):
#    функция генерирует массив кодов, определяющих изображение на картах, т.к. для целей игры
#    вариативность каждого признака должна быть одинаковой - процесс похож на перечисление всех чисел
#    системы счисления с основанием feature_variety (по умолчанию - троичная система счисления)
#    feature_number число признаков(разрядность, возможные варианты - 4(по умолчанию) и 3(только зеленый цвет))
#    feature_variety вариативность признаков(основание системы счисления, минимум 2, 
#   максимум - максимальное число методов в классе Card(пока 3), теоритический максимум алгоритма - 9)
    code_of_set_list=[0 for i in range(feature_variety**feature_number)] # массив кодов(число возможных вариаций чисел в заданной разрядности)
    append_list=[0 for i in range(feature_number)] # массив приращений(нужен для работы механизма переноса разряда)
    start_code_value=int('1'*feature_number) # стартовое значение(нулевое число системы счисления с учетом разрядов, в данном случае - 1111)
    code_counter=0 # счетчик массива кодов
    while feature_variety**feature_number>code_counter: # цикл четырехразрядного приращения feature_variety-ричной системы счисления
        # выполнять пока не достигнуто максимальное число комбинаций(максимальное число в системе отсчета)
        code_of_set_list[code_counter]=start_code_value
        for i in range(feature_number): # цикл приращения
            code_of_set_list[code_counter]+=append_list[i] 
        code_counter+=1
        append_list[feature_number-1]+=1
        for j in range(feature_number-1): # цикл переноса разряда с права на лево
            if append_list[feature_number-1-j]==feature_variety*(int(round(0.1**(-j), 1))):
                append_list[feature_number-1-j]=0
                append_list[feature_number-2-j]+=(int(round(0.1**(-j-1), 1)))
    return code_of_set_list






dwg = svgwrite.Drawing('C:\\test.svg', profile='tiny', size=(u'100%', u'100%'))

# градиенты вынесены отдельно так как непонятно как создать отдельный объект градиента в каждом объекте карты
# кроме того экономичнее иметь три градиента вместо 81
rad_grad1=svgwrite.gradients.RadialGradient(id="grad1")
rad_grad1.add_stop_color(offset='0%', color='rgb(230, 25, 25)', opacity=None)
rad_grad1.add_stop_color(offset='100%', color='white', opacity=None)
dwg.defs.add(rad_grad1)

rad_grad2=svgwrite.gradients.RadialGradient(id="grad2")
rad_grad2.add_stop_color(offset='0%', color='rgb(50, 165, 80)', opacity=None)
rad_grad2.add_stop_color(offset='100%', color='white', opacity=None)
dwg.defs.add(rad_grad2)

rad_grad3=svgwrite.gradients.RadialGradient(id="grad3")
rad_grad3.add_stop_color(offset='0%', color='rgb(20, 50, 250)', opacity=None)
rad_grad3.add_stop_color(offset='100%', color='white', opacity=None)
dwg.defs.add(rad_grad3)

class Card: # класс карты, каждая карта будет уникальным объектом этого класса
    card_widht=183 #  ширина карты, из неё высчитывается высота карты и центры фигур
    # вынесенна отдельна т.к. к этой переменной обращаются до создания объектов
    def __init__(self):
        self.fill_color='rgb(00, 250, 00)' # цвет заливки фигуры по умолчанию - зеленый
        self.border_color='rgb(0, 200, 0)' # цвет контура фигуры по умолчанию - темно зеленый
        self.fill_type='url(#grad2)'  # цвет заливки по умолчанию - зеленый
        self.figure_size=30 # размер фигуры -половина её длинны или радиус круга
 #       self.cardx, self.cardy=20, 30 # верхний левый угол карты
        self.card_height= self.card_widht//0.7 #  высота карты

# методы смены цвета фигуры        
    def set_color1(self): # смена цвета на красный
        self.fill_color='rgb(250, 0, 0)'
        self.border_color='rgb(200, 0, 0)'
        self.fill_type='url(#grad1)'  # при инициализации цвета определяется какой градиент использовать, если надо
    def set_color2(self): # смена цвета на зеленый
        self.fill_color='rgb(00, 250, 00)'
        self.border_color='rgb(0, 200, 0)'
        self.fill_type='url(#grad2)'
    def set_color3(self): # смена цвета на синий
        self.fill_color='rgb(0, 0, 250)'
        self.border_color='rgb(0, 0, 200)'
        self.fill_type='url(#grad3)'

# методы смена типа заполнения - полной, градиентом, ничем, штриховкой(?)
# этот метод нужно запускать обязательно
    
    def set_fill1(self): # смена типа заполнения на пустой
        self.fill_type='none'
        
    def set_fill2(self): # по умолчанию заполнение уже стоит на градиенте правильного цвета
        pass 
        
    def set_fill3(self): # смена типа заполнения на заливку
        self.fill_type=self.fill_color

# методы задания колличества фигур, создает координаты для расположения центров этих фигур   
# figure_centreX/Y массив из координат центров, цикл отрисовки фигур отрабатывает по числу координат в массиве X
# координаты относительно края карты, Х всегда по середине карты, Y зависит от числа фигур
    def set_position1(self): # центра единственной фигуры, Y по середины карты
        # кортеж из одного элемента нужно завершать запятой
        self.figure_centreX, self.figure_centreY=(int(self.cardx+self.card_widht//2),), (int(self.cardy+self.card_height*0.5),)
    def set_position2(self): # центры двух фигур, Y на 1/3 и 2/3 высоты карты
        self.figure_centreX=(int(self.cardx+self.card_widht//2), int(self.cardx+self.card_widht//2)) 
        self.figure_centreY=(int(self.cardy+self.card_height*0.333), int(self.cardy+self.card_height*0.666))
    def set_position3(self): # центры трех фигур, Y на 0.2, 0.5 и 0.8 высоты карты
        self.figure_centreX=(int(self.cardx+self.card_widht//2), int(self.cardx+self.card_widht//2), int(self.cardx+self.card_widht//2)) 
        self.figure_centreY=(int(self.cardy+self.card_height*0.20), int(self.cardy+self.card_height*0.5), int(self.cardy+self.card_height*0.8))
        
        
# методы форм, собственно рисуют заданные фигуры, использует определенные выше переменные объекта для 
# цвета(color), заполнения(fill), центра(figure_centreX) фигуры
    

    def draw_figure1(self): # рисование круга
        for i in range(len(self.figure_centreX)): # рисовать столько раз, сколько задано координат центра
            dwg.add(dwg.circle(center=(self.figure_centreX[i],self.figure_centreY[i]),
            r=self.figure_size, 
            stroke=self.border_color,
            fill=self.fill_type,
            stroke_width=3))
        
    def draw_figure2(self): # рисование креста, через функцию отрисовки многоугольника
        for i in range(len(self.figure_centreX)):
             dwg.add(dwg.polygon(points=Card.quarter_figure_expand(self.figure_centreX[i], self.figure_centreY[i],  
              [(self.figure_centreX[i],self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size//2.7,self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size//2.7,self.figure_centreY[i]+self.figure_size//2.7), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i]+self.figure_size//2.7), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i])]),    
              stroke=self.border_color,
              fill=self.fill_type,
              stroke_width=3))    

    def draw_figure3(self): # рисование квадрата, через функцию отрисовки многоугольника
        for i in range(len(self.figure_centreX)):
             dwg.add(dwg.polygon(points=Card.quarter_figure_expand(self.figure_centreX[i], self.figure_centreY[i],  
              [(self.figure_centreX[i],self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i])]),    
              stroke=self.border_color,
              fill=self.fill_type,
              stroke_width=3))
            
    def draw_figure4(self): # рисование восьмиконечной звезды, через функцию отрисовки многоугольника
         for i in range(len(self.figure_centreX)):
              dwg.add(dwg.polygon(points=Card.quarter_figure_expand(self.figure_centreX[i], self.figure_centreY[i],  
               [(self.figure_centreX[i],self.figure_centreY[i]+self.figure_size), 
                (self.figure_centreX[i]+self.figure_size//4.3,self.figure_centreY[i]+self.figure_size//2), 
                (self.figure_centreX[i]+self.figure_size//1.4,self.figure_centreY[i]+self.figure_size//1.4), 
                (self.figure_centreX[i]+self.figure_size//2,self.figure_centreY[i]+self.figure_size//4.3), 
                (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i])]),    
               stroke=self.border_color,
               fill=self.fill_type,
               stroke_width=3))   
    
 
    
    def quarter_figure_expand(centerX, centerY, quart): # функция дорисовки четверти в полную фигуру
# centerX, centerY центр фигуры, quart нижняя правая четверть отрисованной фигуры в виде массива точек
        dots=len(quart) # число точек четверти
        sx,sy=0, -2 # множители для отрисовки
        d=0
        for j in range(dots-1): # проецироем каждую после первой точку либо по одной оси
            d-=2 # отрисовка идет против часовой стрелки, следующая точка проецирует расположенную(в массиве) ранее донора предыдущей
            quart+=[(quart[d][0]+(quart[d][0]-centerX)*sx, quart[d][1]+(quart[d][1]-centerY)*sy)]
        sx,sy=-2,0
        d=0        
        for j in range(dots-1): # либо по другой, sx sy нужны для этого 
            d-=2
            quart+=[(quart[d][0]+(quart[d][0]-centerX)*sx, quart[d][1]+(quart[d][1]-centerY)*sy)]
        sx,sy=0,2  
        d=0        
        for j in range(dots-1):
            d-=2
            quart+=[(quart[d][0]+(quart[d][0]-centerX)*sx, quart[d][1]+(centerY-quart[d][1])*sy)]
        return quart
    
  
    def draw_card_borders(self): # метод создания границ карты 
        dwg.add(dwg.rect((self.cardx, self.cardy), (self.card_widht, self.card_height),  
        stroke=svgwrite.rgb(10, 10, 16, '%'),
        fill='none'))
        
        
init_cardX=20 # значение самой левой карты
gap=3 # промежуток между картами
cardX=init_cardX+Card.card_widht*2+gap*2 # значение для текущей карты !!!
cardY=30 #
card_object=[] # массив хранящий экземпляры карт
code_list=generate_set()
for i in range(len(code_list)):
    
    card_object.append(Card())
# определение расположения карты на листе формата A4
# определение X исходя из горионтальной позиции    
    if cardX==init_cardX+card_object[i].card_widht*2+gap*2:  
        cardX=init_cardX
    elif cardX==init_cardX:
        cardX+=card_object[i].card_widht+gap
    elif cardX==init_cardX+card_object[i].card_widht+gap:
        cardX+=card_object[i].card_widht+gap
# определение Y исходя из вертикальной позиции         
    if i%3==0 and i!=0:
        cardY+=Card.card_widht//0.7+gap
    if i%9==0 and i!=0:
        cardY+=60
# сохранение полученных координат 
    card_object[i].cardx= cardX 
    card_object[i].cardy= cardY 

# расшифровка полученного кода
    code=str(code_list[i]) 
# четвертый с права регистр (если есть) - цвет
    if len(code)==4:
        if code[-4]=='1':
            card_object[i].set_color1()
        if code[-4]=='2':
            card_object[i].set_color2()
        if code[-4]=='3':
            card_object[i].set_color3()
# третий с права регистр - заполнение       
    if code[-3]=='1':
        card_object[i].set_fill1()
    if code[-3]=='2':
        card_object[i].set_fill2()
    if code[-3]=='3':
        card_object[i].set_fill3()
# второй с права регистр - число фигур         
    if code[-2]=='1':
        card_object[i].set_position1()
    if code[-2]=='2':
        card_object[i].set_position2()
    if code[-2]=='3':
        card_object[i].set_position3()
# самый правый регистр - определение формы и отрисовка содержимого карты     
    if code[-1]=='1':
        card_object[i].draw_figure1()
    if code[-1]=='2':
        card_object[i].draw_figure2()
    if code[-1]=='3':
        card_object[i].draw_figure3()
# отрисовка границ карты        
    card_object[i].draw_card_borders()
  
    
dwg.save()    
