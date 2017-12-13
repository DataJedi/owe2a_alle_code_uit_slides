import re

# Opdracht 1#
seq = "CGTGATGCAGTGACGTACTAGTCAGCGATGACGCGACTTAA"
matchObj = re.search("(ATG|TAA|TAG|TGA)",seq)
print(matchObj.string)
################################

seq = "CGTGATGCAGTGACGTACTAGTCAGCGATGACGCGACTTAA"
#pattern = re.compile("(ATG|TAA|TAG|TGA)")
pattern = re.compile("C.C")
matchObj = pattern.search(seq)
print(matchObj.group())

# Voorbeeld sub
seq = "ATGCATGCAGCATGCAGTATGACAGCTATATACGAC"
pattern = "(TAG|TGA|TAA)"
print(re.sub(pattern, "*", seq))
################################

# Opdracht 3
seq = "CGTGATGCAGTGACGTACTAGTCAGCGATGACGCGACTTAA"
pattern = "ATG"
matchObj = re.search(pattern, seq)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())
print(seq[matchObj.start():matchObj.end()])
################################

# Opdracht 4
#import re
seq = "CGTGATGCAGTACGTACTAGTCAGCGATTTAGACGCGACTTAA"
pattern = "ATG([ATGC]{3})*(TAA|TGA|TAG)"
matchObj = re.search(pattern, seq)
if matchObj:
    print("Span: ",matchObj.span())
    print("Coding seq: ",seq[matchObj.start():matchObj.end()])
else:
    print("Geen match gevonden")
################################

# Groepen
seq = "CGTGATGCAGTACGTACTAGTCAGCGATTTAGACGCGACTTAA"
pattern = "([ATGC]{3})*"
matchObj = re.search(pattern, seq)
print(matchObj.groups())
print(matchObj.group(0))
print(matchObj.group(1))


