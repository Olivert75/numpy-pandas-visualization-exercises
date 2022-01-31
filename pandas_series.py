#Use pandas to create a Series named fruits from the following list:
from turtle import title
import matplotlib.pyplot as plt
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
fruits.value_counts().nlargest(n = 1, keep = 'all')

#Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n = 1, keep = 'all')
fruits.value_counts().idxmin()



#Explore more attributes and methods while you continue to work with the fruits Series.

#Capitalize all the string values in fruits.
fruits.str.capitalize() 

#Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')
sum(fruits.str.count('[a]'))

#Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]')
sum(fruits.str.count('[aeiou]'))
#This is for testing
sum(fruits.str.count('[a-z]'))

#Write the code to get the longest string value from fruits.
max(fruits, key=len)
[fruits.str.len().argmax()] #This just return the index of the longest string
fruits[fruits.str.len().idxmax()]

#Write the code to get the string values with 5 or more letters in the name.
fruits[fruits.str.len()>= 5]

#Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lambda i: i.count('o') >= 2)]

#Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

#Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

#Which string value contains the most vowels?
fruits[fruits.str.count('[aeiou]').max()]


words = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
letters = pd.Series(list(words))

#Which letter occurs the most frequently in the letters Series?
letters.value_counts() #give me the count of each letter
letters.value_counts().nlargest(n=1, keep='all')

#Which letter occurs the Least frequently?
letters.value_counts().nsmallest(n=1, keep='all')

#How many vowels are in the Series?
sum(letters.str.count('[aeiou]'))
#or give it a variable name and then call the variable
vowel_counts = letters.str.count('[aeiou]').sum()
vowel_counts

#How many consonants are in the Series?
sum(letters.str.count('[a-z]')) - sum(letters.str.count('[aeiou]'))

#Create a Series that has all of the same letters but uppercased.
letters.str.upper()

#Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters.value_counts().head(6).plot.bar(title = "Commonly occuring letters", edgecolor = 'black', color = 'red', width = .8).set(xlabel='Letter', ylabel='Frequency')

#Use pandas to create a Series named numbers from the following list:

numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

#What is the data type of the numbers Series?
numbers.dtype

#How many elements are in the number Series?
numbers.size

#Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
convert_num = numbers.str.replace('$', '').str.replace(',','').astype('float')
convert_num

#Run the code to discover the maximum value from the Series.
convert_num.max()

#Run the code to discover the minimum value from the Series.
convert_num.min()

#What is the range of the values in the Series?
convert_num.max() - convert_num.min()

#Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
pd.cut(convert_num, 4).value_counts()
#or
convert_num.value_counts(bins = 4)

#Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
convert_num.value_counts(bins = 4).sort_index(ascending= False).plot(kind ='barh', color = 'blue')
plt.title('4 bins')
plt.xlabel('Counts')
plt.ylabel('US Dollars')
plt.show()

#Use pandas to create a Series named exam_scores from the following list:
num = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#How many elements are in the exam_scores Series?
num.size

#Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
num.max()
num.min()
num.mean()
num.median() #or np.median(num) 
#Short Cut
num.describe()

#Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
num.value_counts().sort_index().plot(kind = 'bar', color = 'red', title = 'Exam Score', xlabel ='Scores', ylabel ='Counts')

#Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
eq = 100 - num.max()
curved_grades = num + eq
curved_grades

#Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
bin_edges = [0,70,75,80,90,101]
bin_labels = ['F','D','C','B','A']
letter_grades = pd.cut(curved_grades, bins = bin_edges, labels = bin_labels)
letter_grades.value_counts()

#Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades.value_counts().sort_index().plot(kind = 'bar', color ='blue', grid = True, title = 'Numbers of letter grade')
#plt.title = ('Letter Grade')
#plt.grid(True, ls='-')
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.xlabel('Letters Grade')
plt.ylabel('Counts')
plt.show()