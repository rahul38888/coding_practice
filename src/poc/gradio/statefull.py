import gradio as gr
import random


def roll(sides: int, history: list[int]):
    r = random.randint(1, sides)
    history.append(r)
    return r, history, history


demo = gr.Interface(
    fn=roll,
    inputs=[gr.Radio(choices=[20]), gr.State(value=list())],
    outputs=[gr.Number(label="Roll output"), "json", gr.State()]
)
demo.launch()

if __name__ == '__main__':
    pass
