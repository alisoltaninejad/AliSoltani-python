students=[
    ('ali',[12,20,18,19]),
    ('reza',[8,14,18]),
    ('samad',[13,3,6]),
]

highest_grade = 0
lowest_grade = 20
highest_student = ""
lowest_student = ""

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
    
    if average > highest_grade:
        highest_grade = average
        highest_student = name
    if average < lowest_grade:
        lowest_grade = average
        lowest_student = name

print(f"بالاترین نمره: {highest_grade:.1f} {highest_student}")
print(f"پایین‌ترین نمره: {lowest_grade:.1f} {lowest_student}")
