import svgwrite

# функция генерирует массив кодов
from generate_set import generate_set

# создание градиентов и паттернов
from set_gradients import set_gradients
from set_patterns import set_patterns

 # класс карты, каждая карта будет уникальным объектом этого класса
from card_class import Card

# папка назначения
folder_path = 'C:\\'
file_path = folder_path+'print0.svg'
dwg = svgwrite.Drawing(file_path, size=(u'100%', u'100%'))

card_object = [] # массив хранящий экземпляры карт
# функция генерирует массив кодов, определяющих изображение на картах
# принимает feature_numbe - число признаков и feature_variety - вариативность признака
code_list = generate_set(feature_number=4,feature_variety=4)
card_widht = 183 #  ширина карты, из неё высчитывается X для позиции следующей карты
init_cardX = 20 # значение самой левой карты
gap = 3 # промежуток между картами
cardX = init_cardX+card_widht*2+gap*2 # значение для текущей карты !!!
cardY = 30 #     

for i in range(len(code_list)):
    card_object.append(Card())
# определение расположения карты на листе формата A4
# определение X исходя из горионтальной позиции    
    if cardX == init_cardX+card_object[i].card_widht*2+gap*2:  
        cardX = init_cardX
    elif cardX == init_cardX:
        cardX += card_object[i].card_widht+gap
    elif cardX == init_cardX+card_object[i].card_widht+gap:
        cardX += card_object[i].card_widht+gap
# определение Y исходя из вертикальной позиции         
    if i%3 == 0 and i != 0:
        cardY += card_object[i].card_widht//0.7+gap
    if i%9 == 0 and i != 0:
        cardY = 30
# после девятой карты сбрасываем Y, сохраняем старый файл и создаем новый        
        dwg.save()
        file_path = file_path.replace(str(i//9-1)+'.svg', str(i//9)+'.svg')
        dwg = svgwrite.Drawing(file_path, size=(u'100%', u'100%'))
# для каждого файла нового файла требуется пересоздание градиентов и паттернов        
        set_gradients(dwg)
        set_patterns(dwg)
        
# сохранение полученных координат 
    card_object[i].cardx = cardX 
    card_object[i].cardy = cardY 

# расшифровка полученного кода
    code = str(code_list[i]) 
# четвертый с права регистр (если есть) - цвет
# если признаков только три - цвет меняться не будет, вариант для дальтоников
    if len(code) == 4:
        if code[-4] == '1':
            card_object[i].set_color1()
        if code[-4] == '2':
            card_object[i].set_color2()
        if code[-4] == '3':
            card_object[i].set_color3()
        if code[-4] == '4':
            card_object[i].set_color4()
# третий с права регистр - заполнение       
    if code[-3] == '1':
        card_object[i].set_fill1()
    if code[-3] == '2':
        card_object[i].set_fill2()
    if code[-3] == '3':
        card_object[i].set_fill3()
    if code[-3] == '4':
        card_object[i].set_fill4()
# второй с права регистр - число фигур         
    if code[-2] == '1':
        card_object[i].set_position1()
    if code[-2] == '2':
        card_object[i].set_position2()
    if code[-2] == '3':
        card_object[i].set_position3()
    if code[-2] == '4':
        card_object[i].set_position4()
# самый правый регистр - определение формы и отрисовка содержимого карты     
    if code[-1] == '1':
        card_object[i].draw_figure1(dwg)
    if code[-1] == '2':
        card_object[i].draw_figure2(dwg)
    if code[-1] == '3':
        card_object[i].draw_figure3(dwg)
    if code[-1] == '4':
        card_object[i].draw_figure4(dwg)
# отрисовка границ карты        
    card_object[i].draw_card_borders(dwg)
  
dwg.save()   
