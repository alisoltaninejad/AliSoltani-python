# محاسبه  نمرات دانشجویان و مشخص کردن وضعیت قبولی هر کدام
students=[
    ('ali',[12,20,18,19]),
    ('reza',[8,14,18]),
    ('samad',[13,3,6]),
]
for student in students:
    name= student[0]
    grades=student[1]
    
    total=0
    for grade in grades:
        total+=grade
        
    average =  total / len(grades)

    if average >=10 :
        status = "✅ قبول شد"
    else : 
        status = "❌ مردود شد"

    print(f'{student[0]}:{average:.1f}=>{status}')
