import svgwrite
class Card: # класс карты, каждая карта будет уникальным объектом этого класса
    def __init__(self):
        self.fill_color='rgb(00, 250, 00)' # цвет заливки фигуры по умолчанию - зеленый
        self.border_color='rgb(0, 200, 0)' # цвет контура фигуры по умолчанию - темно зеленый
        self.gradient_color='url(#grad2)'  # цвет градиента по умолчанию - зеленый
        self.pattern_color='url(#pat2)' # цвет узора по умолчанию - зеленый
        self.figure_size=30 # размер фигуры -половина её длинны или радиус круга
 #       self.cardx, self.cardy=20, 30 # верхний левый угол карты
        self.card_widht=183 #  ширина карты, из неё высчитывается высота карты и центры фигур
        self.card_height= self.card_widht//0.7 #  высота карты


# методы смены цвета фигуры
# с начала переопределяются цвета для контура фигуры, и если они будут, 
# для заливки, градиента, узора. Если признаков 3 - остается цвет по умолчанию 
    def set_color1(self): # смена цвета на красный
        self.border_color='rgb(200, 0, 0)'
        self.fill_color='rgb(250, 0, 0)'
        self.gradient_color='url(#grad1)'  
        self.pattern_color='url(#pat1)'
    def set_color2(self): # смена цвета на зеленый
        self.border_color='rgb(0, 200, 0)'
        self.fill_color='rgb(00, 250, 00)'
        self.gradient_color='url(#grad2)'
        self.pattern_color='url(#pat2)'
    def set_color3(self): # смена цвета на синий
        self.border_color='rgb(0, 0, 200)'
        self.fill_color='rgb(0, 0, 250)'
        self.gradient_color='url(#grad3)'
        self.pattern_color='url(#pat3)'
    def set_color4(self): # смена цвета на черный
        self.border_color='rgb(0, 0, 0)'
        self.fill_color='rgb(50, 50, 50)'
        self.gradient_color='url(#grad4)'
        self.pattern_color='url(#pat4)'
        
# методы смена типа заполнения - полной, градиентом, ничем, обратным градиентом
    def set_fill1(self): # смена типа заполнения на пустой
        self.fill_type='none'
    def set_fill2(self): # смена типа заполнения на градиент
        self.fill_type=self.gradient_color
    def set_fill3(self): # смена типа заполнения на заливку
        self.fill_type=self.fill_color
    def set_fill4(self): # смена типа заполнения на обратный градиент(заменить на узор)
        self.fill_type=self.pattern_color

# методы задания колличества фигур, создает координаты для расположения 
# центров этих фигур   
# figure_centreX/Y кортеж из координат центров, цикл отрисовки фигур 
# отрабатывает по числу координат в figure_centreX
# координаты относительно края карты, Х по середине карты(или на 28% 72% ширины) 
# Y зависит от числа фигур
    def set_position1(self): # центра единственной фигуры, Y по середины карты
        # кортеж из одного элемента нужно завершать запятой
        self.figure_centreX=(int(self.cardx+self.card_widht*0.5),)
        self.figure_centreY=(int(self.cardy+self.card_height*0.5),)
    def set_position2(self): # центры двух фигур, Y на 1/3 и 2/3 высоты карты
        self.figure_centreX=(int(self.cardx+self.card_widht*0.5), 
                             int(self.cardx+self.card_widht*0.5)) 
        self.figure_centreY=(int(self.cardy+self.card_height*0.333), 
                             int(self.cardy+self.card_height*0.666))
    def set_position3(self): # центры трех фигур, Y на 0.2, 0.5 и 0.8 высоты карты
        self.figure_centreX=(int(self.cardx+self.card_widht*0.5), 
                             int(self.cardx+self.card_widht*0.5), 
                             int(self.cardx+self.card_widht*0.5)) 
        self.figure_centreY=(int(self.cardy+self.card_height*0.2), 
                             int(self.cardy+self.card_height*0.5), 
                             int(self.cardy+self.card_height*0.8))
    def set_position4(self): # центры четырех фигур, Y на 0.35 и 0.65 высоты карты
        self.figure_centreX=(int(self.cardx+self.card_widht*0.28), 
                             int(self.cardx+self.card_widht*0.28), 
                             int(self.cardx+self.card_widht*0.72),
                             int(self.cardx+self.card_widht*0.72))
        self.figure_centreY=(int(self.cardy+self.card_height*0.35), 
                             int(self.cardy+self.card_height*0.65), 
                             int(self.cardy+self.card_height*0.35),
                             int(self.cardy+self.card_height*0.65))
     
# методы форм, собственно рисуют заданные фигуры, использует определенные выше переменные объекта для 
# цвета(color), заполнения(fill), центра(figure_centreX) фигуры
    def draw_figure1(self, dwg): # рисование круга
        for i in range(len(self.figure_centreX)): # рисовать столько раз, сколько задано координат центра
            dwg.add(dwg.circle(center=(self.figure_centreX[i],self.figure_centreY[i]),
            r=self.figure_size, 
            stroke=self.border_color,
            fill=self.fill_type,
            stroke_width=3))
    def draw_figure2(self, dwg): # рисование креста, через функцию отрисовки многоугольника
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
    def draw_figure3(self, dwg): # рисование квадрата, через функцию отрисовки многоугольника
        for i in range(len(self.figure_centreX)):
             dwg.add(dwg.polygon(points=Card.quarter_figure_expand(self.figure_centreX[i], self.figure_centreY[i],  
              [(self.figure_centreX[i],self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i]+self.figure_size), 
               (self.figure_centreX[i]+self.figure_size,self.figure_centreY[i])]),    
              stroke=self.border_color,
              fill=self.fill_type,
              stroke_width=3))
    def draw_figure4(self, dwg): # рисование восьмиконечной звезды, через функцию отрисовки многоугольника
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
    
# метод дорисовки четверти в полную фигуру
# centerX, centerY центр фигуры, 
# quart нижняя правая четверть отрисованной фигуры в виде массива точек
    def quarter_figure_expand(centerX, centerY, quart):
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
 
# метод отрисовки границ карты
    def draw_card_borders(self, dwg):  
        dwg.add(dwg.rect((self.cardx, self.cardy), (self.card_widht, self.card_height),  
        stroke=svgwrite.rgb(10, 10, 16, '%'),
        fill='none'))
        
