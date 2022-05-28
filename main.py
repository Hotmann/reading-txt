# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    content = filename.read()
    
    return content



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    dict = {}

    occurrences = text.count("python")
    return dict
    

result = count_words()
print (result)

    # return {"as": 10, "would": 20}