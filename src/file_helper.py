import os


def search_files(path, extension):
    # search files dummy extension returns non empty list
    # search files json extension returns non empty list
    with os.scandir(path) as entries:
        files = [f.path for f in entries if f.name.endswith(extension)]
    return files


def read_data(files):
    # read data known filenames returns non empty list
    list_data = []
    for file in files:
        if os.path.exists(file):
            with open(file, 'r') as file_name:
                data = file_name.read()
                if data is not None:
                    list_data.append(data)
    return list_data


if __name__ == '__main__':
    result = search_files('../test_files', 'json')
    print(result)
