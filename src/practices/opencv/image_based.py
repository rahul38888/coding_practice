import cv2

from src.practices.opencv.common import add_border, get_layers, switch_color, \
    border_thickness, color_modes, color_map, State, matching_keys

win_name = "Image"
frame = cv2.imread("image.jpg")

frame_width = frame.shape[1]
frame_height = frame.shape[0]

state = State(color_mode=0, selected_kernel=0)

if __name__ == '__main__':
    while True:
        flipped = cv2.flip(frame, 1)
        color_layer = get_layers(flipped, color_modes[state.color_mode])
        cv2.imshow(win_name, add_border(color_layer,
                                        color_map[state.color_mode],
                                        border_thickness,
                                        frame_width, frame_height))
        cv2.setMouseCallback(win_name, switch_color, param=state)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in matching_keys('q'):
            break

    cv2.destroyAllWindows()
