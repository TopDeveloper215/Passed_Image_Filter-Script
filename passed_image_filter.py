import csv
import os
import shutil
from datetime import datetime

file_path = './data.csv'
image_folder = './8.origin_images'

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
        if len(list_path) > 3:
            type_input = list_path[2]
            unique_types.add(type_input)
        elif len(list_path) == 3 :
            type_input = 'none'
            unique_types.add(type_input)

unique_names = sorted(list(unique_names))
unique_types = sorted(list(unique_types))

print("All names: \n")
for i, name in enumerate(unique_names, start=1):
    print(f"{i}. {name}")
name_index = int(input("\n Select name :")) - 1
name_input = unique_names[name_index]

print("All types: \n")
for i, type in enumerate(unique_types, start=1):
    print(f"{i}. {type}")
type_index = int(input("\n Select type : ")) - 1
type_input = unique_types[type_index]

for list in lists:
    list_component = list.split('\\')
    if len(list_component) > 3:
        name = list_component[1]
        type = list_component[2]
        if name == name_input and type == type_input:
            each_passed_list = list_component[-1]
            passed_list.append(each_passed_list)
    elif len(list_component) == 3:
        name = list_component[1]
        if name == name_input:
            each_passed_list = list_component[-1]
            passed_list.append(each_passed_list)
all_images = os.listdir(image_folder)
filtered_images = [image for image in all_images if image in passed_list]

if filtered_images == []:
    print('Passed images not found')

current_date = datetime.now()
month_day = f"{current_date.month}.{current_date.day}"

if name_input and type_input != 'none':
    output_folder_name = f"{month_day}_Passed image_{name_input}({type_input})"
else:
    output_folder_name = f"{month_day}_Passed image_{name_input}"

filtered_folder = os.path.join('./', output_folder_name)
os.makedirs(filtered_folder, exist_ok=True)

for image in filtered_images:
    source_path = os.path.join(image_folder, image)
    output_path = os.path.join(filtered_folder, image)
    shutil.move(source_path, output_path)
    print(f"Moved {image} to {filtered_folder}")