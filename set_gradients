import svgwrite
# градиенты вынесены отдельно так как непонятно как создать 
# отдельный объект градиента в каждом объекте карты
# сейчас они пересоздаются при каждом открытии файла
def set_gradients(dwg):
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
    
    rad_grad4=svgwrite.gradients.RadialGradient(id="grad4")
    rad_grad4.add_stop_color(offset='0%', color='rgb(0, 0, 0)', opacity=None)
    rad_grad4.add_stop_color(offset='100%', color='white', opacity=None)
    dwg.defs.add(rad_grad4)
