import gradio as gr


def calculator(num1, num2, operation="add"):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2


demo = gr.Interface(
    calculator,
    [
        gr.Number(label="Num1", info="Number 1", elem_id="num1"),
        gr.Number(label="Num2", info="Number 2", elem_id="num2")
    ],
    additional_inputs= [
        gr.Radio(["add", "subtract", "multiply", "divide"], elem_id="op", info="Operation type", value="add"),
    ],
    outputs=gr.Number(label="Result", info="Result", elem_id="result"),
    examples=[
        [45, 3, "add"],
        [3.14, 2, "divide"],
        [144, 2.5, "multiply"],
        [0, 1.2, "subtract"],
    ],
    title="Butter Bot",
    description='What is my purpose <img src="https://i.redd.it/jq6l5lqqhfxa1.jpg" '
                'alt="Girl in a jacket" width="500" height="600" style="aligned:center;">',
    # cache_examples="lazy",
    flagging_options=["Wrong", "Error", "Interesting!"]
)

demo.launch()
