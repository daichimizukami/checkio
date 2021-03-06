from collections import Counter
import re

def checkio(text):

    #1.文字列操作(データ加工)
    str = text.lower() #大文字から小文字
    str2 = str.replace(" ", "") #空白を削除
    str3 = re.sub(r'[!-/:-@[-`{-~]', "", str2) #ASCII記号を削除
    str4 = re.sub(r'[0-9]', "", str3) #数字を削除
    print(str4)
    
    #2.各文字数をカウント
    mwl = Counter(str4)
    print(mwl)
    
    #3.文字数が最大のアルファベットのみ格納
    list = []
    cnt = 0    

    for key,value in mwl.most_common(): 
        if cnt <= value:
            list.append(key)
            cnt = value
        else:
            break
    print(list)
    
    #4.アルファベット順にソート 
    list.sort()
    print(list)

    return list[0]

#Lorem ipsum dolor sit amet
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")