row_list = []

row_input = ''

firstrow_index = 0

cols = 0

word_list = []

word_list_copy = []


def reverse_list_converter(word):
    index = len(word) - 1
    string = ''
    for i in range(0, len(word)):
        string += word[index]
        index = index - 1
    return string


       
while True:
    row_input = str(input('What is the letters for the next row? If you are all done, type DONE in all capital letters.'))
    if firstrow_index == 0:
        cols = len(row_input)
        firstrow_index = 1
       
    if row_input == 'DONE':
        break
   
    if len(row_input) != cols:
        print("You must enter the same amount of characters as you did in the first row, which  is " + str(cols))
    elif len(row_input) == cols:
        row_letters = str(row_input)
        row_list.append(row_letters)


totalrows = len(row_list)




while True:
    word_list_input = str(input('What is the next word? Enter DONE in all capital letters if you are finished.'))
    if word_list_input == 'DONE':
        break
    else:
        word_list.append(word_list_input)

for word in word_list:
    word_list_copy.append(word)

for word in word_list_copy:
    word_list.append(reverse_list_converter(word))





rows, column = (totalrows, cols)
arr = [[0 for i in range(cols)] for j in range(rows)]



for x in range(0, totalrows):
    for y in range(0, cols):
        arr[x][y] = (row_list[x])[y]



def diag_check(array):
    column = 0
    row = 0
    string = ''
    diag_list = []
    diag_index = 0

#for left-to-right diagonals
    while True:
        string += str(arr[diag_index][diag_index])
        diag_index += 1
        column += 1
        row += 1
        if column == cols or row == totalrows:
            break
    diag_list.append(string)
   
    for i in range(1, totalrows):
        string = ''
        column = 0
        row = 0
        diag_index = 0
        while True:
            if column == cols or row == totalrows - i:
                break
            string += str(arr[i + diag_index][diag_index])
            diag_index += 1
            column += 1
            row += 1
        diag_list.append(string)
       
       
    for i in range(1, cols):
        string = ''
        column = 0
        row = 0
        diag_index = 0
        while True:
            if column == cols - i or row == totalrows:
                break
            string += str(arr[diag_index][i + diag_index])
            diag_index += 1
            column += 1
            row += 1
        diag_list.append(string)
   
   
    for diagonal in diag_list:
        for word in word_list:
            if word.lower() in diagonal:
                start_letter = 0
                if diagonal == diag_list[0]:
                    start_letter = diagonal.index(word)
                    for letter in range(0, len(word)):
                        (arr[start_letter + letter][start_letter + letter]) = (arr[start_letter + letter][start_letter + letter]).upper()
                elif diag_list.index(diagonal) < totalrows:
                    start_letter = diagonal.index(word)
                    for letter in range(0, len(word)):
                        arr[start_letter + letter + diag_list.index(diagonal)][start_letter + letter] = (arr[start_letter + letter + diag_list.index(diagonal)][start_letter + letter]).upper()
                elif diag_list.index(diagonal) >= totalrows:
                    start_letter = diagonal.index(word)
                    print(start_letter)
                    for letter in range(0, len(word)):
                        arr[start_letter + letter][start_letter + letter + diag_list.index(diagonal) - totalrows + 1] = (arr[start_letter + letter][start_letter + letter + diag_list.index(diagonal) - totalrows + 1]).upper()
                        
    
    
    
 #for right-to-left diagonals   
    
    column = cols - 1
    row = 0
    string = ''
    diag_list = []
    diag_index = 0
    while True:
        string += str(arr[diag_index][cols - diag_index - 1])
        diag_index += 1
        column = column - 1
        row += 1
        if column == -1 or row == totalrows:
            break
    diag_list.append(string)
   
    for i in range(1, totalrows):
        string = ''
        column = cols - 1
        row = 0
        diag_index = 0
        while True:
            if column == 0 or row == totalrows - i:
                break
            string += str(arr[i + diag_index][cols - diag_index - 1])
            diag_index += 1
            column = column - 1
            row += 1
        diag_list.append(string)
       
       
    for i in range(1, cols):
        string = ''
        column = cols - i - 1
        row = 0
        diag_index = 0
        while True:
            string += str(arr[diag_index][cols - i - diag_index - 1])
            diag_index += 1
            column = column - 1
            row += 1
            if column == -1 or row == totalrows:
                break
        diag_list.append(string)
   
    for diagonal in diag_list:
        for word in word_list:
            if word.lower() in diagonal:
                start_letter = 0
                if diagonal == diag_list[0]:
                    start_letter = diagonal.index(word)
                    for letter in range(0, len(word)):
                        (arr[start_letter + letter][cols - 1 - start_letter - letter]) = (arr[start_letter + letter][cols - 1 - start_letter - letter]).upper()
                elif diag_list.index(diagonal) < totalrows:
                    start_letter = diagonal.index(word)
                    for letter in range(0, len(word)):
                        arr[start_letter + letter + diag_list.index(diagonal)][cols - 1 - start_letter - letter] = (arr[start_letter + letter + diag_list.index(diagonal)][cols - 1 - start_letter - letter]).upper()
                elif diag_list.index(diagonal) >= totalrows:
                    start_letter = diagonal.index(word)
                    print(start_letter)
                    for letter in range(0, len(word)):
                        arr[start_letter + letter][cols - 1 - start_letter - letter - diag_list.index(diagonal) + totalrows - 1] = (arr[start_letter + letter][cols - 1 - start_letter - letter - diag_list.index(diagonal) + totalrows - 1]).upper()
                        
                        









def horizontal_check(array):
    string = ''
    for row in row_list:
        for word in word_list:
            if word.lower() in row:
                 start_letter = row.index(word)
                 for i in range(0, len(word)):
                     arr[row_list.index(row)][start_letter + i] = (arr[row_list.index(row)][start_letter + i]).upper()
                     
                     


def vertical_check(array):
    string = ''
    column_list = []
    for i in range(0, cols):
        string = ''
        for j in range(0, totalrows):
            string += arr[j][i]
        column_list.append(string)
    
    for column in column_list:
        for word in word_list:
            if word.lower() in column:
                start_letter = column.index(word)
                for i in range(0, len(word)):
                    arr[start_letter + i][column_list.index(column)] = (arr[start_letter + i][column_list.index(column)]).upper()
                    
            
    
diag_check(arr)
horizontal_check(arr)
vertical_check(arr)


def list_converter(list):
    string = ''
    for item in list:
        string += item
    return string
   
for row in arr:
    print(row)

