
import gradio as gr
from gradio_gradio_browser_agent_console import gradio_browser_agent_console

def handle(action: str, state: str):
    state += f"> {action}\n"
    return state, state         # update both copies

with gr.Blocks() as demo:
    log_state = gr.State("") 
    console = gradio_browser_agent_console()

    # wire the change event yourself
    console.change(
        fn=handle,
        inputs=[console, log_state],
        outputs=[console], 
        queue=False               # keep it snappy
    )

if __name__ == "__main__":
    demo.launch()
