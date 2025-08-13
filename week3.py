# def mid(s):
#     length = len(s)
#     if length == 0:
#         return s  

#     return s[0]+'*'*(length-1)+s[length-1]

# a=mid("shaurya")
# print(a)

# quest1

# def longest(text):
#         words=text.split()
#         long=''
#         for i in words:
#                 if len(i)>len(long):
#                      long=i
#         return long
# print(longest("shauryzza is crazy"))

#question 3

#check if is isogram

# def check_iso(text):
#     a=set(text)
#     if len(a)==len(text):
#         return True
#     return False

# print(check_iso("machinee"))

# #question 4

# def nchars(text,n):
#     #do it through slicing
#     return text[::n]

# print (nchars("shaurya rahlon",4))


# question 5

# def rev_words(text):
#     words=text.split()
#     result=[]
#     for word in words:
#         rev_w=word[::-1]
#         result.append(rev_w)

#     print(' '.join(result))

# print(rev_words("hi huku"))