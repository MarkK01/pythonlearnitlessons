# String Methods

# len() - returns length of a string
work_tip = "save your code"
print("number of characters in string", len(work_tip))

work_tip = "good code is commented code"
len_tip = len(work_tip)
mid_pt = int(len_tip/2)
print(work_tip[:mid_pt])  # output: good code is
print(work_tip[mid_pt:])  # output: commented code

# .count() - returns number of times a character or sub-string occur
work_tip = "save your code"
print('letter "e" occurrences', work_tip.count("e"))  # output: letter "e" occurrences 2

print(work_tip[:7])  # output: save yo
print("# o's in first half")  # output: # o's in first half
print(work_tip[:7].count("o"))  # output: 1

print()
print(work_tip[7:])  # output: ur code
print("# o's in second half")  # output: # o's in second half
print(work_tip[7:].count("o"))  # output: 1


# .find(string) - returns index of first character of sub-string match
# returns -1 if no match found

work_tip = "save your code"
print("find the index of the first space")
print(work_tip.find(" "), "\n")  # output: 4

work_tip = "good code has meaningful variable names"
print(work_tip)
code_here = work_tip.find("code")
print(code_here, '= starting index for "code"')  # output: 5 = starting index for "code"

# multiple matches in a string
print("work_tip:", work_tip, "\n")
location = work_tip.find("o")

while location >= 0:
    print("'o' at index = ", location)
    location = work_tip.find("o", location + 1)
print("\nno more o's, -1 was returned")

# .find(string, start index, end index)
# same as above .find() but searches from optional start and to optional end index
print('search for "meaning" in the sub-string:', work_tip[13:33], "\n")
meaning_here = work_tip.find("meaning", 13, 33)
print('"meaning" found in work_tip[13:33] sub-string search at index', meaning_here)