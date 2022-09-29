import uos as os


def walk_directories(initial_directory="/"):
    if not initial_directory.startswith("/"):
        initial_directory = f"/{initial_directory}"
    directories = [initial_directory]
    paths = {}
    while directories:
        for directory in directories:
            new_directories, files = recursive_walk(directory)
            paths[directory] = files
            directories = new_directories
    return paths

def recursive_walk(initial_directory):
    files = []
    directories = []
    unprocessed_directory = os.ilistdir(initial_directory)
    if unprocessed_directory:
        for item in unprocessed_directory:
            if item[1] == 16384:
                if initial_directory == "/":
                    initial_directory = ""
                directories.append(f"{initial_directory}/{item[0]}")
            else:
                files.append(item[0])
    return (directories, files)

def unquote(string):
    bytes_string = string.encode("utf-8")
    split_byte_string = bytes_string.split(b'%')
    if len(split_byte_string) == 1:
        return bytes_string
    final_byte_string = [split_byte_string[0]]
    for split in split_byte_string[1:]:
        try:
            final_byte_string.append(bytes([int(split[:2], 16)]))
            final_byte_string.append(split[2:])
        except KeyError:
            final_byte_string.append(b'%')
            final_byte_string.append(split)
    return b"".join(final_byte_string)
