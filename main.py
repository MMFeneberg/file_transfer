import os
import shutil


def file_transfer():
    print("Hello World")
    if os.path.exists("Testing"):
        print("Folder Exists, Moving File")
        if os.path.exists("Source/file.txt"):
            shutil.move("Source/file.txt", "Testing")
    else:
        os.mkdir("Testing")


if __name__ == "__main__":
    file_transfer()
