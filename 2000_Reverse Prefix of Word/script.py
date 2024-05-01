def reverse_prefix(word,ch):
    word = word.strip()
    ch = ch.strip()
    if len(word) <= 1 or len(word) > 250 or len(ch) != 1:
        return word
    word = word.lower()
    ch = ch.lower()
    try :
        index = word.index(ch)
    except : return word
    resultat = word[:index][::-1] + word[index:]
    print(resultat)
    return resultat


reverse_prefix("hjwwtjumqkvqcpvkfbgftvpdjopxvxdifravksbvuhkvsjiwklbiqbqyejcccduzadnokxnkolpzbogkafpzortiqdeuegquaqeddahihxngrafrlrccbllgcrmswlfstyzjafkplvacrwijexmtpqexszrartwwgbxuhkxcwfubjdoiorszxzgutvymrdjhdxqngqswwwwjqcvzuyhgcvaehvguczgiapnspkvndgmkoumlbmzefnnodu","b")
#reverse_prefix(input("Enter a word: "),input("Enter a ch: "))