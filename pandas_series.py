#Use pandas to create a Series named fruits from the following list:
import numpy as np
import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#Use Series attributes and methods to explore your fruits Series.

#Determine the number of elements in fruits.
fruits.size 

#Output only the index from fruits.
fruits.index

#Output only the values from fruits.
fruits.values

#Confirm the data type of the values in fruits.
fruits.dtype

#Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)
fruits.tail(5)
fruits.sample(2)

#Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()

#Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
#Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

#Determine the string value that occurs most frequently in fruits.
fruits.value_counts().head(1)
fruits.value_counts().idxmax()
fruits.value_counts().nlargest()
#Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest()
fruits.value_counts().idxmin()

#Explore more attributes and methods while you continue to work with the fruits Series.

#Capitalize all the string values in fruits.
fruits.str.capitalize() 

#Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')
sum(fruits.str.count('[a]'))

#Output the number of vowels in each and every string value.
fruits.str.count('aeiou')
fruits['Vowels'] = sum(fruits.str.count('[a-e]'))

#Write the code to get the longest string value from fruits.
max(fruits, key=len)
[fruits.str.len().argmax()] #This just return the index of the longest string

#Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len() >= 5]

#Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lambda fruit: fruit.count('o') >= 2)]

#Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

#Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

#Which string value contains the most vowels?
fruits[fruits.str.count('[aeiou]').max()]