from pyzbar.pyzbar import decode
import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('qrcode_make_test1.jpg')
# QRコードのデータ取得
decode_data = decode(img)
print(decode_data)

# 画像内のQRコードを数える
qrcode_num = len(decode_data)

if qrcode_num != 0:
    for i in range(qrcode_num):
        # QRコードの座標部分を抽出
        polygon = decode_data[0].polygon
        # QRコード四隅の座標を取得
        left_top = [polygon[0][0], polygon[0][1]]
        left_bottom = [polygon[1][0], polygon[1][1]]
        right_bottom = [polygon[2][0], polygon[2][1]]
        right_top = [polygon[3][0], polygon[3][1]]
        # QRコード四隅の座標を整理
        points = np.array([left_top, left_bottom, right_bottom, right_top])
        # QRコードを囲う線分を画像に描画
        cv2.polylines(
            img, # 画像データ
            [points], #多角形描画座標
            isClosed=True, # 多角形の線分が繋がっているか
            color=(0, 255, 0), # 線の色
            thickness=2 # 線の太さ
            )
        
        
        # QRコードの読み取りデータを抽出
        text = decode_data[i].data.decode('utf-8')
        # QRコードの描画座標を指定
        text_coordinate = (left_top[0], left_top[1]-10)
        
        # 画像に読み取りデータのテキストを描画
        cv2.putText(
            img, # 画像データ
            text, # 読み取り内容
            text_coordinate, # 描画座標
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, # フォント
            fontScale=0.5, # 文字の大きさ
            color=(0, 0, 0), # 文字の色
            thickness=1, # 文字の太さ
            lineType=cv2.LINE_AA, # 線の描画方法
        )
        # QRコードの枠と読み取りデータを描画した画像を保存
        cv2.imwrite('qrcode_read_result.jpg', img)
else:
    'There was no QR code.'