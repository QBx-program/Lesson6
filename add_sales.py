def add_sales(args):
    program, *args = args
    with open('bakery.csv', 'a', encoding='UTF-8') as f:
        for i in args:
            f.write(f'{i}\n')


if __name__ == '__main__':
    import sys
    exit(add_sales(sys.argv))