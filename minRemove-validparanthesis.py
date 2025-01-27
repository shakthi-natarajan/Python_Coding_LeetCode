'''
Remove min invalid paranthesis:
1. got through the string one char at a time
2. if it is brackets, push it into stack:
    if open brackets- push
    if close brackets- is there a matching open- pop both
    else: pop close bracket from string
'''
def minRemoveToMakeValid(s):
    stack=[]
    index_to_remove=set()
    for i, char in enumerate(s):
        if char=='(':
            stack.append(i)
        elif char==')':
            if stack:
                stack.pop()
            else:
                index_to_remove.add(i)
    
    #add remaining stack elements to list_index
    index_to_remove.update(stack)

    result=[]
    for index, char in enumerate(s):
        if index not in index_to_remove:
            result.append(char)
    s=''.join(result)      
    print(s)

minRemoveToMakeValid('))((')