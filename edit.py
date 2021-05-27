'''Параметры ввода для редактирования: №строки новое_значение'''

def edit_sales(args):
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        v = int(args[1])
        line = f.readline()
        for i in range(1, v + 1):
            if line:
                if i == v:
                    f.seek(n)
                    f.writelines(f'{args[2]}\n')
                    break
                else:
                    n = f.tell()
                    line = f.readline()
            else:
                print(f'Всего записей: {i - 1}')
                break


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('Введите данные со следующими параметрами: №строки новое_значение')
    if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
        if len(sys.argv) < 3 or sys.argv == '':
            sys.argv.append('   ')
        exit(edit_sales(sys.argv))
    elif len(sys.argv) > 1 and (not sys.argv[1].isdigit() or int(sys.argv[1] or not sys.argv[2]) <= 0):
        print('Введите целое положительное число номера строки!')

#python edit.py