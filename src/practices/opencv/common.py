import cv2
import numpy as np


border_thickness = 3
layer_map = {"b": 0, "g": 1, "r": 2}
color_modes = "bgr"
color_map = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

kernels = [None,
           np.array([[1 / 6, 0, 1 / 6], [1 / 6, 0, 1 / 6], [1 / 6, 0, 1 / 6]]),
           np.array([[1 / 6, 1 / 6, 1 / 6], [0, 0, 0], [1 / 6, 1 / 6, 1 / 6]]),
           np.array([[3 / 16, 1 / 16, 3 / 16], [1 / 16, 0, 1 / 16],
                     [3 / 16, 1 / 16, 3 / 16]])]


class State:
    def __init__(self, **kwargs):
        self.color_mode = None
        for key in kwargs:
            self.set_attr(key, kwargs[key])

    def set_attr(self, att_name: str, value: int = 0):
        self.__setattr__(att_name, value)

    def inc_attr(self, att_name: str, base: int):
        val = self.__getattribute__(att_name) or 0
        if val + 1 < base:
            self.__setattr__(att_name, val + 1)

    def dec_attr(self, att_name: str):
        val = self.__getattribute__(att_name) or 0
        if val - 1 >=0:
            self.__setattr__(att_name, val - 1)


def add_border(image: np.ndarray, color, thickness, frame_width, frame_height):
    image = image.copy()
    cv2.rectangle(image, (0, 0), (frame_width, frame_height), color, thickness)
    return image


def get_layers(image: np.ndarray, layers: str):
    color_layers = cv2.split(image)
    layer_indices = list(map(layer_map.get, layers))

    new_img = []
    for li in range(3):
        if li in layer_indices:
            new_img.append(color_layers[li])
        else:
            new_img.append(np.zeros(image.shape[:2], dtype="uint8"))

    return cv2.merge(new_img)


def switch_color(event, x, y, flags, param: State):
    if event == cv2.EVENT_RBUTTONUP:
        param.inc_attr("color_mode", len(color_modes))
        param.inc_attr("selected_kernel", len(kernels))


def matching_keys(key: str):
    return [ord(key.lower()), ord(key.upper())]


def random_color():
    return (np.random.randint(low=0, high=256),
            np.random.randint(low=0, high=256),
            np.random.randint(low=0, high=256))
