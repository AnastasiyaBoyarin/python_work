import re, csv


def get_data(list_files):
    header = ['System manufacturer', 'Name of OS',
              'Code of Product', 'Type of system']

    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name_reg = re.compile(r'Название ОС:\s*\S*')
    os_code_reg = re.compile(r'Код продукта:\s*\S*')
    os_type_reg = re.compile(r'Тип системы:\s*\S*')

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file_path in list_files:
        with open(file_path, 'r', encoding='utf-8') as fr_obj:
            data = fr_obj.read()
            os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
            os_name_list.append(os_name_reg.findall(data)[0].split()[2])
            os_code_list.append(os_code_reg.findall(data)[0].split()[2])
            os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    main_data = [[os_prod_list[i], os_name_list[i], os_code_list[i],
                  os_type_list[i]] for i in range(0, len(os_prod_list))]

    main_data.insert(0, header)

    return main_data


def write_to_csv(list_files, output_file_name):
    res_main_data = get_data(list_files)

    with open(output_file_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in res_main_data:
            f_n_writer.writerow(row)


list_of_files = ('info_1.txt', 'info_2.txt', 'info_3.txt')
write_to_csv(list_of_files, 'result.csv')
