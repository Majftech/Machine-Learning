"""
to find the common book ids in books_published_last_two_years.txt and all_coding_books.txt to obtain a list of recent coding books.
"""
import time
import pandas as pd
import numpy as np

"""
Inefficient method - Time taken will be more
"""
with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')   
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')
start = time.time()
recent_coding_books = []
for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))   


"""
better method - Use vector methods
"""
start = time.time()
recent_coding_books =  recent_coding_books = np.intersect1d(recent_books, coding_books)
# or, even this is correct
#recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
    
