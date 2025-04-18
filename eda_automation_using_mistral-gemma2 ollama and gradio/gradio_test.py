import gradio as gr

def square_num(x):
    return x ** 2
interface = gr.Interface(fn=square_num, inputs='number', outputs='number')

interface.launch()
 