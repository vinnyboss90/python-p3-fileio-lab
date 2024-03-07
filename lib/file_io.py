def write_file(file_name, file_content):
    t = open(str(file_name) + '.txt', 'w')
    t.write(file_content)

def append_file(file_name, append_content):
    t = open(str(file_name) + '.txt', 'a')
    t.write(append_content)

def read_file(file_name):
    t = open(str(file_name) + '.txt', 'r')
    content = t.read()
    return content