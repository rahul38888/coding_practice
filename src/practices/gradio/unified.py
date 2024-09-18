import gradio as gr


def generate_text(text_prompt):
    response = f"{text_prompt} back at you"
    return response


textbox = gr.Textbox()

demo = gr.Interface(generate_text, textbox, textbox)

if __name__ == '__main__':
    demo.launch()
