# Author: SCT (AMDG) 11/15/21

word1 = list(input("Enter a word to be tested:\n"))

word2 = list(input("Enter a second word to be tested:\n"))
word1.sort()
word2.sort()

if word1 == word2:
    print("These words are anagrams")
else:
    print("These words are not anagrams")
