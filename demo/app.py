
import gradio as gr
from gradio_gradio_browser_agent_console import gradio_browser_agent_console


example = gradio_browser_agent_console().example_value()

demo = gr.Interface(
    lambda x:x,
    gradio_browser_agent_console(),  # interactive version of your component
    gradio_browser_agent_console(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
