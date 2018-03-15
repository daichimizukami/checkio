
def count_words(text, words):
    
    cnt = 0

    for w in words:
        if (w in text.lower()) == True:
             cnt += 1
        else:
            continue #pass
    return cnt


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""
■アルゴリズム
・words回数分、textの中にwordが含まれているか確認
・含まれてたらカウントアップ

■学習したこと
・要素の確認(in演算子, indexメソッド, countメソッド)
A in B = True/Flase
https://www.pythonweb.jp/tutorial/list/index10.html

・forのpass,continueの違い
continueは続く命令を実行せず、次のループへ突入する。
http://code.i-harness.com/ja/q/90b6cb

■Next
・形態素解析
https://qiita.com/pika_shi/items/94df1d8f47ef82cf39c8

"""
