
#! to know the present path : pwd (present working directory)

#! who is login : whoami

#! To check system date and time : date, to check only date : date +%D, for only time : date +%T, to customize datetime : date +%D/%T or date +%D:%T or date +%D-%H:%M:%S

#!display files and directory in current location :  ls 
#! check the details of this files and folders : ls -lt --> using this we get latest file first and using ls -ltr get latest file at the last \
#! also want to see the size of file in human readable format then use : ls -lh
# -rw-rw-r-- 1 bharat bharat  27353 Jan 29 14:48 app.py     : start with -rw suggest is file
# drwxrwxr-x 2 bharat bharat   4096 Jan  9 16:33 pkl_files  : start with drwx suggest is folder 

#! to clear linux terminal : clear or ctrl+l

#! how to read or display content of file: cat filename

#! how to read file and search for word : less filename --> for search word : /name of word , possible that more than one word can present in file : use n for next word.
#! --> first line of file to last line direct reach : shift + g, and search bottom to up direction: ? name of word,
#! from bottom line to first line : p and if you want to close file :q 

#! page wise move downward in file : more file_name , use down arrow for go down direction, up arrow for upward direction.

#! to create new file : touch filename Note: this will create empty file , if you want to write something inside file : vim file_name then use i for write inside file or use nano file_name
#! --> vim file_name: directly you can go inside new file and then use : i for insert 
#! --> nano file_name: directly you can go inside new file

#! to delete file in linux : rm file_name 

#! to delete folder : rm -rf folder_name, rmdir folder_name

#! create directory : mkdir folder_name

#! change directory or move to the other folder : cd (change directory)

#! to move one folder back : cd .. , to move two folder back cd ../..

#! how to copy and past file from one folder to another folder : cp file_name destination_path ex. cp mini.csv (dest_path absolute or relative path)

#! copy file which is available in folder which is one location back: cp ../ file_name . # current location

#! copy content of one file to another file : cp mini.csv mini_new.csv

#!cut and past file from one location to another : mv file_name (desti/path: absolute or relative path)

#! rename file : mv file_name new_file_name

#! see the top 5 or num of lines instead of whole content: head -5 file_name

#! bottom 5 or num of lines : tail -5 file_name

#! how to sort the content of file : sort file_name , for reverse sorting : sort -r file_name

#! get unique content from file : sort file_name | uniq  (hete | used for multiple command run at time )

#! split file into number of file based on line of content : split -l 3 file_name 
# ex. have file mine.py has 10 lines of code now i want to make 3 files and each file contain 3 lines 
# use: split -l 3 mine.py , here -l is line  3 is number of line , total 4 file generate 

#! search word and display matching content from file : grep "word" file_name

#! for multiple word at time searching: egrep ann|kor file_name

#! use of wildcards * [], {} : 
# if folder contains so many files that time find perticular file is time taking for that use : 
# ex.1 file name start with test : ls test* , file end with .csv : ls *.csv
# ex.2 if you want to make 10 files : touch file{1..10} , 10 empty file will be created 

#! shuffle the content of file: shuf file_name

#! count number of lines in file : wc -l file_name

#! to check two files are identical or not : cmp file_1 file_2

#! to see how to compare and what is difference between two file : diff -u file1 file2 | diff file1 file2 

#! how to find the file : find path -name file_name
# ex. i am in root location using cd / , now in current folder i want to identify app.py available in which folders : find . app.py , to find in perticular folder then use : find AI_Chatbot -name app.py
# we can also use wildcards : find . --name *.csv 

#Note : locate is also used to find files but if available in updatedb if you have created then new file and 
#now you search for file then without "sudo updatedb" not able to find file 
#! find path from updatedb database : locate filename 

#! display previously used command : history, history | grep ps*

#! check process id(PID) of file : ps aux | grep filename , ps aux | grep filename *

#! to get more information about command ex ls -- help , ls --help | more
#! to know about the command : man command_name ex man ls

#! how to use calculator : bc 

#! to see the calendar : cal , cal JAN 2020, cal 2020

#! since when server is up and how many user log in : uptime

#! to record script : script command --> now which command you write on server with output store in typescript , to exit typescript file : ctrl+D

#! zip file but original file should be present : gzip -k file_name (k means keep the original)

#! unzip the file : gzip -d file_name (d means decompress) or gunzip file_name(gunzip means g un zip)

#! compress folder : tar -czf compress.tar.gz folder_name/  (tar : tap archive, -czf compress zip file, compress.tar.gz is file not folder)

#! decompress folder : tar -xzf compress.tar.gz (compress.tar.gz : file name)

#! zip multiple file in single zip file : zip myfiles.zip file1 file2 

#! unzip this file : unzip myfiles.zip

#! to know number files and details of that in zip file : unzip -l myfiles.zip (here unzip is not happening only get the information of files available in myfiles.zip)

#! download file or package from internet : wget url_of_file , if you want to give name of file  wget -O file_name url_of_file

#! call the api in linux : curl api

#! to install application on linux : for Ubantu : apt , REDHAT(Fedora/CentOS) : yum/dnf , ex yum iinstall nginx, we can install nay like python, postgres, java, etc

#! to check application is installed or not: rpm -qa | grep app
#! to get list of all the application installed in linux: dnf list installed, dnf list installed | grep python 

#! how to list available package or app to install : apt search package_name, Redhat : yum/dnf list available,  yum/dnf list available | grep package_name

#! start or stop the service on linux : systemctl start/stop service_name (firewall, nginx,)

#! status of service ; systemctl status service_name

#! list all the service on linux :  systemctl list-units --type=service --all

#! to list existing environment variable: printenv

#! how to add  new environment variable in linux temporary : export JAVA_HOME = "usr/lib/jvm/java_v" export PATH=$JAVA_HOME/bin:$PATH
#! TO ADD ENVIRONMENT VARIABLE PERMANET :  add that variable in bashrc file (bashrc file is user specific file)
# do ls -la --> find .bashrc --> vi .bashrc --> add new variable ex testvar = 'abcd', now check this environment variable generate or not : printenv | grep testvar
# testvar is not added till , need to do one thing --> source .bashrc --> printenv | grep testvar --> now appear. this is permanent changes

#! print only perticular column from csv file : awk -F ,'{print$2}' file_name.csv  (print$2 : print 2nd column, ',' :csv file is comma seperated, -F field), for multiple column '{print $1,$2}', to get last column : '{print $NF}'

#! display starting 2 char of all line : cut -c1-2 file_name, starting 2 to 5 : cut -c2-5 file_name

#! display specific line from file: sed -n '5p' file_name (print 5th line).

#! replace word with otherword : sed 's/business/finance/g file_name (s:substitute, g: globally).