#Valid word abbreviation
#"sub4u4" ("sub stit u tion")
#word = "substitution", abbr = "sub4u4"

'''
Two pointers
i is start of word and j is start of abbr
- compare letter by letter:
- if number in abbr- it is an abbrv. check for next index and find the number
    - skip word by length of number
at the end
- if i and j reaches end of word and abbr- then true else false

'''

def valid_abbreviation(word, abbr):
    i=j=0
    x=len(word)
    y=len(abbr)
    print(f'x,y: {x,y}')
    
    while i<x and j<y:
        if word[i]==abbr[j]:
            print(f'match: {word[i],abbr[j]}')
            i+=1
            j+=1
        elif abbr[j].isdigit():
            if abbr[j]==0:
                print(False)
            else:
                if abbr[j+1].isdigit():
                    print(f'abbr: {abbr[j:j+2]}')
                    length=int(abbr[j:j+2])
                    i+=length
                    j+=2
                    print(f'i,j= {i,j}')
                else:
                    print(f'abbr: {abbr[j]}')
                    length=int(abbr[j])
                    i+=length
                    j+=1
        else:
            return False
    if i==x and j==y:
        print(f'i,j: {i,j}')
        return True
    else:
        return False
                    
print(valid_abbreviation("internationalization", "i12iz4n"))



    