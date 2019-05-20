import json
import sys
import curses.ascii

def judge_chr(input_string):
    for c in input_string:
        #入力文字がすべて印字可能な ASCII で構成されるか判定
        if not curses.ascii.isprint(c):
            print('すべて印字可能な ASCII で構成される文字列で入力してください')
            sys.exit()

    #入力文字列が空かどうか判定
    if not input_string:
        print('空でない文字列を入力してください')
        sys.exit()
        
def __any_rot(c):
    if 'A' <= c and c <= 'Z':
        # 入力された数字の数だけ，文字をずらす
        return chr((ord(c) - ord('A') + input_num) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 入力された数字の数だけ，文字をずらす
        return chr((ord(c) - ord('a') + input_num) % 26 + ord('a'))

    # その他の文字はそのまま出力
    return c

def any_rot(input_string):
    # 文字列に ROT13 を適用する
    g = (__any_rot(c) for c in input_string)
    # 文字列に直す
    return ''.join(g)


def main():
    print('任意のROTで計算します．半角数字で26以下の数字を入力してください')
    global input_num
    input_num = int(input())
    if input_num > 26:
        print('半角数字で26以下の数字を入力してください')
        sys.exit()

    print('文字列を入力してください')
    input_string = str(input()) #入力文字列
    judge_chr(input_string)
    output_string = any_rot(input_string) #出力文字列
    print('"output":{}'.format(json.dumps(output_string)))
    sys.exit()


if __name__ == '__main__':
    main()