# To add a new cell, type ''
# To add a new markdown cell, type ''

from IPython import get_ipython


# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Python Text Basics Assessment
# 
# Welcome to your assessment! Complete the tasks described in bold below by typing the relevant code in the cells.<br>
# You can compare your answers to the Solutions notebook provided in this folder.

# ## f-Strings
# #### 1. Print an f-string that displays `NLP stands for Natural Language Processing` using the variables provided.


abbr = 'NLP'
full_text = 'Natural Language Processing'

# Enter your code here:


# ## Files
# #### 2. Create a file in the current working directory called `contacts.txt` by running the cell below:


get_ipython().run_cell_magic('writefile', 'contacts.txt', 'First_Name Last_Name, Title, Extension, Email')


# #### 3. Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.


# Write your code here:



    
# Run fields to see the contents of contacts.txt:
fields


# ## Working with PDF Files
# #### 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.


# Perform import


# Open the file as a binary object


# Use PyPDF2 to read the text of the file



# Get the text from page 2 (CHALLENGE: Do this in one step!)
page_two_text = 



# Close the file


# Print the contents of page_two_text
print(page_two_text)


# #### 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.
# 
# #### CHALLENGE: See if you can remove the word "AUTHORS:"


# Simple Solution:





# CHALLENGE Solution (re-run the %%writefile cell above to obtain an unmodified contacts.txt file):




# ## Regular Expressions
# #### 6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`.


import re

# Enter your regex pattern here. This may take several tries!
pattern = 

re.findall(pattern, page_two_text)


# ### Great job!

