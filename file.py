def read_file(filepath):
    with open(filepath, "rb") as file:
        return file.read()
    
def write_file(filepath, data):
    with open(filepath, "wb") as file:
        return file.write(data.encode())