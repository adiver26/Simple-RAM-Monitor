# Simple-RAM-Monitor
A simple tool to monitor available RAM space without having to open task manager using python with basic tkinter.

## Steps to run the file
* Clone this repository
* Install the psutil library using the command 
`pip install psutil`
  * If during installation you encounter a permission error, try using the `--user` flag or run the installation command in administrative mode.
* Run the file using the command `python ram.py`

## Steps to create an executable
For ease of access, you might want to create an executable of the program, so that you can run it directly instead of navigating to the folder and running the script everytime.
* Install the pyinstaller library using the command `pip install pyinstaller` 
  * If during installation you encounter a permission error, try using the `--user` flag or run the installation command in administrative mode.
* Navigate to the folder containing the python file, then open Command Prompt or any such tool
* Run the command `pyinstaller --onefile ram.py`
* After execution of the script, navigate to the newly created `dist` folder in the current directory. Here you will find the executable.
* Simply double click on the newly created `.exe` file to run the program

The program will show the percentage of available RAM in your system on a small window, along with the convenience to start or stop the scanning.
