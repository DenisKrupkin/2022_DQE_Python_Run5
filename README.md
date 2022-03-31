# 2022_DQE_Python_Run5

PUBLICATIONS v.0.1
====================================

1. Introduction
2. Publications
3. Parameters
4. Interface
5. Input file format
6. Output file format

INTRODUCTION
=============
This command line application is a part of Python for DQE mentoring programm. Application creates publications ot three types 
News, Advertisement, Arcticle manually or loads from file with special format and writes to output file in special format.
User can change files for loading, use default file or enter any count of publication directly via applicaation. 
All publications are stored in output file.

PUBLICATIONS
=============
There are three types of publications supported in v.0.1
- News
  Contains:
    - Publication text
    - City 
    - Date\time of publishing
- Advertisement
  Contains:
    - Publication text
    - Actual until date (expiration date)
    - Count of days before publication expired
- Article
  Contains:
    - Publication text
    - Text author name
    - Count of symbols is article

PARAMETERS
==========
Publications app should be started with two parameters:
- --default_path path to file
  This parameter stores path to file in special format (see 4.Input file format). 
  Publications will be parsed from this file as batch of lines. Parameter used if user selected the corresponding option (see 3. Interface)
  Example:
  "--default_path C:\Python\2022_DQE_Python_Run5\Files\example_file.txt"
- --target_file_path path to file
  This parameter stores path to file where all publications will be stored after publishing via app.
  Example:
  "--target_file_path C:\Python\2022_DQE_Python_Run5\Files\News_file.txt"
  Application can be started without one of these parameters or both. 
  But it is recommended to strart with both parametres to avoid any errors.
  Example:
  ```C:\Python\2022_DQE_Python_Run5\venv\Scripts\python.exe C:/Python/2022_DQE_Python_Run5/Files/files_home_task.py --default_path               C:\Python\2022_DQE_Python_Run5\Files\example_file.txt --target_file_path C:\Python\2022_DQE_Python_Run5\Files\News_file.txt```
  
INTERFACE
==========
At the start applications asks to select between two modes:
"Please choose input format (1-2): 1. One record 2. Many records (load from file)"
  - "One record." mode.
  This mode allows to enter publications manually step by step according to publication type.
    - If one record mode selected. Applications asks to select publication type:
  "Please choose publication type (1-3): 1. News 2. Advertisement 3. Article"
  After selection of publications type application will ask to enter all publication data step by step according to publication type (see 2. Publications) and write  publication to file specified in --target_file_path(see 3. Parameters)
    - If publication was published successfully then following message will appear:
      "The publication was published successfully."
    - After publishing of publication applications will ask:
    "Do you want to add more publications? Type "Yes" or "No":"
  User may answer "Yes" to continue and start all process again or "No" to exit from app.
  Only answers "Yes" and "No" are allowed.
  
  - Many records (load from file)
  This mode allows to load several publications as batch from default path or from file with manually specified path.
    - After selecting this mode application will ask:
      "Please choose using default file path or custom one (1-2): 1. Default 2. Custom"
    - If "1. Default" option seleted then application will load publications as batch from path specified in --default-path(see 3. Parameters) parameter and write to         file specified in --target_file_path(see 3. Parameters)
      - After finishing of publication process count of publications will appear:
        "<number> publications were published."
        and will ask:
        "Do you want to add more publications? Type "Yes" or "No":"
  
    - If "2. Custom" option selected the application will ask to enter path to file with publications:
      "Please enter path to file with publications:"
    - After will load publications as batch from path specified in --default-path(see 3. Parameters) parameter and write to         file specified in --                     target_file_path(see 3. Parameters)
      - After finishing of publication process count of publications will appear:
        "<number> publications were published."
        and will ask:
        "Do you want to add more publications? Type "Yes" or "No":"

INPUT FILE FORMAT
==================
The special source file format is used for batch loading of publications.
Rules:
- One line in file it is one publication.
- Each publication property ends with ';'
- All properties in double quotes.
- Line starts with publication type:
  "News" or "Advertisement" or "Article"
- Each line ends with './n'
- Following order of properties should be used:
  "Publication type";"publication text";"city or expiration date or author". (third property depends of publication type (see 2. Publications))
- Empty string at the end of file.

Example of file in special format:
```
"News"; "first_news."; "tvr1".
"Advertisement"; "first_adv"; "2022-03-25".
"Article"; "first_arc"; "Fergus1".
empty string
```

OUTPUT FILE FORMAT
==================
The publications are published in the target file in the following format:
```
News -------------------------
First_news.
tvr1, 2022-03-30 22:47:29
------------------------------

Private Ad -------------------
First_adv.
Actual until: 2022-03-25, -5 days left
------------------------------

Article ----------------------
First_arc.
Text author: Fergus1. Symbols count: 8.
------------------------------ 
```
This format is incompatible for loading to application.
