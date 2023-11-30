from typing import TextIO

def destroy_file(file: TextIO):
    file_contents = file.readlines()
    for i in range(len(file_contents)):
        x = file_contents[i]
        new_x = ""
        for z in range(len(x)):
            new_x += chr((ord(x[z]) + z - ord('a')) % 26 + ord('a'))
        file_contents[i] = new_x

    with open("destroyed_file.txt", "w") as f:
        f.writelines(file_contents)

destroy_file(open("file_question.txt", "r"))