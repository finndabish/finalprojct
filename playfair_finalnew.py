"""
CS120
Final Project
Corinne and Finn
"""

row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
table = [row1, row2, row3, row4, row5]

def make_table(keyword): #this makes the 5x5 table
    alphabet_noj = 'abcdefghiklmnopqrstuvwxyz'
    for letter in keyword:
        for i, row in enumerate(table):
            if letter in table[i - 1]:
                break
            elif len(row) <= 4:
                row.append(letter)
    for letter2 in alphabet_noj:
        for i, row in enumerate(table):
            if letter2 in table[i - 1] or letter2 in table[i]:
                break
            elif len(row) <= 4:
                row.append(letter2)    
    return table

def separate_phrase(phrase): #makes the phrase we want to encrypt into a 2D list of pairs of letters
    separated_phrase = []
    separated_phrase2 = []
    for i, letter in enumerate(phrase):
        if letter == ' ': #ignores spaces so we can have multiple word phrases
            pass
        else:
            separated_phrase.append(letter)
        
    for i, letter in enumerate(separated_phrase):
        if separated_phrase[i] == separated_phrase[i-1]:
            separated_phrase.insert(i, "x")
            
    if len(separated_phrase) % 2 == 1:
        separated_phrase.append('x')
    
    for i in range(len(separated_phrase) // 2):
        separated_phrase2.append([])
    for i, letter in enumerate(separated_phrase):
        if i % 2 == 0:
            for lst in separated_phrase2:
                if len(lst) < 2:
                    lst.append(letter)
                    break
                    
        if i % 2 == 1:
            for lst in separated_phrase2:
                if len(lst) < 2:
                    lst.append(letter)
                    break        
                    
    return separated_phrase2
    

def encrypt(phrase, word):
    e_phrase = [] #the thing we wanna return eventually
    table = make_table(word)
    keep_index0 = []
    keep_index1 = []
    
    for pair in separate_phrase(phrase): #looping over the phrase pair by pair. 
        for index, row in enumerate(table): #for each pair, look at every row in the table
            
            if pair[0] and pair[1] in row: #if they are in the same row
                for letter in row: #for each row, look at every letter individually
                    if pair[0] == letter and row.index(letter) != 4: #if the first letter in pair is the letter we are on
                        e_phrase.append(row[int(row.index(letter) + 1)]) #add the next letter in the same row to the return list
                    elif row.index(letter) == 4:
                        e_phrase.append(table[index][0])#if the letter is last in the row, instead add the first letter in row
                        
                for letter in row:
                    if pair[1] == letter and row.index(letter) != 4:
                        e_phrase.append(row[int(row.index(letter) + 1)])
                    elif row.index(letter) == 4:
                        e_phrase.append(table[index][0])#if the letter is last in the row, instead add the first letter in row
                            
            if pair[0] in row and pair[1] not in row:          
                for letter in row:
                    if pair[0] == letter:
                        keep_index0.append(index) #add the row# of first letter in the pair to a list
                        keep_index0.append(row.index(letter)) #add the letter# of the first letter in the pair to the same list
                        
            elif pair[1] in row and pair[0] not in row: #if the second letter is there but NOT the first one
                for letter in row:
                    if pair[1] == letter:
                        keep_index1.append(index) #add row# of the second letter to a list
                        keep_index1.append(row.index(letter)) #add letter# of the second letter to the same list
                    
        if keep_index0[1] == keep_index1[1]:#if the pair is in the same column different row#, add the same letter# but the next row#
            try: 
                e_phrase.append(table[int(index) + 1][keep_index0[1]])
                keep_index0.clear()
                keep_index1.clear()
                
            except IndexError:
                e_phrase.append(table[0][keep_index0[1]])#if the letter is in the last row, add the letter from the first row in the corresponding column
        else:
            None #shouldnt use pass here because i still need it to do the code under it
                    
        if keep_index0[1] != keep_index1[1]:
            e_phrase.append(table[keep_index0[0]][keep_index1[1]]) #add the row# of the first letter but the letter# of the second letter
            e_phrase.append(table[keep_index1[0]][keep_index0[1]]) #add the row# of the second letter but the letter# of the first letter
            keep_index0.clear()
            keep_index1.clear()
                      
    return e_phrase
    
    
    
print(make_table('lizard'))
print(separate_phrase('house'))
print(encrypt('house', 'lizard'))

