#Ali SWoltani Nejad
def calc_b(a, c, d):
    b = (a / c) + d
    return b

def calc_y(b, x, a):
    y = (b * x) / (a / x)
    return y

def calc_circleArea(r):
    pi = 3.14
    area = pi * r * r
    return area
b_result = calc_b(20, 4, 6)    
y_result = calc_y(b_result, 2, 10) 
circleArea_result = calc_circleArea(4) 

print(b_result)
print(y_result)
print(circleArea_result)
