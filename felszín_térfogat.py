#Ha rajtam múlna nem így csinálnám, de igyekeztem függvény-a-függvényben módszerrel :D

def volume_and_surface(a,b,c):
    def volume_(a,b,c):
        def rectangel_area(a,b):
            area = a*b
            return area
        volume = rectangel_area(a,b)*c
        return volume
    result_v = volume_(a,b,c)
    def surface(a,b,c):
        def rectangel_area(a,b):
            area = a*b
            return area
        surface = 2*(rectangel_area(a,b) + a*c + c*b)
        return surface
    result_s = surface(a,b,c)
    return f"""V = {round(result_v, 3)}
    A = {round(result_s, 3)}"""


