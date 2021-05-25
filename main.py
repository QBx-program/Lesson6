# Задание 1 и 2*

list_tuple = []
dict_ip = {}

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    string_txt = f.readline().strip()
    while string_txt:
        string_lines = string_txt.split(' ')
        tuples = (string_lines[0], string_lines[5][1:], string_lines[6])
        dict_ip.setdefault(string_lines[0], 1)
        dict_ip[string_lines[0]] += 1
        list_tuple.append(tuples)
        string_txt = f.readline().strip()
ip_spam_attempt = max(dict_ip.values())
print('IP спамера:', *(k for k, v in dict_ip.items() if v == ip_spam_attempt))

# Задание 3

dict_hobby = {}

with open('users.csv', 'r', encoding='UTF-8') as f:
    string_txt = f.read()
    list_arg_user = string_txt.splitlines()

with open('hobby.csv', 'r', encoding='UTF-8') as f:
    string_txt = f.read()
    list_arg_hobby = string_txt.splitlines()

list_null = (None for i in range(len(list_arg_user) - len(list_arg_hobby)) if len(list_arg_user) - len(list_arg_hobby) > 0)
list_arg_hobby.extend((i for i in list_null))
dict_hobby = {user: hobby for user, hobby in zip(list_arg_user, list_arg_hobby)}

with open('dict.csv', 'w', encoding='UTF-8') as f:
    f.write(str(dict_hobby))

with open('dict.csv', 'r', encoding='UTF-8') as f:
    print(f.read())

# dict_hobby = {v: None for v in list_arg_user}
# for i, v in enumerate(list_arg_user):
#     dict_hobby[list_arg_user[i]] = list_arg_hobby[i]



