import pandas as pd
import matplotlib.pyplot as plot
import re
import sys

file = 'translations.csv'
data = pd.read_csv(file, delimiter=';', encoding = 'utf-8')
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 180)

files = data['done'].tolist()
data = data.set_index('done')
file_sizes = []

def no_new_files():
    print("There are no new files to analyze")
    print("\n")
    print("*     " * 5)
    print("Program has finished its work")
    sys.exit()
    
if len(files) == 0:
    no_new_files()

page_price = int(input("Insert translation price per page: "))
characters_to_delete = input("Insert characters to delete without spaces inbetween") + ('\n')

number_of_pages = []

def analyze_file(file):

    content = open(file, encoding = "UTF-8")
    content_all = content.read()
    content_without_numbers = content_all.translate({ord(i): None for i in characters_to_delete})
    content_without_numbers = re.sub(' +', ' ', content_without_numbers)
    file_sizes.append(len(content_without_numbers))   
    
for text in files:
    analyze_file(text)

data['size'] = file_sizes
number_of_pages = []

for i in file_sizes:
    number_of_pages.append(round(i/1800, 2))

data['number of pages'] = number_of_pages
price = []

for i in number_of_pages:
    price.append(round(i * page_price, 2))

data['price'] = price

translation_sizes = pd.Series(data["size"], index = files)
translation_sizes.plot.bar(title = "Translation volume")
#plot.show()

def write_to_file(file):
    new_file = file.strip('.csv') + '_report.csv'
    data.to_csv(new_file, sep =';', encoding='utf-8')

#write_to_file(file)
print(data)
print("\nAll translations are processed")
no_new_files()
