import re

def checkio(data):
    if len(data) >= 10 and re.search("[0-9]",data) and re.search("[a-z]",data) and re.search("[A-Z]",data):
        return True
    else:
        return False
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
■学習したこと
・Pythonで正規表現を扱いたいときは，「re」モジュールを用いることが一般的
・その中にxxが含まれるか否かはsearch()メソッドを利用。その他,match()なども可
・注意：re.search は最初にマッチした文字列の情報しか取得できない

■参考リンク
・Pythonの正規表現の基本的な使い方:http://uxmilk.jp/41416
・サンプル集：http://www.megasoft.co.jp/mifes/seiki/meta.html
■Next
・re.match()の使い方
・re.search(r[],data)のrは何か調べる
・正規表現の基礎を学ぶ

"""