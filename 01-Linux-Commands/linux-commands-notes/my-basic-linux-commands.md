# My Basics Linux Commands Notes

## 1. ls
**What it does:** Shows all files and folders in the current directory.

**Example:**  
ls -l  
(shows files with details like size, permissions, owner)

**Beginner mistake:**  
Thinking `ls` shows hidden files. It doesn’t — you must use `ls -a` for that.

## 2. cd
**What it does:** Used to move (change directory) into another folder.

**Example:**  
cd Documents  
(moves into the Documents folder)

**Beginner mistake:**  
Typing `cd ~` thinking it goes back to the previous folder.  
Actually `cd ~` goes to the HOME directory, not the last one.

## 3. pwd
**What it does:** Shows the full path of the folder you are currently in.

**Example:**  
pwd  
(/home/user/Documents)

**Beginner mistake:**  
Confusing `pwd` with `ls`.  
pwd shows **where you are**, not **what is inside** the folder.

## 4. mkdir
**What it does:** Creates a new folder.

**Example:**  
mkdir projects  
(creates a folder named “projects”)

**Beginner mistake:**  
Trying to create a folder where you don’t have permissions, which gives a “permission denied” error.

## 5. touch
**What it does:** Creates an empty file or updates the timestamp of an existing file.

**Example:**  
touch notes.txt  
(creates a file called notes.txt)

**Beginner mistake:**  
Thinking `touch` opens the file.  
It only creates it — you must use an editor like nano/vim to open.

## 6. rm
**What it does:** Deletes files (and with options, folders).

**Example:**  
rm file.txt  
(deletes file.txt)

**Beginner mistake:**  
Using `rm -r` without thinking.  
This permanently deletes entire folders — no recycle bin, no recovery.