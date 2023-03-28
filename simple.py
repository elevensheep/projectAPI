def simple_substitution(cipher_txt):
    alpa = list("abcdefghijklmnopqrstuvwxyz")
    num = [0] * 26
    ciphers = list(cipher_txt)
    for cipher in ciphers:
        for x in range(0,len(alpa)):
            if alpa[x] == cipher.lower():
                num[x] = num[x] + 1
                break
    print(num)
    num_suv = num
    num.sort()
    max_letter = []
    for compared in range(0,len(num)):
        num.sort()
        for x in range(0,len(num)):
            if num[compared] == num_suv[x]:
                
                max_letter.append(alpa[num_suv[x]])
            else:
                continue
        # max_count = max(num)
        # max_index = num.index(max_count)
        # if 
        # max_letter.append(alpa[max_index])
    print("frequent letter:", max_letter)


text = list("bfx w xobxv fy mt nvf wso jb qmtjbott wso pfjbe wt noii wt no gfmip jy no aosoik yfiifnop xvo hsjbgjhiot xvwx noso ubfnb xf fms eswbpywxvost")
result = simple_substitution(text)
print()