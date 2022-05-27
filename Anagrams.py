# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
from collections import Counter

def find_anagram(word, anagram):
    # [assignment] Add your code here
    input_1 = Counter(word)
    input_2 = Counter(anagram)

    return input_1 == input_2
    

print(find_anagram("pirate", "riot"))

print(find_anagram("liar", "lair"))

print(find_anagram("The doctor is here", "here is their doctor"))


