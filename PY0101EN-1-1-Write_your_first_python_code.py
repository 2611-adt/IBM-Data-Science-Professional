#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 
# # Writing Your First Python Code
# 
# Estimated time needed: **25** minutes
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# *   Write basic code in Python
# *   Work with various types of data in Python
# *   Convert the data from one type to another
# *   Use expressions and variables to perform operations
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="https://#hello">Say "Hello" to the world in Python</a>
#             <ul>
#                 <li><a href="https://version/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">What version of Python are we using?</a></li>
#                 <li><a href="https://comments/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Writing comments in Python</a></li>
#                 <li><a href="https://errors/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Errors in Python</a></li>
#                 <li><a href="https://python_error/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Does Python know about your error before it runs your code?</a></li>
#                 <li><a href="https://exercise/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Exercise: Your First Program</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="https://#types_objects">Types of objects in Python</a>
#             <ul>
#                 <li><a href="https://int/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Integers</a></li>
#                 <li><a href="https://float/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Floats</a></li>
#                 <li><a href="https://convert/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Converting from one object type to a different object type</a></li>
#                 <li><a href="https://bool/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Boolean data type</a></li>
#                 <li><a href="https://exer_type/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Exercise: Types</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="https://#https://exp/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01ressions">Expressions and Variables</a>
#             <ul>
#                 <li><a href="exp">Expressions</a></li>
#                 <li><a href="https://exer_exp/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Exercise: Expressions</a></li>
#                 <li><a href="https://var/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Variables</a></li>
#                 <li><a href="https://exer_exp_var/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Exercise: Expression and Variables in Python</a></li>
#             </ul>
#         </li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>25 min</strong>
#     </p>
# </div>
# 
# <hr>
# 

# <h2 id="hello">Say "Hello" to the world in Python</h2>
# 

# When learning a new programming language, it is customary to start with an "hello world" example. As simple as it is, this one line of code will ensure that we know how to print a string in output and how to execute code within cells in a notebook.
# 

# <hr/>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# [Tip]: To execute the Python code in the code cell below, click on the cell to select it and press <kbd>Shift</kbd> + <kbd>Enter</kbd>.
# </div>
# <hr/>
# 

# In[1]:


# Try your first Python output

print('Hello, Python!')


# After executing the cell above, you should see that Python prints <code>Hello, Python!</code>. Congratulations on running your first Python code!
# 

# <hr/>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
#     [Tip:] <code>print()</code> is a function. You passed the string <code>'Hello, Python!'</code> as an argument to instruct Python on what to print.
# </div>
# <hr/>
# 

# <h3 id="version">What version of Python are we using?</h3>
# 

# <p>
#     There are two popular versions of the Python programming language in use today: Python 2 and Python 3. The Python community has decided to move on from Python 2 to Python 3, and many popular libraries have announced that they will no longer support Python 2.
# </p>
# <p>
#     Since Python 3 is the future, in this course we will be using it exclusively. How do we know that our notebook is executed by a Python 3 runtime? We can look in the top-right hand corner of this notebook and see "Python 3".
# </p>
# <p>
#     We can also ask Python directly and obtain a detailed answer. Try executing the following code:
# </p>
# 

# In[ ]:


# Check the Python Version

import sys
print(sys.version)


# <hr/>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
#     [Tip:] <code>sys</code> is a built-in module that contains many system-specific parameters and functions, including the Python version in use. Before using it, we must explictly <code>import</code> it.
# </div>
# <hr/>
# 

# <h3 id="comments">Writing comments in Python</h3>
# 

# <p>
#     In addition to writing code, note that it's always a good idea to add comments to your code. It will help others understand what you were trying to accomplish (the reason why you wrote a given snippet of code). Not only does this help <strong>other people</strong> understand your code, it can also serve as a reminder <strong>to you</strong> when you come back to it weeks or months later.</p>
# 
# <p>
#     To write comments in Python, use the number symbol <code>#</code> before writing your comment. When you run your code, Python will ignore everything past the <code>#</code> on a given line.
# </p>
# 

# In[16]:


# Practice on writing comments

print('Hello, Python!') # This line prints a string
# print('Hi')


# <p>
#     After executing the cell above, you should notice that <code>This line prints a string</code> did not appear in the output, because it was a comment (and thus ignored by Python).
# </p>
# <p>
#     The second line was also not executed because <code>print('Hi')</code> was preceded by the number sign (<code>#</code>) as well! Since this isn't an explanatory comment from the programmer, but an actual line of code, we might say that the programmer <em>commented out</em> that second line of code.
# </p>
# 

