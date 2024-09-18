import gradio as gr
import numpy as np


def flip(im):
    print("Here")
    return np.flipud(im)


demo = gr.Interface(
    flip,
    gr.Image(sources=["webcam"], streaming=True),
    gr.Image(),
    live=True
)


if __name__ == '__main__':
    demo.launch()
