from collections import Counter

def checkio(text):

    mwl = Counter(text) #1.配列系の数え上げ
    list = []
    print(mwl)
    
    for key,value in mwl.most_common(): #2.頻出回数が多い順に格納（順不同）
        list.append(key)
    return list[0]

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


"""
■アルゴリズム
1.出現回数を調べる
2.多い順に配列に格納する
3.一番多いものを出力
→できたら例外を付け足して行く

■学習したこと
・モジュール collections.Counter

■参考リンク
・https://www.sejuku.net/blog/28832

■Next


"""