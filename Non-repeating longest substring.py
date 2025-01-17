'''
1. loop through each character in the string
2. for each character- 
        if not in stack:
            insert at end
        if in stack:
            join and append beginning till end of stack in a list
            del all from beginning till the position of the first occurance of character
            append char to end of list
        at the end what is left in stack add to list
'''
list1=list(input("Enter the string: "))
length=len(list1)
stack=[]
final_list=[]
max_length=0
for index, char in enumerate(list1):
    if char not in stack:
        stack.append(char)
    elif char in stack:
        new_str=''.join(stack)
        #print(new_str)
        if len(new_str)>max_length:
            max_length=len(new_str)
        final_list.append(len(new_str))
        char_occ_index=stack.index(char)
        #print(char_occ_index)
        del stack[:char_occ_index+1]
        #print(stack)
        stack.append(char)
        #print(stack)
    if index==length-1:
        new_str=''.join(stack)
        if len(new_str)>max_length:
            max_length=len(new_str)
print(max_length)
