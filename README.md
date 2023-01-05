# S3BucketEnum

This is a tool developed for my thesis "Security in Cloud Systems". (Aristotle University of Thessaloniki - MSc in 
Communication Networks and Systems Security - Issue date: 2023)

```commandline

CyberSec:S3BucketEnum mat$ source venv/bin/activate
(venv) CyberSec:S3BucketEnum mat$ ./S3BucketEnum.py /Users/mat/Desktop/names1000.txt 
                                                                                
   __________ ____             __        __  ______                             
  / ___/__  // __ )__  _______/ /_____  / /_/ ____/___  __  ______ ___          
  \__ \ /_ </ __  / / / / ___/ //_/ _ \/ __/ __/ / __ \/ / / / __ `__ \         
 ___/ /__/ / /_/ / /_/ / /__/ ,< /  __/ /_/ /___/ / / / /_/ / / / / / /         
/____/____/_____/\__,_/\___/_/|_|\___/\__/_____/_/ /_/\__,_/_/ /_/ /_/          
                                                                                
  AWS S3 Bucket Enumerator                                                      
  Mariana S. Mazi @madmat27                                                     
                                                                                
{'wlist': '/Users/mat/Desktop/names1000.txt'}
Loading…: 100%|████████████████████████| 1000/1000 [11:44<00:00,  1.42it/s]
+---------------------------------------+------------------------------------------+
|                  URL                  |                  STATUS                  |
+---------------------------------------+------------------------------------------+
|    https://aaron.s3.amazonaws.com/    |       Bucket exists and is private       |
|    https://abdul.s3.amazonaws.com/    |       Bucket exists and is private       |
|     https://abe.s3.amazonaws.com/     |       Bucket exists and is private       |
|     https://abel.s3.amazonaws.com/    |       Bucket exists and is private       |
|   https://abraham.s3.amazonaws.com/   |       Bucket exists and is private       |
|     https://adam.s3.amazonaws.com/    |       Bucket exists and is private       |
|     https://adan.s3.amazonaws.com/    |       Bucket exists and is private       |
|    https://adolfo.s3.amazonaws.com/   |       Bucket exists and is private       |
|    https://adolph.s3.amazonaws.com/   |          Bucket doesn't exist.           |
|    https://adrian.s3.amazonaws.com/   |       Bucket exists and is private       |
|   https://agustin.s3.amazonaws.com/   |       Bucket exists and is private       |
|    https://ahmad.s3.amazonaws.com/    |       Bucket exists and is private       |
|    https://ahmed.s3.amazonaws.com/    |       Bucket exists and is private       |
|      https://al.s3.amazonaws.com/     |      Bucket is public and listable!      |
|     https://alan.s3.amazonaws.com/    |       Bucket exists and is private       |
|    https://albert.s3.amazonaws.com/   |       Bucket exists and is private       |
|   https://alberto.s3.amazonaws.com/   | Bucket exist and all access is disabled. |

```

## What's in this repo?
The tool that enumerates Amazon S3 Buckets to find whether they are private or public, for further exploitation. Repo 
also includes the 'requirements.txt' file which contains the module dependencies and should be imported for the tool to 
work properly. Last (but not least!) this README file, which contains detailed instructions for installation and usage.

## Should I install anything on my computer for this to work?
Well, the program is writen in python, so python is mandatory! You can find instructions how to install python on your pc 
(according to your operating system), so I will skip this part.
Please note that program is developed and tested in python --version 3.10.5, so use this version (or higher). 
Feel free to test it in lower versions, but might not work as expected. 

## How can I use this software?
Some actions are required prior to running this program. This is a step-by-step installation, so feel free to skip any 
part you already know.

### Download: 
Open a terminal, navigate to the folder that you want to save the file and run the following command (git should be installed): 
```
git clone https://github.com/madmat27/S3BucketEnum.git
```

### Create virtual environment (venv) and install requirements:
Go to folder that contains the software (if you git-cloned it, then it's 'S3BucketEnum') and execute the following 
commands:
```commandline
cd S3BucketEnum
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Execute the program: 
(Linux/Unix/MacOS): First need to change the file to executable with this command: 
```
chmod +x S3BucketEnum.py
```
Then in terminal run the following code 
>./S3BucketEnum.py [path-to-wordlist-file]: 

Example: 
```commandline
./S3BucketEnum.py /Users/mat/Desktop/names50.txt
```

(Windows): Execute with the following command:
Then in terminal run the following code 
>python3 S3BucketEnum.py [path-to-wordlist-file]: 

Example:
```commandline
python3 S3BucketEnum.py C:\Users\mat\Desktop\names50.txt
```

### Print help file:
```commandline
user@ubuntu:$ ./S3BucketEnum.py -h (Linux/Unix/MacOS)
C:\ python3 S3BucketEnum.py -h (Windows)

```

```commandline
                                                                                
   __________ ____             __        __  ______                             
  / ___/__  // __ )__  _______/ /_____  / /_/ ____/___  __  ______ ___          
  \__ \ /_ </ __  / / / / ___/ //_/ _ \/ __/ __/ / __ \/ / / / __ `__ \         
 ___/ /__/ / /_/ / /_/ / /__/ ,< /  __/ /_/ /___/ / / / /_/ / / / / / /         
/____/____/_____/\__,_/\___/_/|_|\___/\__/_____/_/ /_/\__,_/_/ /_/ /_/          
                                                                                
  AWS S3 Bucket Enumerator                                                      
  Mariana S. Mazi @madmat27                                                     
                                                                                
usage: S3BucketEnum [-h] wlist

AWS S3 Bucket Enumerator

positional arguments:
  wlist       Specify a wordlist to be used to enumerate S3 buckets

options:
  -h, --help  show this help message and exit

Feel free to pass the code!

```

### Deactivate the virtual environment when finished (optional):
Run this command in your terminal:
```commandline
deactivate
```

## Can I use it?
This repository is free for anyone to use. All corrections and amendments are more than welcome! 

### Download thesis
For all Greek-speaking users, you can download thesis from here: 
[Security in Cloud Systems](https://ikee.lib.auth.gr/collection/Postgraduate%20Theses?ln=en)
