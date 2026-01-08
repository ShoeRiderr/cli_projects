import os
import shutil

"""
Organizes files in the given directory into subdirectories based on file extensions.

Args:
    path (str): The path to the directory to organize.
"""
def organize(path: str) -> None:
    if not os.path.isdir(path):
        print(f"The path {path} is not a valid directory.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            target_directory = os.path.join(path, file_extension)

            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            shutil.move(file_path, os.path.join(target_directory, filename))

    print(f"Files in {path} have been organized by extension.")


if __name__ == "__main__":
    directory_path = input("Enter the path of the directory to organize: ")
    organize(directory_path)