import cv2

from src.practices.opencv.common import State

win_name = "Test Camera"

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

border_thickness = 3

layer_map = {"b": 0, "g": 1, "r": 2}

selected_color_mode = 0
color_modes = "bgr"
color_map = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

state = State(ksize=5)


def switch_color(event, x, y, flags, param: State):
    if event == cv2.EVENT_RBUTTONUP:
        param.ksize += 2
    if event == cv2.EVENT_LBUTTONUP:
        param.ksize = max(param.ksize - 2, 5)


if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        flipped = cv2.flip(frame, 1)

        blurred = cv2.GaussianBlur(flipped,
                                   (state.ksize, state.ksize), 0)

        cv2.imshow(win_name, blurred)
        cv2.setMouseCallback(win_name, switch_color, param=state)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in [ord('q'), ord('Q')]:
            break

    cam.release()
    cv2.destroyAllWindows()
