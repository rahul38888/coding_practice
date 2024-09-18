import datetime

import gradio as gr


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(
            """
            <center>
                <h1>Butter Robot!</h1>
                <h3>What is my purpose? </h3>
            </center>
            """)

    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                <center>
                    <img src="https://i.redd.it/jq6l5lqqhfxa1.jpg"  alt="Girl in a jacket" height="200" />
                </center>
                """)

        with gr.Column():
            chatbot = gr.Chatbot(bubble_full_width=False)
            prompt = gr.Textbox(label="Prompt", placeholder="Earth")
            # greet_btn = gr.Button("Ask")

    # @greet_btn.click(inputs=[prompt, chatbot], outputs=[prompt, chatbot])
    def user_message(user_text, history):
        return "", history + [[user_text, None]]

    def agent_message(history):
        user_text = history[-1][0]
        res = "Did you say \"" + user_text + "\"?"
        history[-1][1] = res
        return history


    prompt.submit(user_message, inputs=[prompt, chatbot], outputs=[prompt, chatbot], queue=False).then(
        agent_message, inputs=chatbot, outputs=chatbot
    )

if __name__ == '__main__':
    demo.launch()
