import os
import shutil

path = input("Enter the directory path : ")


def is_valid_path(given_path):
    return os.path.exists(given_path)


if not is_valid_path(path):
    print(f"Error! The given path '{path}' is invalid.")


# Using the default directory if the path doesn't exist or is an invalid path
if not path or not is_valid_path(path):
    path = "/Users/prathagautam/Documents/File_Organizer_ExampleFolder"
    print("Using default directory!")

directory_list = os.listdir(path)
# print(f"Files and directories in {path} are : ")
all_files = []
for file in directory_list:
    if file != '.DS_Store':  # .DS_Store file is used by McOS to store icon info etc
        # print(file)
        all_files.append(file)

# prints all files that are located in the given path
# print(all_files)


# Splitting the list of all files into a list of filename and its extension :
result = [item.split('.', 1) for item in all_files]
# print("This is the result : ")
# print(result)


# Creating a list of filename along with their extensions :
chosen_files = []
for item in result:
    if len(item) > 1:
        full_path_of_item = os.path.join(path, f"{item[0]}.{item[1]}")
        # print(full_path_of_item)
        if os.path.isfile(full_path_of_item):
            chosen_files.append(f"{item[0]}.{item[1]}")

# print("Printing all chosen files : ")
# print(chosen_files)


# custom file extensions created by myself, includes most common extensions in Mac
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

# print("Printing the list of all extensions in file_extensions dict : ")
# print(list_of_all_extensions)
#
#
#
#
folders_to_create = []
sub_folders_to_create = []

# Creating new folders and sub-folders in the given path, based on the files present :


def categorize_file(filename, extensions_dict, path):
    for category, extensions in extensions_dict.items():
        if isinstance(extensions, dict):
            for subcategory, sub_extensions in extensions.items():
                if filename.lower().endswith(sub_extensions):
                    folders_to_create.append(category)
                    sub_folders_to_create.append(subcategory)
                    destination_folder = os.path.join(path, category, subcategory, filename)
                    # print(f"The file {filename} falls in {subcategory} of category {category}")
                    return destination_folder
        else:
            if filename.lower().endswith(extensions):
                folders_to_create.append(category)
                destination_folder = os.path.join(path, category, filename)
                # print(f"The file {filename} falls in {category} category.")
                return destination_folder
    print(f"The {filename} doesn't fall in any category.")
    # destination_folder = os.path.join(path, 'Miscellaneous_Files')
    # return destination_folder
    return None


for file in chosen_files:
    result = categorize_file(file, file_extensions, path)
    print("$$$$$$$$$This says which file falls in which category$$$$$$")
    print(result)

# print(folders_to_create)
# print(sub_folders_to_create)


# folder is each folder created based on the existing files :
for folder in folders_to_create:
    full_path = os.path.join(path, folder)
    # print(full_path)
    try:
        os.makedirs(full_path, mode = 0o777)
        print(f"Directory created: {full_path}")
    except FileExistsError:
        print(f"Directory exists: {full_path}")
    except PermissionError:
        print(f"Permission denied : {full_path}")

    # if not os.path.exists(full_path):
    #     os.makedirs(full_path, mode=0o420)

#
# print("############# Creating folders in sub folder (Document_Files)##########")
for sub_folder in sub_folders_to_create:
    full_path = os.path.join(path, 'Document_Files', sub_folder)
    if not os.path.exists(full_path):
        os.makedirs(full_path)


# Move the files to the final destination  :
for file in chosen_files:
    destination_folder = categorize_file(file, file_extensions, path)
    source_file_path = os.path.join(path, file)
    if destination_folder:
        # destination_file_path = os.path.join(destination_folder)
        shutil.move(source_file_path, destination_folder)
        print(f"File {file} moved from {source_file_path} to {destination_folder}")
    else:
        miscellaneous_path = os.path.join(path, 'Miscellaneous_Files')
        shutil.move(source_file_path, miscellaneous_path)
        print(f"The {file} doesn't fall into any category.")


if not chosen_files:
    print("All files have been moved!")
else:
    print("There are some files remaining!")





