Level 0:
It is the most basic level in the entire task. It informs the player about the working of the SSH function and basically informs us how to connect to a host using SSH.
The required steps were given to us by the instruction page and the info given below is used to login using SSH-
Host-bandit.labs.overthewire.org
Port-2220
Username-bandit0
Password-bandit0

Level 0-1:
We must find the password for logging in as the next user from the bandit0 shell. To do that, we must list the files in the directory. We must find a file named readme.
After doing so, we must read the password stored inside it. The 1s command is then used list all files in the directory. After finding the readme file, read the 
password using the cat command. Then we must use the password to login to the next level using SSH. 

Level 1-2:
We are told that the password for the next level is kept inside a file called -(hyphen).Once again we must find it using 1s command. Then we move onto reading the file
which is different from before as the cat command cannot be used due to it not being able to recognise -(hyphen) as a file name and instead considers it as a 
stdin/Stout. So, we must prefix the command with path ./ which helps to read the password  and after finding the password for bandit2, use it to get an SSH connection 
as bandit2.

Level 2-3:
Next, the password for the next level is stored in a file named spaces in this filename. Once again, to find it we use the 1s command. For reading the file the cat
command cannot be used because the file is named spaces in this filename and cat command considers space as null '/0'. So using cat command directly is useless.
Therefore we must write the name of the file in quotes, this allows us to read the password. After finding the password for the user 3 bandit3. We move onto using
it to get an SSH connection as bandit3.

Level 3-4:
The password for the next level is inside a directory named inhere. We find it using the 1s command. After going through the inhere directory, we use 1s command once
again because the file might be hidden, so we run the 1s command with -al parameter which lists every file including hidden one. This is how we find the .hidden
file. The file with a dot(.) before its name is a hidden file in Linux. We then use the cat command to read the password stored in the file. After finding the 
password for user bandit4, we use it to get an SSH connection as bandit 4.

Level 4-5:
For the next level the password is stored inside human-readable file. The 1s command is used to find it. After going through the inhere directory we run 1s command
again which will give us a group of files.  We then use the file command to get information about the files. We get to know that the file07 conatins ASCII text from
this. It is readable so, we use the cat command which gives us the password for the next level. We must then use it to get an SSH connection as bandit5.

Level 5-6:
The passoword for the next level in a directory named inhere. To find it we use the 1s command. After going through the inhere directory we run 1s command again which
gives us a group files. We must then find the file using the file size. Find command which contains the parameter of size for which we have to use 'c' to get the 
size in bytes. Using the find command, we get to know that the file2 has the password. After acquiring the password, we use it to get an SSH connection as bandit6.

Level 6-7:
We are then told that the password for the next level is somewhere on the server. Finding the file in a server is more complicated than simply using 1s. So our 
search is widened by using the find command. It is insinuated that the user of the file is bandit7 and it is part of the group bandit 6. This information is used
as parameters in the find command, along with the size too. After this, we have found the password file hidden on the server. We know that the bandit7.password
contains the credentials from the find command. We have then found the password for the next level which we use to get an SSH connection as bandit7.

Level 7-8:
We are then told that the password for the next level is stored in a file named data.txt and to find it we use the 1s command. It is then insinuated that the password
is written next to the word millionth in the data.txt file. So to find the password, we must first find millionth word. The grep command is used for finding millionth.
Using the (|)Unix pipe, we connect the standard output from the first command and we feed it as standard input to the second command. Here, cat is first used to read
the file. The data in the file is sent to grep command to be evaluated. From this we get the password for the next level which we use to get an SSH connection as
bandit8.

Level 8-9:
The password for the next level is kept in a file named data.txt. It is insinuated that the password is the only line of code that is not repeated and only occurs
once. We use the sort command to sort the text in the data.txt file. The file still contains many repeating statements. To remendy this, we use the uniq command to
print the statement that does not repeat. Multiple pipes are used to get a filtered result. We then obtain the password for the next level which we use to get an SSH
connection as bandit9.

Level 9-10:
We are then told that the password for the next level is in a file named data.txt. It is insinuated that the password is ensued by many '=' characters. Here, if the
cat command is used the screen would be filled with unreadable mesh. For a more clean and refined result we are going to use strings command which prints character 
sequences that are at least 4 characters long. Then to find the precise location of the password, we use grep which allows us to obtain the password for the next level. 
We use this to get an SSH connection as bandit10.