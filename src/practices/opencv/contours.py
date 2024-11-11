import cv2

from src.practices.opencv.common import State, matching_keys

win_name = "Canny Edges"
image_org = cv2.imread("image.jpg")

frame_width = image_org.shape[1]
frame_height = image_org.shape[0]


state = State(t1=0, t2=254)


if __name__ == '__main__':
    while True:
        image = cv2.flip(image_org, 1)
        canny = cv2.Canny(image, state.t1, state.t2)
        contours, hierarchy = (
            cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE))
        print(f"Number of Contours = {len(contours)}, "
              f"t1 = {state.t1}, t2 = {state.t2}")
        cv2.drawContours(image, contours, -1, (255, 255, 255), 2)
        cv2.imshow(win_name, image)

        # Press 'q' to exit the loop
        key = cv2.waitKey(1)
        if key in matching_keys('d'):
            state.inc_attr("t1", 255)
        elif key in matching_keys('a'):
            state.dec_attr("t1")
        elif key in matching_keys('w'):
            state.inc_attr("t2", 255)
        elif key in matching_keys('s'):
            state.dec_attr("t2")
        elif key in matching_keys('q'):
            break

    cv2.destroyAllWindows()