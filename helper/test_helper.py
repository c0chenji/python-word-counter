class FileWriter:
    @staticmethod
    def write(file_path, content):
        with open(file_path, 'wb') as file:
            file.write(content)

class FileReader:
    @staticmethod
    def count_lines(file_path):
        with open(file_path, 'r') as _file:
            file_content_list = _file.readlines()
            print(file_content_list)
            return len(file_content_list)

def write_to_file(text,path):
    with open(path, "w") as h:
        h.write(text)