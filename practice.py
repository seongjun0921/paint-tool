import cv2
import sys
import numpy as np

canvas = np.full((512,512, 3), 255, dtype=np.uint8)

def mouse_drag(event, x, y, flags, param):
    if flags & cv2.EVENT_FLAG_LBUTTON:
        cv2.line(canvas, (x, y), (x+1, y+1), (0, 0, 0), 5)
        cv2.imshow('canvas', canvas)
        print('(x,y)', (x, y))
cv2.imshow('canvas', canvas)
cv2.setMouseCallback('canvas', mouse_drag)

while True:
    key = cv2.waitKey(0)
    if key == ord('c'):
        canvas.fill(255)
        cv2.imshow('canvas', canvas)
    elif key == ord('q') or key == 27:
        break
    else:
        cv2.imshow('canvas', canvas)
cv2.destroyAllWindows()


# 1. `512x512` 크기의 흰색 빈 이미지를 생성합니다.
# 2. 마우스 **왼쪽 버튼을 누른 채로 이동(Drag)** 하면 검은색(`(0, 0, 0)`) 선이 그려져야 합니다.
# 3. 마우스 버튼을 놓으면 그리기가 멈춰야 합니다.
# 4. 키보드 `c`를 누르면 캔버스가 초기화(Clear) 됩니다.
# 5. 키보드 `q` 또는 `ESC`를 누르면 프로그램이 종료됩니다.