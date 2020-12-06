'''
Created on Dec 6, 2020

@author: kjsanche
'''
# read data from file
file_handle = open('/Users/kjsanche/Documents/advent2020inputs/inputday6.txt','r')

cntyes = 0
group_ans=[]
with file_handle as f:
    for line in f:# loop through each line
        stripped_line = line.strip()
        if len(stripped_line) == 0: #when reaching a blank line add group yes, clear array
            cntyes += len(group_ans)
            group_ans = []
            continue
        
        for i in stripped_line:
            if i not in group_ans:
                group_ans.append(i)

#add result from last group
cntyes += len(group_ans)
file_handle.close() 
print(cntyes)


# part 2

file_handle = open('/Users/kjsanche/Documents/advent2020inputs/inputday6.txt','r')

cntyes = 0
group_ans=[]
first_person = 1
with file_handle as f:
    for line in f:# loop through each line
        stripped_line = line.strip()
        if len(stripped_line) == 0: #when reaching a blank line add group yes, clear array and reset flag
            cntyes += len(group_ans)
            group_ans = []
            first_person = 1
            continue
        if first_person == 1: #start with first persons answers 
            group_ans = stripped_line
            first_person = 0
        else:
            for i in group_ans:
                if i not in stripped_line:
                    group_ans = group_ans.replace(i,'') #if anyone in group does not have yes for the same question then remove

#add result from last group
cntyes += len(group_ans)
file_handle.close() 
print(cntyes)