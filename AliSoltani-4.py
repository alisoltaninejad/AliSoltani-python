import math

def eq1(x, y):
    return -(x/y * math.log(x/y))

def eq2(x):
    return 1 / (1 + math.exp(-x))

def eq3(x):
    return math.exp(x) / math.exp(x**2)

def eq4(x, y, y1):
    return (1/x) * (y - y1)

def eq5(x):
    return math.sqrt(x * math.log(x))

# فراخوانی توابع با مقادیر صحیح که خطا ندهد
print("eq1(2, 3):", eq1(2, 3))  # مقدار معتبر: y ≠ 0 و x/y > 0
print("eq2(1):", eq2(1))        # هر عددی قابل قبول است
print("eq3(1):", eq3(1))        # هر عددی قابل قبول است
print("eq4(2, 5, 3):", eq4(2, 5, 3))  # x ≠ 0
print("eq5(2):", eq5(2))        # x > 1 (برای x=1 مقدار log(1)=0 میشود)

