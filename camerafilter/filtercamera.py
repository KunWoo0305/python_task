import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다.')
    sys.exit()

i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 흑백 영상
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 흐린 영상
    dst = cv2.blur(frame, (7, 7))

    mode = [frame, ~frame, grayFrame, dst]

    cv2.imshow('filterCamera', mode[i])

    if cv2.waitKey(10) == 13:
        # 보여 주기
        i += 1
        if i == 4:
            i = 0

    cv2.imshow('filterCamera', mode[i])

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
