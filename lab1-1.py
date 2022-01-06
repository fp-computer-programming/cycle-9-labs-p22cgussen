# Charlie CCG 1/6/2022

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin", "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for row_numb, row in enumerate(rows):
    for name_numb, name in enumerate(rows):
        student = rows[row_numb][name_numb]
        student_numb = len(student) - 1
        if student[student_numb] == "s":
            student += "'"
        else:
            student += "'s"
        print(student)



