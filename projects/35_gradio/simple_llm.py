# Import the necessary packages
import os
from dotenv import load_dotenv
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm.llms import WatsonxLLM

# Load environment variables from .env file
load_dotenv()

# Specify the model and project settings
# (make sure the model you wish to use is commented out, and other models are commented)
# model_id = 'mistralai/mixtral-8x7b-instruct-v01' # Specify the Mixtral 8x7B model
model_id = 'ibm/granite-3-3-8b-instruct'  # Specify IBM's Granite 3.3 8B model

# Set the necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specify the max tokens you want to generate
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

# Get the query from the user input
query = input("Please enter your query: ")

# Print the generated response
print(watsonx_llm.invoke(query))
