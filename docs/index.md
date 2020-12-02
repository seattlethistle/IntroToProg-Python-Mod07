# MODULE 07: Files & Exceptions        
# ASSIGNMENT 07: Exception Handling & Pickling
 
## 1. Introduction 
This paper documents my learning from Module 7, the goal of which was to learn about creating scripts using custom functions, files and error handling.  We also learned about creating advanced GitHub web pages.   
  
I have demonstrated my learning by  
	• Being able to answer the questions provided in the Assignment  
	• Creating a script that performs this week's task - a demo of both Exception Handling and Pickling 
	• Running the script within both PyCharm and a command shell  
	• Posting my files on GitHub: https://github.com/seattlethistle/IntroToProg-Python-Mod07  
	• Adding a new GitHub web page to my repository: https://seattlethistle.github.io/IntroToProg-Python-Mod07/  
	• Post my GitHub link to the message board  
	• Peer reviewing another student's files in GitHub and adding my comments to their post  

## 2. Discussion  
Figure 1 displays my code in the file "Assignment07.py" in the PyCharm IDE.  
  
As the purpose of this assignment was to demonstrate understanding of 2 specific python features, I started by looking through previous examples to find code I had already written which I could modify.  I picked the answers from Assignment 03 and Assignment 05.   Assignment 03 collected user data to create a Home Inventory so I used this as my base.  I then added the menu selections from Assignment 05.  
  
I incorporated Pickling by modifying the functions to use pickle.load and pickle,dump for read and save, hence creating a binary .dat file instead of the usual csv style .txt file.  
  
I incorporated Exception Handling under menu item 2.  Since I defined the estimated value of the item to be a floating point number, I was able to insert a try/except block to catch anyone accidentally entering text.  This displays a user friendly error message and gives the user another chance to enter a number.  
  
Figure 2 displays the code after being ran in the PyCharm run window.  
  
Figure 3 displays the code being ran at the command prompt.  
  
Figure 4 displays the output file "HomeInventory.dat".  
  


### Figure 1: Script File in PyCharm  
  

### Figure 2: Script run window in PyCharm
  
  
### Figure 3: Script running from a Command Shell
  
  
### Figure 4: Output File











