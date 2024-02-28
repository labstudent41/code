import timeit
def patternmatch_bruteforce(text,pattern):
    a=len(text)
    b=len(pattern)
    l=a-b+1
    for i in range(l):
        text_index=i
        pattern_index=0
        while text_index<len(text) and pattern_index<len(pattern) and text[text_index]==pattern[pattern_index]:
            text_index+=1
            pattern_index+=1
        if pattern_index==len(pattern):
            return i
    return -1

s1=input("enter text")
s2=input("enter pattern")
print(s1)
print(s2)
print(patternmatch_bruteforce(s1,s2))
print("running time",timeit.timeit())
