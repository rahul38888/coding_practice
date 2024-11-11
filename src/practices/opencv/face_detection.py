import cv2

from src.practices.opencv.common import add_border

face_cascade = cv2.CascadeClassifier(
    'haarcascades/haarcascade_frontalface_default.xml')

profile_cascade = cv2.CascadeClassifier(
    'haarcascades/haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

win_name = "Camera"
cam = cv2.VideoCapture(0)


frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

half_blue = (255, 0, 0, 0.5)
half_green = (0, 255, 0, 0.5)
half_red = (0, 0, 255, 0.5)


def draw_face_recs(image_frame):
    face_det = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_det:
        image_frame = cv2.rectangle(image_frame, (x, y), (x + w, y + h),
                                    half_blue, 2)

    prof_face_det = None
    if not len(face_det):
        prof_face_det = profile_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in prof_face_det:
            image_frame = cv2.rectangle(image_frame, (x, y), (x + w, y + h),
                                        half_red, 2)

    return image_frame, face_det, prof_face_det


def draw_eye_recs(image_frame, face_det, gray_img):
    for (x, y, w, h) in face_det:
        roi_gray = gray_img[y:y + h, x:x + w]
        roi_color = image_frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh),
                          half_green, 2)

    return image_frame


def detect_smile(image_frame, face_det, gray_img):
    for (x, y, w, h) in face_det:
        roi_gray = gray_img[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(roi_gray)
        if len(smile) > 1:
            image_frame = add_border(image_frame, (0, 255, 0), 3,
                                     frame_width, frame_height)
            continue

    return image_frame


if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        flipped = cv2.flip(frame, 1)
        gray = cv2.cvtColor(flipped, cv2.COLOR_BGR2GRAY)
        image, faces, prof_faces = draw_face_recs(flipped)
        # image = draw_eye_recs(image, faces, gray)
        image = detect_smile(image, faces, gray)

        cv2.imshow(win_name, image)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in [ord('q'), ord('Q')]:
            break

    cam.release()
    cv2.destroyAllWindows()