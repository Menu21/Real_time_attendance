import os
import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
from time import time

####################################
classID = 0  # 0 is fake and 1 is real
outputFolderPath = 'dataset/datacollect'
confidence = 0.8
save = True
blurThreshold = 35  # Larger is more focus

debug = False
offsetPercentageW = 10
offsetPercentageH = 20
camWidth, camHeight = 640, 480
floatingPoint = 6
####################################

# Check if the path is a file
if os.path.isfile(outputFolderPath):
    os.remove(outputFolderPath)

# Ensure the output directory exists
os.makedirs(outputFolderPath, exist_ok=True)

# Try different camera indexes
for i in range(3):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Using camera index {i}")
        break
else:
    print("Error: Could not open any video capture device.")
    exit()

cap.set(3, camWidth)
cap.set(4, camHeight)

detector = FaceDetector()

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to read frame. Exiting...")
        break

    imgOut = img.copy()
    img, bboxs = detector.findFaces(img, draw=False)

    listBlur = []  # True/False values indicating if the faces are blur or not
    listInfo = []  # The normalized values and the class name for the label txt file
    if bboxs:
        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]
            score = bbox["score"][0]

            if score > confidence:
                offsetW = (offsetPercentageW / 100) * w
                x = int(x - offsetW)
                w = int(w + offsetW * 2)
                offsetH = (offsetPercentageH / 100) * h
                y = int(y - offsetH * 3)
                h = int(h + offsetH * 3.5)

                x = max(0, x)
                y = max(0, y)
                w = max(0, w)
                h = max(0, h)

                imgFace = img[y:y + h, x:x + w]
                if imgFace.size > 0:
                    blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                    if blurValue > blurThreshold:
                        listBlur.append(True)
                    else:
                        listBlur.append(False)

                    ih, iw, _ = img.shape
                    xc, yc = x + w / 2, y + h / 2
                    xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                    wn, hn = round(w / iw, floatingPoint), round(h / ih, floatingPoint)
                    
                    xcn = min(1, xcn)
                    ycn = min(1, ycn)
                    wn = min(1, wn)
                    hn = min(1, hn)

                    listInfo.append(f"{classID} {xcn} {ycn} {wn} {hn}\n")

                    cv2.rectangle(imgOut, (x, y, w, h), (255, 0, 0), 3)
                    cvzone.putTextRect(imgOut, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 10),
                                       scale=2, thickness=3)

                    if debug:
                        cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                        cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 10),
                                           scale=2, thickness=3)

        if save and all(listBlur) and listBlur:
            timeNow = str(int(time() * 1000000))
            cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)

            with open(f"{outputFolderPath}/{timeNow}.txt", 'a') as f:
                f.writelines(listInfo)

    cv2.imshow("Image", imgOut)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
