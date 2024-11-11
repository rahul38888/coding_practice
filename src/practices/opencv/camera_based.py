import cv2

from src.practices.opencv.common import get_layers, add_border, switch_color, \
    State

win_name = "Camera"

cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

border_thickness = 3

layer_map = {"b": 0, "g": 1, "r": 2}

selected_color_mode = 0
color_modes = "bgr"
color_map = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

state = State(0, 0)

if __name__ == '__main__':
    while True:
        ret, frame = cam.read()
        flipped = cv2.flip(frame, 1)

        color_layer = get_layers(flipped, color_modes[state.color_mode])

        # kernel = kernels[selected_kernel]
        # conv = cv2.filter2D(flipped, -1, kernel) \
        #     if kernel is not None else flipped
        cv2.imshow(win_name, add_border(color_layer,
                                        color_map[state.color_mode],
                                        border_thickness,
                                        frame_width, frame_height))
        cv2.setMouseCallback(win_name, switch_color, param=state)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in [ord('q'), ord('Q')]:
            break

    cam.release()
    cv2.destroyAllWindows()
