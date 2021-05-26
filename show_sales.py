def bakery_run(args):
    start_run = 1 if len(args) == 1 else int(args[1])
    max_run = 0 if len(args) < 3 else int(args[2])
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        i = 1
        string_lines = f.readline().strip()
        while string_lines:
            if i != max_run:
                if i >= start_run:
                    print(string_lines)
                    string_lines = f.readline().strip()
                else:
                    string_lines = f.readline().strip()
            else:
                break
            i += 1


if __name__ == '__main__':
    import sys
    exit(bakery_run(sys.argv))