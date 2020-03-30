import svgwrite
# установка узоров, пока заменены обратными градиентами
def set_patterns(dwg):
    rad_grad1=svgwrite.gradients.RadialGradient(id="pat1")
    rad_grad1.add_stop_color(offset='100%', color='rgb(230, 25, 25)', opacity=None)
    rad_grad1.add_stop_color(offset='0%', color='white', opacity=None)
    dwg.defs.add(rad_grad1)
    
    rad_grad2=svgwrite.gradients.RadialGradient(id="pat2")
    rad_grad2.add_stop_color(offset='100%', color='rgb(50, 165, 80)', opacity=None)
    rad_grad2.add_stop_color(offset='0%', color='white', opacity=None)
    dwg.defs.add(rad_grad2)
    
    rad_grad3=svgwrite.gradients.RadialGradient(id="pat3")
    rad_grad3.add_stop_color(offset='100%', color='rgb(20, 50, 250)', opacity=None)
    rad_grad3.add_stop_color(offset='0%', color='white', opacity=None)
    dwg.defs.add(rad_grad3)
    
    rad_grad4=svgwrite.gradients.RadialGradient(id="pat4")
    rad_grad4.add_stop_color(offset='100%', color='rgb(0, 0, 0)', opacity=None)
    rad_grad4.add_stop_color(offset='0%', color='white', opacity=None)
    dwg.defs.add(rad_grad4)
