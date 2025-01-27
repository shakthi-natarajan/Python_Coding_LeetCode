def valid_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            s1=s[:left]+s[left+1:]
            s2=s[:right]+s[right+1:]
            if s1[:]==s1[::-1] or s2[:]==s2[::-1]:
                return True
            else:
                return False
        else:
            left+=1
            right-=1
    return True

print(valid_palindrome("malayallaml"))
