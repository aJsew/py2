import csv

def get_data(file_name):
    with open(file_name, 'r+') as file:
        reader = file.readlines()
        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []

        for row in reader:
            if 'Изготовитель системы' in row:
                os_prod_list.append(row)
            if  'Название ОС' in row:
                os_name_list.append(row)
            if  'Код продукта' in row:
                os_code_list.append(row)
            if  'Тип системы' in row:
                os_type_list.append(row)
    return os_prod_list, os_name_list, os_code_list, os_type_list

def write_to_csv(fileWriteName, fileReadName):
    data = get_data(fileReadName)
    print(data)
    with open (fileWriteName, 'w') as file:
        writer = csv.writer(file)
        for a in data:
            writer.writerow(a)


write_to_csv('1.csv', 'info_1.txt')

get_data('info_1.txt')
get_data('info_2.txt')
get_data('info_3.txt')


