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

    # その他の記号, 数字などははそのまま出力
    return c

def any_rot(input_string):
    # 文字列に ROT を適用する
    g = (__any_rot(c) for c in input_string)
    # 文字列に直す
    return ''.join(g)

def read_json(output_string):
    # JSONファイルの読み込み
    try:
        with open('1_schema.json', 'r') as f:
            data = json.load(f)
            data['properties']['answer']['title'] = output_string
            return data

    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

def main():
    print('任意のROTで計算します．半角数字で26以下の数字を入力してください')
    global input_num
    try:
        input_num = int(input())
        if input_num > 26:
            print('26以下の数字を入力してください')
            sys.exit()
    except ValueError:
        print ('26以下の数字を入力してください')
        sys.exit()

    print('文字列を入力してください')
    input_string = str(input()) #入力文字列
    judge_chr(input_string)
    output_string = any_rot(input_string) #出力文字列
    print("{}".format(json.dumps(read_json(output_string),indent=2, ensure_ascii=False))) #最終結果JSON出力


if __name__ == '__main__':
    main()