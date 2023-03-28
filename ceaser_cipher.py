def decryption(cipher_texts, shift):
    alpa = list("abcdefghijklmnopqrstuvwxyz")
    result = ""
    for cipher_text in cipher_texts:       
            for x in range(0,len(alpa)):
                if alpa[x] == cipher_text.lower():
                    result += alpa[(x - shift + 26)%26]
                    break
            else:
                result += cipher_text      
    return result

def encryption(plain_texts, shift):
    alpa = list("abcdefghijklmnopqrstuvwxyz")
    result = ""
    for plain_text in plain_texts:       
            for x in range(0,len(alpa)):
                if alpa[x] == plain_text.lower():
                    result += alpa[(x + shift)%26]
                    break
            else:
                result += plain_text      
    return result

plain_text = "transparency and security are two major advantages"
cipher_text = "ayhuzwhylujf huk zljbypaf hyl adv thqvy hkchuahnlz"

with open('ceaser_cipher.txt', "a", encoding="utf-8") as f:
    print("cipher_text : " + encryption(plain_text, 3))
    run = 1
    decryption_result = ""
    while run < 26:
        f.write(str(run) + ". " + decryption(cipher_text, run) + "\n")
        run = run + 1

    








