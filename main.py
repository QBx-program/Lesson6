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