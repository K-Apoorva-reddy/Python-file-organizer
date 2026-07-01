📂 Automated File Organization System

A Python-based application that automatically organizes files into categorized folders based on their file extensions. This project was developed as Task 1 of my Python Internship.

Project Overview

Managing files manually can be time-consuming when a folder contains many different file types. This application automates the process by scanning a selected directory and moving files into appropriate folders such as Images, Documents, Videos, Audio, Archives, and Others.


Features

- Automatically scans a selected folder
- Organizes files based on their extensions
- Creates folders automatically if they do not exist
- Maintains a log of organized files
- Simple command-line interface
- Easy to customize with additional file types


Technologies Used

- Python 3.x
- os Module
- shutil Module


 Project Structure

```
Automated_File_Organization_System/
│
├── main.py
├── organizer_log.txt
├── README.md
└── Sample_Files/
```


▶️ How to Run

 Clone the Repository

```bash
git clone https://github.com/K-Apoorva-reddy/Python-file-organizer.git
```

Navigate to Project

```bash
cd Python-file-organizer
```

Run the Application

```bash
python main.py
```

Enter the folder path when prompted.


Sample Output

```
Enter folder path:
(Screenshots/output.png)

Organization Completed Successfully!
Total Files Organized: 25

Learning Outcomes:

- File Handling in Python
- Directory Management
- Working with os module
- Using shutil for file operations
- Exception Handling
- Logging Concepts
- Command Line Applications


Future Enhancements:

- Graphical User Interface (GUI)
- Undo Organization Feature
- Duplicate File Detection
- Custom Category Support
- Scheduled Automatic Organization.
