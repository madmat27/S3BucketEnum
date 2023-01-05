# S3BucketEnum

This is a tool developed for my thesis "Security in Cloud Systems". (Aristotle University of Thessaloniki - MSc in 
Communication Networks and Systems Security - Issue date: 2023)

## What's in this repo?
The tool that enumerates Amazon S3 Buckets to find whether they are private or public, for further exploitation. Repo 
also includes the 'requirements.txt' file which contains the module dependencies and should be imported for the tool to 
work properly. Last (but not least!) this README file, which contains detailed instructions for installation and usage.

## Should I install anything on my computer for this to work?
Well, the program is writen in python, so python is mandatory for the tool to work! You can find instructions how to 
install python in your pc (according to your operating system), so I will skip this part.
Please note that program is developed and tested in python --version 3.10.5, so use this version (or higher). 
Feel free to test it in lower versions, but might not work as expected. 

## How can I use this software?
It requires some actions prior to running this program. This is a step-by-step installation, so feel free to skip any 
part you already know.

### Download: 
Open a terminal, navigate to the folder that you want to save the file and run the following command: 
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
(Unix/Linux/MacOS): First need to change the file to executable with this command: 
```
chmod +x S3BucketEnum.py
```
Then in terminal run the following code 
>./S3BucketEnum.py <path-to-wordlist-file>: 

Example: 
```commandline
./S3BucketEnum.py /Users/mat/Desktop/names50.txt
```

(Windows): Execute with the following command:
Then in terminal run the following code 
>python3 S3BucketEnum.py <path-to-wordlist-file>: 

Example:
```commandline
python3 S3BucketEnum.py /Users/mat/Desktop/names50.txt
```

### Print help file:
```commandline
./S3BucketEnum.py -h
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