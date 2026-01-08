This code organizes files in a given directory based on their file extensions.

## How to use it?
First, install a virtual environment for the Python project:
```
python3 -m venv
```
This will create a .venv directory in the project.
Next, activate the virtual environment by typing the following command in the terminal:
```
source /.venv/bin/activate
```
In the console, you should now see something like this:
```
(.venv) your_user_name@Mac file_organizer % 
```
This means the virtual environment is active.

Now you can run the script by typing:
```
python3 ./organize.py
```
The script will ask you to enter the path that you want to organize.

If the path does not exist, you will receive the following message:
```
The path your/invalid/path is not a valid directory.
```
If the path exists, the response will look like this:
```
Files in your/alid/path have been organized by extension.
```
Your files in the given directory will then be organized.
