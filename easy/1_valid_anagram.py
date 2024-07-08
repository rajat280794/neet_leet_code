"""
Given two strings s and t, return true if t is an anagram of s and false otherwise.
"""

s = input("Enter string s: ")
t = input("Enter string t: ")


def check_anagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        if set(s) == set(t):
            return check_anagram_2(s, t)
        return False
    return False


def check_anagram_2(s: str, t: str) -> bool:
    # convert string to list to use inbuilt sort method of lists
    # there is another option to use sorted(): sorted() function accepts any iterable and not just lists
    s_list = list(s)
    t_list = list(t)
    sorted_s = s_list.sort()
    sorted_t = t_list.sort()
    if sorted_s == sorted_t:
        return True
    return False


value = check_anagram(s, t)

if value:
    print("Strings are anagram")
else:
    print("Not anagram")
