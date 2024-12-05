
import sys
sys.path.append('../')
from utils import reader
import re
import numpy as np

#Get Input
data = reader.read_input('./input.txt')
lines = data.split('\n')

#Part 1
###Search Functions###
def search_line(line,term):
    return len(re.findall(term, line))

#search left right
def search(arr, term='XMAS'):
    total=0
    for i in range(arr.shape[0]):
        t_line = ''.join(line for line in arr[i,:])
        total+=search_line(t_line,term)
    return total

# Search diagonals
def diagonal_search(arr, term='XMAS'):
    total = 0
    for i in range(-1*arr.shape[0]+1,arr.shape[0]):
        diag = arr.diagonal(i)
        d_line=''.join(line for line in diag)
        total+=search_line(d_line,term)
    return total


#Create Array from input
word_search = []
for line in lines:
    new_line = [letter for letter in line]
    word_search.append(new_line)

#Setup Various Array Orientations for Searching
xmas_arr = np.array(word_search)
xmas_arr_fliplr = np.fliplr(xmas_arr)
transpose_arr = xmas_arr.T
transpose_fliplr = np.fliplr(transpose_arr)

total_matches = 0
#Search Left/Right
total_matches+= search(xmas_arr)
total_matches+= search(xmas_arr, term='SAMX')
#earch Up/Down
total_matches+= search(transpose_arr)
total_matches+= search(transpose_arr, term='SAMX')
#search First Diagonal
total_matches+= diagonal_search(xmas_arr)
total_matches+= diagonal_search(xmas_arr,term='SAMX')
#Search Second Diagonal
total_matches+= diagonal_search(np.fliplr(transpose_arr))
total_matches+= diagonal_search(np.fliplr(transpose_arr), term='SAMX')

print(total_matches)

#Part 2
sam = ['S','A','M']
mas = ['M','A','S']

total_matches=0
for i in range(xmas_arr.shape[0]-2):
  for j in range(xmas_arr.shape[1]-2):
    window = xmas_arr[i:i+3,j:j+3]
    diag = window.diagonal()
    diag_t = np.fliplr(window.T).diagonal()
    if (np.array_equal(diag, sam) and (np.array_equal(diag_t, sam) or (np.array_equal(diag_t, mas)))) or (np.array_equal(diag,mas) and (np.array_equal(diag_t,mas) or np.array_equal(diag_t,sam))):
      total_matches+=1
print(total_matches)
