import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# imshow : ウィンドウへ画像を表示する関数
# 第一引数 : ウィンドウ名(自由に命名ください)
# 第二引数 : 多次元配列(numpy.ndarray)
# imshow関数について : https://kuroro.blog/python/KKpVvO2dnumZPPVu6lH1/
cv2.imshow('image', img)

# Pythonプログラムの終了とともに、画像を表示するウィンドウがすぐに閉じられてしまうため、waitKey関数を利用する。
k = cv2.waitKey(0)

# キーボードから's'の文字が入力された場合、画像を保存する。
# ord : 文字を10進数で表記されるアスキーコードへ変換する。
if k == ord('s'):
    # imwrite : 画像の保存を行う関数
    # 第一引数 : 保存先の画像ファイル名
    # 第二引数 : 多次元配列(numpy.ndarray)
    # <第二引数の例>
    # [
    # [
    # [234 237 228]
    # ...
    # [202 209 194]
    # ]
    # [
    # [10 27 16]
    # ...
    # [36 67 46]
    # ]
    # [
    # [34 51 40]
    # ...
    # [50 81 60]
    # ]
    # ]
    # imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
    cv2.imwrite('output.jpg', img)
