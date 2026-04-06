'''2942. Find Words Containing Character
Easy

You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

'''
def findWordsContaining(words,x):
    result = []
    for idx, word in enumerate(words):
        if x in word:
            result.append(idx)
    print(result)    
    return result   


words = ["leet","code"]
x = "e"
findWordsContaining(words,x)