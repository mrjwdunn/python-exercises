import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from env import user, host, pw


def separator():
    print()
    print('--------------------------------------------------')
    print()


separator()

# Basic

# 1. Import pandas and numpy


# 2. Use the code below to generate a data frame for students
#
# Your data frame should include the student number, student name, shoe_size, and favorite number.
#
# Store your data frame in a variable named students
#
#     students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
#                 'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
#
#     student_number = list(range(1, len(students) + 1))
#     shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
#     side_of_classroom = np.random.choice(['left', 'right'], len(students))
#     favorite_number = np.random.randint(1, 11, len(students))

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

students_df = pd.DataFrame({'name': students,
                            's_number': student_number,
                            'shoe_size': shoe_sizes,
                            'classroom': side_of_classroom,
                            'f_number': favorite_number})

(students_df)

# 3. Print out the shape of the data frame.

students_df.shape

# 4. Print out the names of the columns in the data frame.

students_df.columns[:]

# 5. Rename 2 of the columns in your data frame.

students_df.rename(
    columns={'s_number': 'id', 'f_number': 'favorite_number', }, inplace=True)
students_df


# 6. Create a new data frame based on the one you have. The new data frame should only have columns for shoe size and side of the classroom.

students_df[['shoe_size', 'classroom']]

# 7. Create a new data frame that has all of the columns, but only 5 rows.

students_df.sample(5)

# 8. Create a new data frame that has only columns for favorite number and name, and only includes 7 rows.
# or students_df.sample(7)[['favorite_number', 'name']]

students_df[['favorite_number', 'name']].sample(7)

# 9. Create a new column for the ratio of shoe size to the favorite number. Name this ss_to_fn

students_df['ss_to_fn'] = students_df.shoe_size / students_df.favorite_number
students_df

# 10. Create a new column that contains the z-score for the shoe size.

students_df['z-score'] = (students_df.shoe_size -
                          students_df.shoe_size.mean()) / students_df.shoe_size.std()
students_df

# 11. Transform the side_of_the_classroom columns such that the values are either R or L.

students_df.classroom.apply(lambda side: side[0].upper())

# 12. Find the names of all the students that have a shoe size greater than the 3rd quartile of shoe sizes (You can use the .quantile method on a series for this)

students_df[students_df.shoe_size > students_df.shoe_size.quantile(0.75)]

# 13. Find the names of all the students that have a shoe size less than the 1st quartile of shoe sizes

students_df[students_df.shoe_size < students_df.shoe_size.quantile(0.25)]

separator()

# Aggregation & Plotting

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

students_df = pd.DataFrame({'name': students,
                            'id': student_number,
                            'shoe_size': shoe_sizes,
                            'classroom': side_of_classroom,
                            'favorite_number': favorite_number})
(students_df)

# 1. Calculate the mean, median, min, and max for the shoe sizes and favorite numbers

students_df.agg({'shoe_size': [np.mean, np.median, np.min, np.max], 'favorite_number': [
                np.mean, np.median, np.min, np.max]})


# 2. Sort the data frame by the students shoe size

students_df.sort_values(by='shoe_size', ascending=False)

# 3. Sort the data frame by the side of the classroom, then by their student number

students_df.sort_values(by=['classroom', 'id'])

# 4. Find the number of students on each side of the classroom

students_df.groupby('classroom').count()[['id']]

# 5. Find the average shoe size for each side of the classroom

students_df.groupby('classroom').mean()[['shoe_size']]

# 6. Find the maximum favorite number for each side of the classroom

students_df.groupby('classroom').max()[['favorite_number']]

# 7. Create a pie chart that visualizes the number of students on each side of the classroom.

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Right', 'Left'
sizes = students_df.groupby('classroom').count()[['id']]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Number of students on each side of the classrooms')
plt.show()

# 8. Create a histogram of the shoe sizes in the classroom

students_df.shoe_size.plot.hist()
plt.title('Shoe Sizes in the Classroom')

# 9. Create a histogram of the favorite numbers in the classroom

students_df.favorite_number.plot.hist()
plt.title('Favorite Numbers in the Classroom')

# 10. Create a scatter plot of shoe size vs favorite number

students_df.plot.scatter(x='shoe_size', y='favorite_number')
plt.title('Shoe Size vs Favorite Number')

separator()

# Reading & Writing Data

# 1. Save the students data to a csv file.

csv_string = students_df.to_csv(index=False)
csv_string

with open('students.csv', 'w') as f:
    f.write(csv_string)

# 2. Read the data from the csv file back into pandas. What do you notice?

panda_df = pd.read_csv('students.csv')
panda_df

# 3. Create a data frame based on the profiles.json file. Explore this data frame's structure

profiles_json_df = pd.read_json('profiles.json')
profiles_json_df

# 4. Write the code necessary to create a data frame based on the results of a SQL query to the numbers database.


def get_connection(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{pw}@{host}/numbers'
    return create_engine(url)


conn = get_connection('numbers', user, host, pw)

sql_number_df = pd.read_sql('SELECT * FROM numbers', conn)

sql_number_df
