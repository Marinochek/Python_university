# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))
    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
