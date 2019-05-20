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


def __rot13(c):
    if 'A' <= c and c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))

    # その他の記号，数字などはそのまま出力
    return c


def rot13(input_string):
    # 文字列に ROT13 を適用する
    g = (__rot13(c) for c in input_string)
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
    input_string = str(input()) #入力文字列
    judge_chr(input_string)
    output_string = rot13(input_string) #出力文字列
    print(read_json(output_string))


if __name__ == '__main__':
    main()