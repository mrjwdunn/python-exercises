
# coding: utf-8

# In[10]:


# Make sure this is first
# %matplotlib notebook

import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt # same as the top
print(plt)
import math


# ## 1. Write the Python code necessary to write your name with matplotlib lines

# In[11]:


plt.figure(figsize=(20, 10)) # (width, height)

""" All this code is for the lettter 'J' """
jx1 = [1.8,2.15] # Top of the J, starting point
jy1 = [4,4] # Top of the J, ending point
plt.plot(jx1, jy1, c='Blue')
jx2 = [2,2] # Middle line of the J, starting point
jy2 = [4,1] # Middle line of the J, ending point
plt.plot(jx2, jy2, c='Blue')
jx3 = [2,1.9] # Right half of the Bottom line, starting point
jy3 = [1,-1] # Right half of the Bottom line, ending point
plt.plot(jx3, jy3, c='Blue')
jx4 = [1.9,1.8] # Left half of the Bottom line, starting point
jy4 = [-1,1] # left half of the Bottom line, ending point
plt.plot(jx4, jy4, c='Blue')
         
""" All this code is for the lettter 'a' """
ax1 = [2, 2.05] # Left line of the A, starting point
ay1 = [-1,1] # Left line of the A, ending point
plt.plot(ax1, ay1, c='Blue')
ax2 = [2.05,2.1] # Right line of the A, starting point
ay2 = [1,-1] # Right line of the A, ending point
plt.plot(ax2, ay2, c='Blue')
ax3 = [2.025,2.075] # Middle line of A, starting point
ay3 = [0,0] # Middle line of A, ending point
plt.plot(ax3, ay3, c='Blue')

""" All this code is for the lettter 'y' """
ax1 = [2.15, 2.15] # Left line of the A, starting point
ay1 = [-1,0] # Left line of the A, ending point
plt.plot(ax1, ay1, c='Blue')
ax2 = [2.15,2.1] # Right line of the A, starting point
ay2 = [0,1] # Right line of the A, ending point
plt.plot(ax2, ay2, c='Blue')
ax3 = [2.15,2.2] # Middle line of A, starting point
ay3 = [0,1] # Middle line of A, ending point
plt.plot(ax3, ay3, c='Blue')


plt.show()


# ## 2. Use matplotlib to plot the following equation:
# 
# * y
# =
# x^2
# −
# x
# +
# 2
# 
# Add an anotation for the point 0, 0, the origin.

# In[12]:


x = range(-5, 6)
y = []
for n in x:
    y.append(n ** 2 - n + 2)
    
print(x)
print(y)


# In[13]:


x = list(range(-5, 6))
y = [n ** 2 - n + 2 for n in x]

plt.plot(x, y, ls=':')
plt.title('An Exponential Distribution, $y = x^2 - x + 2$')
plt.xlabel('$x$')
plt.ylabel('$x^2 - x + 2$')
plt.annotate('Intersection', xy=(0, 2), xytext=(0, 15),
             arrowprops={'facecolor': 'red'})
plt.text(.2,2, '(0,0)', fontsize=10)
plt.show()


# In[14]:


x = range(-6, 5)
y = [n ** 2 - n + 2 for n in x]

plt.plot(x, y)
plt.title('An Exponential Distribution, $y = x^2 - x + 2$')
plt.xlabel('$x$')
plt.ylabel('$x^2 - x + 2$')
plt.annotate('Intersection', xy=(0, 0), xytext=(0, 1000),
             arrowprops={'facecolor': 'red'})
plt.show()


# ## 3. Create and label 4 separate plots for the following equations (choose a range for x that makes sense):
# 
# * y
# =
# √
# x
# * y
# =
# x^
# 3
# * y
# =
# tan
# (
# x
# )
# * y
# =
# 2^
# x
# 
# You can use functions from the math module to help implement some of the equations above.

# In[15]:


x = list(range(1, 10))

"""
from math import sqrt, tan

x1 = range(0, 8)
x2 = range(-7, 8)
x3 = x1
x4 = x2

# y1 = sqrt x
y1 = []
for x in x1:
    y1.append(sqrt(x))

# y2 = x ^ 2
y2 = []
for x in x2:
    y2.append(x **2)

# y3 = []
for x in x3:
    y3.append(y = tan(x))

# y4 = []
for x in x4:
    y4.append(y = 2^x)

"""

y1 = [math.sqrt(n) for n in x]
plt.plot(x, y1)
plt.title('$y = √ x$')
plt.show()

y2 = [n ** 3 for n in x]
plt.plot(x, y2)
plt.title('$y = x^3$')
plt.show()

y3 = [math.tan(n) for n in x]
plt.plot(x, y3)
plt.title('$y = tan(x)$')
plt.show()

y4 = [2 ** n for n in x]
plt.plot(x, y4)
plt.title('$y = 2^x$')
plt.show()


# ## 4. Combine the figures you created in the last step into one large figure with 4 subplots.

# In[16]:


n_rows = 2
n_cols = 2

plt.figure(figsize=(12, 8))
x = list(range(1, 10))

y1 = [math.sqrt(n) for n in x]
plt.subplot(n_rows, n_cols, 1)
plt.plot(x, y1)
plt.title('$y = √ x$')
# plt.show()

y2 = [n ** 3 for n in x]
plt.subplot(n_rows, n_cols, 2)
plt.plot(x, y2)
plt.title('$y = x^3$')
# plt.show()

y3 = [math.tan(n) for n in x]
plt.subplot(n_rows, n_cols, 3)
plt.plot(x, y3)
plt.title('$y = tan(x)$')
# # plt.show()

y4 = [2 ** n for n in x]
plt.subplot(n_rows, n_cols, 4)
plt.plot(x, y4)
plt.title('$y = 2^x$')
plt.show()


# ## 5. Comine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend.

# In[17]:


x = list(range(1, 5))

y1 = [math.sqrt(n) for n in x]
y2 = [n ** 3 for n in x]
y3 = [math.tan(n) for n in x]
y4 = [2 ** n for n in x]

plt.figure(figsize=(12, 10)) # (width, height)

plt.scatter(x, y1, c='blue')
plt.scatter(x, y2, c='red')
plt.scatter(x, y3, c='orange')
plt.scatter(x, y4, c='green')

plt.plot(x, y1, c='blue', label='$y = √ x$')
plt.plot(x, y2, c='red', label='$y = x^3$')
plt.plot(x, y3, c='orange', label='$y = tan(x)$')
plt.plot(x, y4, c='green', label='$y = 2^x$')

plt.legend()
plt.title('Approximate X and Y curves')
plt.xlabel('$x$')

plt.show()

