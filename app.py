import streamlit as st
import boto3
import os
from langchain_aws import ChatBedrock

# --- Page Configuration ---
# Set the title and icon that appear in the browser tab
st.set_page_config(
    page_title="TerraScribe",
    page_icon="🤖",
    layout="wide"
)

# --- AWS Session & Bedrock Client ---
# It's best practice to explicitly set up your session, especially for Streamlit apps
# This will use the credentials you configure in the terminal later
aws_session = boto3.Session(
    region_name="us-east-1" # IMPORTANT: Bedrock models are primarily in us-east-1, eu-west-3, ap-southeast-1. Use a region where you have model access.
)

# --- Main App Logic ---

# Function to call the Bedrock LLM to generate code
def generate_iac_code(user_request, code_type):
    """
    Takes a user's plain English request and a code type (Terraform or Kubernetes)
    and returns the generated IaC code from Amazon Bedrock.
    """
    try:
        # Initialize the ChatBedrock model from LangChain
        model = ChatBedrock(
            client=aws_session.client("bedrock-runtime"),
            model_id="anthropic.claude-3-sonnet-20240229-v1:0", # A powerful and cost-effective model
            model_kwargs={"temperature": 0.1} # Low temperature makes the output less random and more predictable
        )

        # This is "Prompt Engineering". We give the AI its instructions and persona.
        if code_type == "Terraform (AWS)":
            system_prompt = """
            You are an expert AWS DevOps Engineer and a Terraform specialist. 
            Your task is to generate clean, secure, and production-ready Terraform HCL code based on the user's request.
            Always follow AWS and Terraform best practices. For example:
            - Do not use hardcoded secrets or access keys.
            - Add appropriate and descriptive tags to all resources.
            - Create secure, least-privilege security group rules.
            - Only output the raw Terraform code inside a single code block. Do not include any extra explanations or text outside the code block.
            """
        elif code_type == "Kubernetes (YAML)":
            system_prompt = """
            You are an expert Kubernetes administrator and a YAML specialist. 
            Your task is to generate clean, secure, and production-ready Kubernetes manifest YAML based on the user's request.
            Always follow Kubernetes best practices. For example:
            - Specify resource requests and limits for containers.
            - Use appropriate labels for all resources.
            - Use the latest stable API versions (e.g., apps/v1 for Deployments).
            - Only output the raw YAML code inside a single code block. Do not include any extra explanations or text outside the code block.
            """
        
        # Combine our instructions with the user's specific request
        full_prompt = f"{system_prompt}\n\nUser Request: {user_request}"

        # Send the prompt to the model and get the response
        response = model.invoke(full_prompt)
        
        # The AI's response is in the 'content' attribute. We clean it up.
        generated_code = response.content.replace("```terraform", "").replace("```hcl", "").replace("```yaml", "").replace("```", "").strip()
        
        return generated_code

    except Exception as e:
        # Provide helpful error messages if something goes wrong
        st.error(f"An error occurred with the Bedrock API: {e}")
        st.warning("Please ensure you have AWS credentials configured and have requested access to the 'Claude 3 Sonnet' model in the Amazon Bedrock console in the us-east-1 region.")
        return "# Error generating code. Please check the warnings above."

# --- Streamlit User Interface ---
# This is the code that creates the webpage you see

st.title("🤖 TerraScribe: Your AI Infrastructure Assistant")
st.markdown("Instantly generate production-ready Terraform or Kubernetes code from plain English.")

# Create a sidebar for configuration options
st.sidebar.header("Configuration")
code_type = st.sidebar.selectbox(
    "1. Select the code you want to generate:",
    ("Terraform (AWS)", "Kubernetes (YAML)")
)

st.sidebar.markdown("---")
st.sidebar.info("This app uses Amazon Bedrock (Claude 3 Sonnet) to generate code.")

# Main interface area
st.header("2. Enter your infrastructure request")
user_request = st.text_area("Example: 'Create a private S3 bucket for logs with versioning and server-side encryption enabled'", height=150)

# The "Generate Code" button
if st.button("Generate Code", type="primary"):
    if user_request:
        # Show a spinner while the AI is thinking
        with st.spinner("Generating code with Amazon Bedrock... this may take a moment."):
            generated_code = generate_iac_code(user_request, code_type)
            st.header("3. Generated Code")
            
            # Display the code with the correct language for syntax highlighting
            output_language = 'terraform' if 'Terraform' in code_type else 'yaml'
            st.code(generated_code, language=output_language, line_numbers=True)

            st.success("Code generated successfully!")
    else:
        # Show a warning if the user clicks the button without typing anything
        st.warning("Please enter a request in the text box above.")