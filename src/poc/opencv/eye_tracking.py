import time

import cv2

face_cascade = (
    cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml'))
eye_cascade = (
    cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml'))

cap = cv2.VideoCapture(0)

half_blue = (255, 0, 0, 0.5)
half_green = (0, 255, 0, 0.5)
half_red = (0, 0, 255, 0.5)


def available(cam):
    if cam is None or not cam.isOpened():
        return False
    return True


if __name__ == '__main__':
    print("Waiting for the camera to come up", end="")
    # time.sleep(5)
    while not available(cap):
        print(". ", end="")
        time.sleep(0.100)

    while True:

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), half_blue, 2)

            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh),
                #               half_green, 2)

                eye_grey = roi_gray[ey:ey + eh, ex:ex + ew]
                eye_color = roi_color[ey:ey + eh, ex:ex + ew]

                blurred = cv2.GaussianBlur(eye_grey, (5, 5), 0)
                thresh = cv2.adaptiveThreshold(blurred, 225,
                                               cv2.ADAPTIVE_THRESH_MEAN_C,
                                               cv2.THRESH_BINARY_INV,
                                               11, 2)

                contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
                contours = sorted(contours, key=lambda c: cv2.contourArea(c),
                                  reverse=True)

                if contours:
                    (cx, cy), radius = cv2.minEnclosingCircle(contours[0])
                    (cx, cy), radius = (int(cx), int(cy)), int(radius)
                    cv2.line(eye_color, (cx, cy), (cx + 50, cy), half_red,
                             2)  # Horizontal line
                    cv2.line(eye_color, (cx, cy), (cx, cy + 50), half_red,
                             2)  # Vertical line
                    cv2.circle(eye_color, (cx, cy), radius,
                               half_green, 2)

        cv2.imshow("Eye tracking", frame)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in [ord('q'), ord('Q')]:
            break

    cap.release()
    cv2.destroyAllWindows()
