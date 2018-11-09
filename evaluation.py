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
        print("Sans faute!")
    tuple_2 = ('0', grade)
    return (tuple_2)


good_answers = ['B', 'C', 'C', 'A', 'A', 'A', 'D', 'C', 'A', 'B', 'C', 'A', 'C', 'C']
stud_answers = input('Entrez les réponses, 0 si pas de réponse:')
scale = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 4]
domain = ['A', 'B', 'C', 'D', 'E', '0']

print(evaluate(good_answers, stud_answers, domain, scale))
