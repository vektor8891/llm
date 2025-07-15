# Import the necessary packages
import gradio as gr
import os
from dotenv import load_dotenv
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm.llms import WatsonxLLM

# Load environment variables from .env file
load_dotenv()

# Specify the model and project settings
# (make sure the model you wish to use is commented out, and other models are commented)
model_id = 'mistralai/mixtral-8x7b-instruct-v01'  # Specify the Mixtral 8x7B model
# model_id = 'ibm/granite-3-3-8b-instruct'  # Specify IBM's Granite 3.3 8B model

# Set the necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 512,  # Specify the max tokens you want to generate
    GenParams.TEMPERATURE: 0.5,  # This randomness or creativity of the model's responses
}

# Wrap up the model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url=os.getenv("WATSONX_URL"),
    apikey=os.getenv('IBM_CLOUD_API_KEY'),
    project_id=os.getenv("WATSONX_PROJECT_ID"),
    params=parameters
)


def generate_response(prompt_txt):
    # Function to generate a response from the model
    generated_response = watsonx_llm.invoke(prompt_txt)
    return generated_response


# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2,
                      placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port=7860)
