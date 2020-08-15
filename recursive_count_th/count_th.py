'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word.lower()
    counter=0
    # TBC
    #basecase
    # if the length of string is less than 2 it cannot hold "th" --- return 0
    # if the length of the string becomes less than 2 --- return 0 
    if len(word) < 2:
        return 0
    # check if the first 2 letters of the string is "th" from start of the string 
    if (word[0 : 2] == "th"): 
        # add one to counter
        counter += 1
        # if it does then call it again starting at next letter after "th"
        # return the number being return plus counter increased by 1
        return count_th(word[2:]) + counter
    
            # example of missing a "th"
            # "ethi" 
            # first loop - "et" != "th" (starting at the next letter)
            # second loop - "hi" != "th" 

    # else just return withouth incriminting 
    return count_th(word[1:]) # start at the next char 