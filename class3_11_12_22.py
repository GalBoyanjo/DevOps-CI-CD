try:
    my_file = open('C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/test_file.txt', 'r', encoding='utf-8')
    content = my_file.write('123')
    print('asd')
except IOError as x:
    print(x)
finally:
    my_file.close()

with open('C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/test_file.txt', 'w', encoding='utf-8') as my_file:
    cont = my_file.write('hello')
print(cont)


