import re
string = raw_input("enter the string = ")
def reverse_string(string):
    print string[::-1]

def reverse_the_words_in_string(string):
    word = string.split(' ')
    reverse_words = []
    for rev in word:
        reverse_words.append(rev[::-1])
    print str(' '.join(reverse_words))

def count_element(string):
    fd_element = raw_input("Enter the elment to be found in string = ")
    print string.lower().split().count(fd_element.lower())

def find_sub_string(string):
    f_string = raw_input("Enter sub string to search = ")
    print string.lower().find(f_string.lower())

def find_all_sub_string(string):
    sub = raw_input("Enter sub string to find = ")
    print [(m.start(), m.end()) for m in re.finditer(sub.lower(), string.lower())]

def max_distance(string):
    sub = raw_input("Enter sub string to find distance = ")
    sub_len = len(sub)
    ind = [m.start() for m in re.finditer(sub.lower(), string.lower().replace(" ", ""))]
    if ind is not None:
        print ind[-1] - ind[0] - sub_len
