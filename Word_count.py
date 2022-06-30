"""
Count words in Python
Problem
Implement a function count_words() in Python that takes as input a string s and a number n, and returns the n most frequently-occuring words in s. The return value
should be a list of tuples - the top n words paired with their respective counts [(<word>, <count>), (<word>, <count>), ...], sorted in descending count order.
You can assume that all input will be in lowercase and that there will be no punctuations or other characters (only letters and single separating spaces).
In case of a tie (equal count), order the tied words alphabetically.
E.g.:
print count_words("betty bought a bit of butter but the butter was bitter",3)
Output:
[('butter', 2), ('a', 1), ('betty', 1)]
Instructions
This is a Python programming exercise. A simple code editor will open up in the next node. Follow the instructions in the template code provided to complete the exercise (look for "TODO"s).
You can execute your program using the Test Run button. Output is shown below the editor area.
"""

"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    lis = s.split() #List of words - repeated
    length = len(lis) #number of words in string
    dup_list = lis #duplicate of list of repeated words - to modify this list to contain only unique occurances of words
    distinct_words = [] #list to store distinct words
    word_count = [] #occurance count of distinct words
    dup_len = len(dup_list)
    i=0
    while i < dup_len:
        count = 0
        word = dup_list[0]
        distinct_words.append(word)
        dup_len = len(dup_list)
        j = 0
        while j < dup_len:
            if(word == dup_list[j]):
                count = count+1
                dup_list.remove(word)
                dup_len = len(dup_list)
                j = j-1
            j = j+1
        word_count.append(count)
     
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    for a in range(len(distinct_words)):
        #large = word_count[a]
        for b in range(len(distinct_words)):
            if word_count[a] > word_count[b]:
                temp = word_count[a]
                word_count[a] = word_count[b]
                word_count[b] = temp
                temp1 = distinct_words[a]
                distinct_words[a] = distinct_words[b]
                distinct_words[b] = temp1
            elif word_count[a] == word_count[b] and a != b :
                if min(distinct_words[a],distinct_words[b]) == distinct_words[a]:
                    if a>b:
                        temp1 = distinct_words[a]
                        distinct_words[a] = distinct_words[b]
                        distinct_words[b] = temp1
                elif min(distinct_words[a],distinct_words[b]) == distinct_words[b]:
                    if b>a:
                        temp1 = distinct_words[b]
                        distinct_words[b] = distinct_words[a]
                        distinct_words[a] = temp1               
                
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    if n == 0:
        print('No count of words requested.')
    elif n>len(distinct_words):
        print('There are lesser number of distinct words than requested')
    else:
        top_n = [(distinct_words[0],word_count[0])]
        for c in range(n-1):
            top_n.append((distinct_words[c+1],word_count[c+1]))
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
