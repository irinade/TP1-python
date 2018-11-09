import csv
csv_reader = csv.reader(open("marks.csv"))

good_answers = ['B', 'C', 'C', 'A', 'A', 'A', 'D', 'C', 'A', 'B', 'C', 'A', 'C', 'C']
scale = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 4]
domain = ['A', 'B', 'C', 'D', 'E', '0']
grade_M = 0
grade_F = 0
M = 0
F = 0

def evaluate(good_answers, stud_answers, domain, scale):
    if len(stud_answers) != 14:
        a = "Il n'y a pas le bon nombre de réponses"
        tuple_1 = ('1', a)
        print(tuple_1)
        quit()

    for element in stud_answers:
        if element in domain:
            print()
        else:
            c = "Il y a un caractère interdit."
            tuple_3 = ('1', c)
            print(tuple_3)
            quit()

    grade = 0

    for question_number in range(0, 14):
        if good_answers[question_number] == stud_answers[question_number]:
            grade = grade + scale[question_number]

    if grade > 20:
        grade = 20
        #print("Sans faute!")
    tuple_2 = ('0', grade)
    return (tuple_2)


for row in csv_reader:
    gender = row[1]
    stud_answers = row[2]
    num = row[0]
    grade = evaluate(good_answers, stud_answers, domain, scale)[1]  
    if gender == "M":
        grade_M = grade_M + grade
        M = M + 1
    else:
        grade_F = grade_F + grade
        F = F + 1

average_F = grade_F / F
average_M = grade_M / M

print("La moyenne des filles est de:", average_F, "sur 20", "et la moyenne des garçons est de:", average_M, "sur 20.")
