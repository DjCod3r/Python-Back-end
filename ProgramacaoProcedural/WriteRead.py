

try:
    file = open('test.txt', 'w+')
    file.write('Hello World!\n')
    file.write('Hello World!')


    file.seek(0,0)
    print(file.read())


    file.seek(0,0)
    print(file.readline(), end='')

    file.seek(0,0)

finally:
    file.close()



with open('test.txt', 'r') as file:
    print(file.read())