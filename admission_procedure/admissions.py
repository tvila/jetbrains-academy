n = int(input())

with open('applicants_test.txt', 'r') as file:
    data = [line.split() for line in file]

order_list = []
special_exam = 6
order_scores = {'Biotech': [3, 2], 'Chemistry': [3], 'Engineering': [4, 5], 'Mathematics': [4], 'Physics': [2, 4]}
counter = {'Biotech': 0, 'Chemistry': 0, 'Engineering': 0, 'Mathematics': 0, 'Physics': 0}
full_list = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
accepted = []

for i in full_list.keys():
    for j in range(7, 10):
        for k in data:
            if k[j] == i:
                if len(order_scores[k[j]]) == 1:
                    median = float(k[order_scores[k[j]][0]])
                    special = float(k[special_exam])
                    score = str(float(max(median, special)))
                    name = " ".join([k[0], k[1], k[j], str(j - 5), score])
                    order_list.append(name.split())
                elif len(order_scores[k[j]]) == 2:
                    median = float((float(k[order_scores[k[j]][0]]) + float(k[order_scores[k[j]][1]])) / 2)
                    special = float(k[special_exam])
                    score = str(float(max(median, special)))
                    name = " ".join([k[0], k[1], k[j], str(j - 5), score])
                    order_list.append(name.split())
            else:
                continue

order_list.sort(key=lambda x: (float(x[3]), x[2], -float(x[4]), x[0], x[1]))

for student in order_list:
    name = " ".join([student[0], student[1], student[4]])
    #
    if counter[student[2]] == n or " ".join(student[0:2]) in accepted:
        continue
    else:
        full_list[student[2]].append(name)
        counter[student[2]] += 1
        accepted.append(" ".join(student[0:2]))

for department in full_list.keys():
    file_name = department.lower() + '.txt'
    dep_sorted = sorted(full_list[department], key=lambda x: (-float(x.rsplit(' ', 1)[1]), x.rsplit(' ', 1)[0]))

    file = open(file_name, 'w', encoding='utf-8')
    for text in dep_sorted:
        file.write(text + '\n')
    file.close()
