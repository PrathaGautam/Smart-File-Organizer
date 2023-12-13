import os

path = input("Enter the directory path : ")


def is_valid_path(given_path):
    return os.path.exists(given_path)


# if is_valid_path(path):
#     # print(f"The given path '{path}' is valid.")
#     pass
# else:
#     print(f"Error! The given path '{path}' is invalid.")

if not is_valid_path(path):
    print(f"Error! The given path '{path}' is invalid.")

if not path or not is_valid_path(path):
    path = "/Users/prathagautam/Documents/File_Organizer_ExampleFolder"
    print("Using default directory!")

directory_list = os.listdir(path)
print(f"Files and directories in {path} are : ")
all_files = []
for file in directory_list:
    if file != '.DS_Store':  # .DS_Store file is used by McOS to store icon info etc
        # print(file)
        all_files.append(file)

print(all_files)


result = [item.split('.', 1) for item in all_files]
print("This is the result : ")
print(result)
chosen_files = []


for item in result:
    if len(item) > 1:
        full_path_of_item = os.path.join(path, f"{item[0]}.{item[1]}")
        # print(full_path_of_item)
        if os.path.isfile(full_path_of_item):
            chosen_files.append(f"{item[0]}.{item[1]}")

print("Printing all chosen files : ")
print(chosen_files)


file_extensions = {'Document_Files':
                       {'PDF Files': '.pdf',
                        'MS Word files': ('.docx', '.doc'),
                        'MS Powerpoint files': ('.pptx', '.ppt'),
                        'Text': ('.txt', '.rtf'),
                        'Spreadsheet_Files': ('.csv', '.xls', '.xlsx'),
                        },
                   'Image_Files': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif'),
                   'Audio_Files': ('.mp3', '.aac', '.wav', '.flac', '.m4a', '.flac'),
                   'Video_Files': ('.mp4', '.mov', '.avi', '.mkv', '.wmv'),
                   'Compressed_Files': ('.zip', '.tar', '.gz', '.7z', '.rar'),
                   'Programming_Files': ('.py', '.cpp', '.html', '.css'),
                   'Miscellaneous_Files': ('.app', '.dmg', '.plist', '.otf', '.lnk')
                   }

list_of_all_extensions = []

for folder_type, extension in file_extensions.items():
    if folder_type == 'Document_Files' and isinstance(extension, dict):
        for file_type, file_extension in extension.items():
            # print(file_extension)
            if isinstance(file_extension, tuple):
                list_of_all_extensions.extend(file_extension)
            else:
                list_of_all_extensions.append(file_extension)
    else:
        list_of_all_extensions.extend(extension)

# print("Printing the extensions : ")
# print(list_of_all_extensions)
