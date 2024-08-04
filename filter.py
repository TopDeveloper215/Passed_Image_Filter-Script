import csv
import os
import shutil
from datetime import datetime

file_path = './329_passed_list.csv'
image_folder = './origin_image'

lists = []
passed_list = []
unique_names = set()
unique_types = set()

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if not row:
            continue
        file_path = row[2]
        lists.append(file_path)
        name_component = file_path.split('\\')[1]
        unique_names.add(name_component)
        list_path = file_path.split('\\')

unique_names = sorted(list(unique_names))

for i, name in enumerate(unique_names, start=1):
    print(f"\n{i}. {name}")
name_index = int(input("\nSelect name :")) - 1
name_input = unique_names[name_index]

for list in lists:
    list= str(list)
    list_path = list.split('\\')
    if list_path[1] == name_input:
        if len(list_path) > 3:
            type_input = list_path[2]
            unique_types.add(type_input)
        elif len(list_path) == 3:
            unique_types.add('none')

unique_types = sorted(unique_types)

for i, type in enumerate(unique_types, start=1):
    print(f"\n{i}. {type}")
type_index = int(input("\nSelect type : ")) - 1
type_input = unique_types[type_index]
print()

for list in lists:
    list = str(list)
    list_component = list.split('\\')   
    name = list_component[1]
    if len(list_component) > 3:
        type = list_component[2]
        if name == name_input and type == type_input:
            each_passed_list = list_component[-1]
            passed_list.append(each_passed_list)
    else:
        if name == name_input and type_input == 'none':
            each_passed_list = list_component[-1]
            passed_list.append(each_passed_list)
all_images = os.listdir(image_folder)
filtered_images = [image for image in all_images if image in passed_list]

if not filtered_images:
    print('WARNING : Passed images not found!')
else:
    current_date = datetime.now()
    month_day = f"{current_date.month}.{current_date.day} ({current_date.strftime('%p')})"

    if name_input and type_input != 'none':
        output_folder_name = f"{month_day}_passed image_{name_input}({type_input})"
    else:
        output_folder_name = f"{month_day}_passed image_{name_input}"

    filtered_folder = os.path.join('./', output_folder_name)
    os.makedirs(filtered_folder, exist_ok=True)

    for image in filtered_images:
        source_path = os.path.join(image_folder, image)
        output_path = os.path.join(filtered_folder, image)
        shutil.move(source_path, output_path)
        print(f"Moved {image} to {filtered_folder}")

terminal_width = shutil.get_terminal_size().columns
done_message = "--------------Done---------------"
input("\n" + done_message.center(terminal_width))