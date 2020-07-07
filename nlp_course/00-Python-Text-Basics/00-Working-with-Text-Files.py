# To add a new cell, type ''
# To add a new markdown cell, type ' '
   

name = 'Fred'

# Using the old .format() method:
print('His name is {var}.'.format(var=name))

# Using f-strings:
print(f'His name is {name}.')

 
# Pass `!r` to get the <strong>string representation</strong>:


print(f'His name is {name!r}')

 
# Be careful not to let quotation marks in the replacement fields conflict with the quoting used in the outer string:


d = {'a':123,'b':456}

print(f'Address: {d['a']} Main Street')

 
# Instead, use different styles of quotation marks:


d = {'a':123,'b':456}

print(f"Address: {d['a']} Main Street")

 
# ### Minimum Widths, Alignment and Padding
# You can pass arguments inside a nested set of curly braces to set a minimum width for the field, the alignment and even padding characters.


library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]

for book in library:
    print(f'{book[0]:{10}} {book[1]:{8}} {book[2]:{7}}')

 
# Here the first three lines align, except `Pages` follows a default left-alignment while numbers are right-aligned. Also, the fourth line's page number is pushed to the right as `Mythology` exceeds the minimum field width of `8`. When setting minimum field widths make sure to take the longest item into account.
# 
# To set the alignment, use the character `<` for left-align,  `^` for center, `>` for right.<br>
# To set padding, precede the alignment character with the padding character (`-` and `.` are common choices).
# 
# Let's make some adjustments:


for book in library:
    print(f'{book[0]:{10}} {book[1]:{10}} {book[2]:.>{7}}') # here .> was added

 
# ### Date Formatting


from datetime import datetime

today = datetime(year=2018, month=1, day=27)

print(f'{today:%B %d, %Y}')

 
# For more info on formatted string literals visit https://docs.python.org/3/reference/lexical_analysis.html#f-strings
# 
# ***
 
# # Files
# 
# Python uses file objects to interact with external files on your computer. 
# These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available. (We will cover downloading modules later on in the course).
# 
# Python has a built-in open function that allows us to open and play with basic file types. First we will need a file though. We're going to use some IPython magic to create a text file!
# 
# ## Creating a File with IPython
# #### This function is specific to jupyter notebooks! Alternatively, quickly create a simple .txt file with Sublime text editor.


#get_ipython().run_cell_magic('writefile', 'test.txt', 'Hello, this is a quick test file.\nThis is the second line of the file.')

 
# ## Python Opening a File
# 
# ### Know Your File's Location
# 
# It's easy to get an error on this step:


myfile = open('whoops.txt')

 
# To avoid this error, make sure your .txt file is saved in the same location as your notebook. To check your notebook location, use **pwd**:


pwd

 
# **Alternatively, to grab files from any location on your computer, simply pass in the entire file path. **
# 
# For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
# 
#     myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
# 
# For MacOS and Linux you use slashes in the opposite direction:
# 
#     myfile = open("/Users/YourUserName/Folder/myfile.txt")


# Open the text.txt file we created earlier
my_file = open('test.txt')



my_file

 
# `my_file` is now an open file object held in memory. We'll perform some reading and writing exercises, and then we have to close the file to free up memory.
# 
# ### .read() and .seek()


# We can now read the file
my_file.read()



# But what happens if we try to read it again?
my_file.read()

 
# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:


# Seek to the start of file (index 0)
my_file.seek(0)



# Now read again
my_file.read()

 
# ### .readlines()
# You can read a file line by line using the readlines method. Use caution with large files, since everything will be held in memory. We will learn how to iterate over large files later in the course.


# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()

 
# When you have finished using a file, it is always good practice to close it.


my_file.close()

 
# ## Writing to a File
# 
# By default, the `open()` function will only allow us to read the file. We need to pass the argument `'w'` to write over the file. For example:


# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')

 
# <div class="alert alert-danger" style="margin: 20px">**Use caution!**<br>
# Opening a file with 'w' or 'w+' *truncates the original*, meaning that anything that was in the original file **is deleted**!</div>


# Write to the file
my_file.write('This is a new first line')



# Read the file
my_file.seek(0)
my_file.read()



my_file.close()  # always do this when you're done with a file

 
# ## Appending to a File
# Passing the argument `'a'` opens the file and puts the pointer at the end, so anything written is appended. Like `'w+'`, `'a+'` lets us read and write to a file. If the file does not exist, one will be created.


my_file = open('test.txt','a+')
my_file.write('\nThis line is being appended to test.txt')
my_file.write('\nAnd another line here.')



my_file.seek(0)
print(my_file.read())



my_file.close()

 
# ### Appending with `%%writefile`
# Jupyter notebook users can do the same thing using IPython cell magic:


#get_ipython().run_cell_magic('writefile', '-a test.txt', '\nThis is more text being appended to test.txt\nAnd another line here.')

 
# Add a blank space if you want the first line to begin on its own line, as Jupyter won't recognize escape sequences like `\n`
 
# ## Aliases and Context Managers
# You can assign temporary variable names as aliases, and manage the opening and closing of files automatically using a context manager:


with open('test.txt','r') as txt:
    first_line = txt.readlines()[0]
    
print(first_line)

 
# Note that the `with ... as ...:` context manager automatically closed `test.txt` after assigning the first line of text to first_line:


txt.read()

 
# ## Iterating through a File


with open('test.txt','r') as txt:
    for line in txt:
        print(line, end='')  # the end='' argument removes extra linebreaks

 
# Great! Now you should be familiar with formatted string literals and working with text files.
# ## Next up: Working with PDF Text

