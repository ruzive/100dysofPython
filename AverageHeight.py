student_heights = input('Input a list of student heights ').split()
sum_student_height = 0
sum_student_count = 0
tallest_height = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_student_count +=1
    sum_student_height += student_heights[n]
    if n != 0:
        if student_heights[n] > tallest_height:
            tallest_height = student_heights[n]
    else:
        tallest_height = student_heights[n]






print(f'The tallest student is of height: {tallest_height}')
print(f'sum of all student heights is : {sum_student_height}')
print(f'the list has : {sum_student_count} number of students')
print(f'The average height is: {round(sum_student_height/sum_student_count,0)}')
