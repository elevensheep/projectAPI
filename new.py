def simple_substitution(cipher_txt):
    # initialize a dictionary to store the letter counts
    counts = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
    # count the occurrences of each letter in the ciphertext
    for letter in cipher_txt:
        if letter in counts:
            counts[letter] += 1
    # sort the counts in descending order and extract the most frequent letter(s)
    max_count = max(counts.values())
    max_letters = [letter for letter, count in counts.items() if count == max_count]
    return max_letters

text = list("bfx w xobxv fy mt nvf wso jb qmtjbott wso pfjbe wt noii wt no gfmip jy no aosoik yfiifnop xvo hsjbgjhiot xvwx noso ubfnb xf fms eswbpywxvost")
result = simple_substitution(text)
print()