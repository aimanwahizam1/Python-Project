# ---------------------------------------------------------------------------- #
#                                Roman Numerals                                #
# ---------------------------------------------------------------------------- #

""" def romanToInt(s: str) -> int:
    value_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    for i in range(len(s)):
        if i+1 < len(s):
            if value_dictionary[s[i]] >= value_dictionary[s[i+1]]:
                total += value_dictionary[s[i]]
            else:
                total -= value_dictionary[s[i]]
        else:
            total += value_dictionary[s[i]]

    return total
        
print(romanToInt("CIV")) """

# ---------------------------------------------------------------------------- #
#                             Longest Common Prefix                            #
# ---------------------------------------------------------------------------- #

""" from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    common_prefix = ""

    for i in range(len(strs[0])):
        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return common_prefix
        common_prefix += strs[0][i]

print(longestCommonPrefix(["flower","flow","flight"])) """

# ---------------------------------------------------------------------------- #
#                               Valid Parentheses                              #
# ---------------------------------------------------------------------------- #

# NOTE: this exercise used stacks - a queue of LAST IN FIRST OUT
# learnt to use dictionary/hashmap in place of large of statements/switch cases

""" def isValid(s: str) -> bool:

    stack = []
    closed_to_open = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for i in s:
        if i in closed_to_open:
            if stack and stack[-1] == closed_to_open[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False
    
print(isValid("()")) """

# ---------------------------------------------------------------------------- #
#                            Merge Two Sorted Lists                            #
# ---------------------------------------------------------------------------- #

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    output = []

    while list1.val != None and list2.val != None:
        if list1[0] >= list2[0]:
            output.append(list1[0])
            list1.pop(0)
        else:
            output.append(list2[0])
            list2.pop(0)
    
    return output

print(mergeTwoLists(list1=[1,2,4],list2=[1,3,4]))
# print(mergeTwoLists([],[]))
# print(mergeTwoLists([],[0]))