# <h3 id="errors">Errors in Python</h3>
# 

# <p>Everyone makes mistakes. For many types of mistakes, Python will tell you that you have made a mistake by giving you an error message. It is important to read error messages carefully to really understand where you made a mistake and how you may go about correcting it.</p>
# <p>For example, if you spell <code>print</code> as <code>frint</code>, Python will display an error message. Give it a try:</p>
# 

# In[15]:


# Print string as error message

frint("Hello, Python!")


# <p>The error message tells you: 
# <ol>
#     <li>where the error occurred (more useful in large notebook cells or scripts), and</li> 
#     <li>what kind of error it was (NameError)</li> 
# </ol>
# <p>Here, Python attempted to run the function <code>frint</code>, but could not determine what <code>frint</code> is since it's not a built-in function and it has not been previously defined by us either.</p>
# 

# <p>
#     You'll notice that if we make a different type of mistake, by forgetting to close the string, we'll obtain a different error (i.e., a <code>SyntaxError</code>). Try it below:
# </p>
# 

# In[14]:


# Try to see built-in error message

print("Hello, Python!)


# <h3 id="python_error">Does Python know about your error before it runs your code?</h3>
# 

# Python is what is called an <em>interpreted language</em>. Compiled languages examine your entire program at compile time, and are able to warn you about a whole class of errors prior to execution. In contrast, Python interprets your script line by line as it executes it. Python will stop executing the entire program when it encounters an error (unless the error is expected and handled by the programmer, a more advanced subject that we'll cover later on in this course).
# 

# Try to run the code in the cell below and see what happens:
# 

# In[13]:


# Print string and error to see the running order

print("This will be printed")
print("This will cause an error")
print("This will NOT be printed")


# <h3 id="exercise">Exercise: Your First Program</h3>
# 

# <p>Generations of programmers have started their coding careers by simply printing "Hello, world!". You will be following in their footsteps.</p>
# <p>In the code cell below, use the <code>print()</code> function to print out the phrase: <code>Hello, world!</code></p>
# 

# In[3]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
print("Hello, world!")


# <details><summary>Click here for the solution</summary>
# 
# ```python
# print("Hello, world!")
# 
# ```
# 
# </details>
# 

# <p>Now, let's enhance your code with a comment. In the code cell below, print out the phrase: <code>Hello, world!</code> and comment it with the phrase <code>Print the traditional hello world</code> all in one line of code.</p>
# 

# In[4]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
print("Hello, world!") #Print the traditional hello world 


# <details><summary>Click here for the solution</summary>
# 
# ```python
# print("Hello, world!") # Print the traditional hello world
# 
# ```
# 
# </details>
# 

# <hr>
# 

# <h2 id="types_objects" align="center">Types of objects in Python</h2>
# 

# <p>Python is an object-oriented language. There are many different types of objects in Python. Let's start with the most common object types: <i>strings</i>, <i>integers</i> and <i>floats</i>. Anytime you write words (text) in Python, you're using <i>character strings</i> (strings for short). The most common numbers, on the other hand, are <i>integers</i> (e.g. -1, 0, 100) and <i>floats</i>, which represent real numbers (e.g. 3.14, -42.0).</p>
# 

# <a align="center">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesObjects.png" width="600">
# </a>
# 

# <p>The following code cells contain some examples.</p>
# 

# In[11]:


# Integer

11


# In[10]:


# Float

2.14


# In[9]:


# String

"Hello, Python 101!"


# <p>You can get Python to tell you the type of an expression by using the built-in <code>type()</code> function. You'll notice that Python refers to integers as <code>int</code>, floats as <code>float</code>, and character strings as <code>str</code>.</p>
# 

# In[8]:


# Type of 12

type(12)


# In[7]:


# Type of 2.14

type(2.14)


# In[6]:


# Type of "Hello, Python 101!"

type("Hello, Python 101!")


# <p>In the code cell below, use the <code>type()</code> function to check the object type of <code>12.0</code>.
# 

# In[5]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(12.0)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# type(12.0)
# 
# ```
# 
# </details>
# 

# <h3 id="int">Integers</h3>
# 

# <p>Here are some examples of integers. Integers can be negative or positive numbers:</p>
# 

# <a align="center">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%201/images/TypesInt.png" width="600">
# </a>
# 

# <p>We can verify this is the case by using, you guessed it, the <code>type()</code> function:
# 

# In[17]:


# Print the type of -1

type(-1)


# In[18]:


# Print the type of 4

type(4)


# In[19]:


# Print the type of 0

type(0)


# <h3 id="float">Floats</h3> 
# 

# <p>Floats represent real numbers; they are a superset of integer numbers but also include "numbers with decimals". There are some limitations when it comes to machines representing real numbers, but floating point numbers are a good representation in most cases. You can learn more about the specifics of floats for your runtime environment, by checking the value of <code>sys.float_info</code>. This will also tell you what's the largest and smallest number that can be represented with them.</p>
# 
# <p>Once again, can test some examples with the <code>type()</code> function:
# 

# In[20]:


# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float


# In[21]:


# Print the type of 0.5

type(0.5)


# In[22]:


# Print the type of 0.56

type(0.56)


# In[23]:


# System settings about float type

sys.float_info


# <h3 id="convert">Converting from one object type to a different object type</h3>
# 

# <p>You can change the type of the object in Python; this is called typecasting. For example, you can convert an <i>integer</i> into a <i>float</i> (e.g. 2 to 2.0).</p>
# <p>Let's try it:</p>
# 

# In[24]:


# Verify that this is an integer

type(2)


# <h4>Converting integers to floats</h4>
# <p>Let's cast integer 2 to float:</p>
# 

# In[25]:


# Convert 2 to a float

float(2)


# In[26]:


# Convert integer 2 to a float and check its type

type(float(2))


# <p>When we convert an integer into a float, we don't really change the value (i.e., the significand) of the number. However, if we cast a float into an integer, we could potentially lose some information. For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):</p>
# 

# In[27]:


# Casting 1.1 to integer will result in loss of information

int(1.1)


# <h4>Converting from strings to integers or floats</h4>
# 

# <p>Sometimes, we can have a string that contains a number within it. If this is the case, we can cast that string that represents a number into an integer using <code>int()</code>:</p>
# 

# In[28]:


# Convert a string into an integer

int('1')


# <p>But if you try to do so with a string that is not a perfect match for a number, you'll get an error. Try the following:</p>
# 

# In[30]:


# Convert a string into an integer with error

int("1 or 2 people")


# <p>You can also convert strings containing floating point numbers into <i>float</i> objects:</p>
# 

# In[31]:


# Convert the string "1.2" into a float

float('1.2')


# <hr/>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
#     [Tip:] Note that strings can be represented with single quotes (<code>'1.2'</code>) or double quotes (<code>"1.2"</code>), but you can't mix both (e.g., <code>"1.2'</code>).
# </div>
# <hr/>
# 

# <h4>Converting numbers to strings</h4>
# 

# <p>If we can convert strings to numbers, it is only natural to assume that we can convert numbers to strings, right?</p>
# 

# In[32]:


# Convert an integer to a string

str(1)


# <p>And there is no reason why we shouldn't be able to make floats into strings as well:</p> 
# 

# In[33]:


# Convert a float to a string

str(1.2)


# <h3 id="bool">Boolean data type</h3>
# 

# <p><i>Boolean</i> is another important type in Python. An object of type <i>Boolean</i> can take on one of two values: <code>True</code> or <code>False</code>:</p>
# 

# In[34]:


# Value true

True


# <p>Notice that the value <code>True</code> has an uppercase "T". The same is true for <code>False</code> (i.e. you must use the uppercase "F").</p>
# 

# In[35]:


# Value false

False


# <p>When you ask Python to display the type of a boolean object it will show <code>bool</code> which stands for <i>boolean</i>:</p> 
# 

# In[36]:


# Type of True

type(True)


# In[37]:


# Type of False

type(False)


# <p>We can cast boolean objects to other data types. If we cast a boolean with a value of <code>True</code> to an integer or float we will get a one. If we cast a boolean with a value of <code>False</code> to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a <code>True</code>. And if we cast a 0 to a Boolean we will get a <code>False</code>. Let's give it a try:</p> 
# 

# In[38]:


# Convert True to int

int(True)


# In[39]:


# Convert 1 to boolean

bool(1)


# In[40]:


# Convert 0 to boolean

bool(0)


# In[41]:


# Convert True to float

float(True)


# <h3 id="exer_type">Exercise: Types</h3>
# 

# <p>What is the data type of the result of: <code>6 / 2</code>?</p>
# 

# In[42]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6/2)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# type(6/2) # float
# 
# ```
# 
# </details>
# 

# <p>What is the type of the result of: <code>6 // 2</code>? (Note the double slash <code>//</code>.)</p>
# 

# In[43]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6//2)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# type(6//2) # int, as the double slashes stand for integer division 
# 
# ```
# 
# </details>
# 

# <hr>
# 

# <h2 id="expressions">Expression and Variables</h2>
# 

# <h3 id="exp">Expressions</h3>
# 

# <p>Expressions in Python can include operations among compatible types (e.g., integers and floats). For example, basic arithmetic operations like adding multiple numbers:</p>
# 

# In[44]:


# Addition operation expression

43 + 60 + 16 + 41


# <p>We can perform subtraction operations using the minus operator. In this case the result is a negative number:</p>
# 

# In[45]:


# Subtraction operation expression

50 - 60


# <p>We can do multiplication using an asterisk:</p>
# 

# In[46]:


# Multiplication operation expression

5 * 5


# <p>We can also perform division with the forward slash:
# 

# In[47]:


# Division operation expression

25 / 5


# In[48]:


# Division operation expression

25 / 6


# <p>As seen in the quiz above, we can use the double slash for integer division, where the result is rounded down to the nearest integer:
# 

# In[49]:


# Integer division operation expression

25 // 5


# In[ ]:


# Integer division operation expression

25 // 6


# <h3 id="exer_exp">Exercise: Expression</h3>
# 

# <p>Let's write an expression that calculates how many hours there are in 160 minutes:
# 

# In[50]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
160/60


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 160/60 
# 
# # Or 
# 
# 160//60
# 
# ```
# 
# </details>
# 

# <p>Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the result of the multiplication (i.e., 120).
# 

# In[51]:


# Mathematical expression

30 + 2 * 60


# <p>And just like mathematics, expressions enclosed in parentheses have priority. So the following multiplies 32 by 60.
# 

# In[52]:


# Mathematical expression

(30 + 2) * 60


# <h3 id="var">Variables</h3>
# 

# <p>Just like with most programming languages, we can store values in <i>variables</i>, so we can use them later on. For example:</p>
# 

# In[53]:


# Store value into variable

x = 43 + 60 + 16 + 41


# <p>To see the value of <code>x</code> in a Notebook, we can simply place it on the last line of a cell:</p>
# 

# In[54]:


# Print out the value in variable

x


# <p>We can also perform operations on <code>x</code> and save the result to a new variable:</p>
# 

# In[55]:


# Use another variable to store the result of the operation between variable and value

y = x / 60
y


# <p>If we save a value to an existing variable, the new value will overwrite the previous value:</p>
# 

# In[56]:


# Overwrite variable with new value

x = x / 60
x


# <p>It's a good practice to use meaningful variable names, so you and others can read the code and understand it more easily:</p>
# 

# In[57]:


# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min


# In[58]:


# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours 
total_hours


# <p>In the cells above we added the length of three albums in minutes and stored it in <code>total_min</code>. We then divided it by 60 to calculate total length <code>total_hours</code> in hours. You can also do it all at once in a single expression, as long as you use parenthesis to add the albums length before you divide, as shown below.</p>
# 

# In[59]:


# Complicate expression

total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression
total_hours


# <p>If you'd rather have total hours as an integer, you can of course replace the floating point division with integer division (i.e., <code>//</code>).</p>
# 

# <h3 id="exer_exp_var">Exercise: Expression and Variables in Python</h3>
# 

# <p>What is the value of <code>x</code> where <code>x = 3 + 2 * 2</code></p>
# 

# In[60]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
x=3+2*2
print(x)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 7
# 
# ```
# 
# </details>
# 

# <p>What is the value of <code>y</code> where <code>y = (3 + 2) * 2</code>?</p>
# 

# In[61]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
y=(3+2)*2
print(y)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 10
# 
# ```
# 
# </details>
# 

# <p>What is the value of <code>z</code> where <code>z = x + y</code>?</p>
# 

# In[62]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
z=x+y
print(z)


# <details><summary>Click here for the solution</summary>
# 
# ```python
# 17
# 
# ```
# 
# </details>
# 

# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href="https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01" target="_blank">this article</a> to learn how to share your work.
# <hr>
# 

# ## Author
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01" target="_blank">Joseph Santarcangelo</a>
# 
# ## Other contributors
# 
# <a href="https://www.linkedin.com/in/jiahui-mavis-zhou-a4537814a?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01">Mavis Zhou</a>
# 
# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
# | ----------------- | ------- | ---------- | ---------------------------------- |
# | 2020-08-26        | 2.0     | Lavanya    | Moved lab to course repo in GitLab |
# |                   |         |            |                                    |
# |                   |         |            |                                    |
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
