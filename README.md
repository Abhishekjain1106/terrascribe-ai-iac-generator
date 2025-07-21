<img width="1919" height="1066" alt="Screenshot 2025-07-21 232729" src="https://github.com/user-attachments/assets/b6e27007-7b01-4d0c-a374-20d973571fcf" />
<img width="1919" height="1066" alt="Screenshot 2025-07-21 232729" src="https://github.com/user-attachments/assets/fd5a934d-e5a0-4bdb-abd3-d4b763b79c7f" />
# 🤖 TerraScribe: The AI-Powered Infrastructure as Code Assistant

TerraScribe is a web-based tool that leverages the power of Amazon Bedrock (Anthropic's Claude 3 Sonnet) to translate plain English requests into production-ready Infrastructure as Code. This project automates the often tedious process of writing boilerplate Terraform and Kubernetes configuration files, allowing DevOps engineers to build faster and more consistently.

![TerraScribe Screenshot](https://github.com/user-attachments/assets/7d560f47-91c9-4b4b-bed4-d5e2c4a1293a)


## 📖 About The Project

As a DevOps engineer, I know that writing Infrastructure as Code (IaC) is essential for modern cloud management. However, it can also be time-consuming and requires remembering the specific syntax for hundreds of different resources.

TerraScribe was built to solve this problem. It acts as an intelligent assistant, allowing a user to describe the infrastructure they need in natural language. The application then uses a powerful Large Language Model (LLM) via Amazon Bedrock to generate the corresponding code, following security and best practices.

**Key Goals:**
*   **Accelerate Development:** Drastically reduce the time it takes to write standard IaC configurations.
*   **Enforce Best Practices:** Use prompt engineering to guide the AI to produce secure and well-structured code.
*   **Explore GenAI in DevOps:** Demonstrate a practical application of Generative AI to solve a real-world DevOps challenge.

## 🛠️ Built With

This project was built using a modern, cloud-native stack:

*   **Application Framework:**
    *   ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
*   **Programming Language:**
    *   ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
*   **AI & Cloud Services:**
    *   ![Amazon Bedrock](https://img.shields.io/badge/Amazon%20Bedrock-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
    *   ![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
    *   `boto3` & `langchain-aws`

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   An AWS account with access to Amazon Bedrock and the 'Claude 3 Sonnet' model enabled in the `us-east-1` region.
*   Python 3.9+ installed on your local machine.
*   AWS credentials configured locally (e.g., via `aws configure`).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Abhishekjain1106/terrascribe-ai-iac-generator.git
    cd terrascribe-ai-iac-generator
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .\.venv\Scripts\activate
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```sh
    streamlit run app.py
    ```


## 💡 Usage

Once the application is running, navigate to the provided `localhost` URL in your browser.

1.  Use the sidebar to select whether you want to generate `Terraform (AWS)` or `Kubernetes (YAML)` code.
2.  In the main text area, type your request in plain English. Be as descriptive as possible.
3.  Click the "Generate Code" button and wait for the AI to produce the result.


## 📞 Contact

Abhishek Jain -(https://linkedin.com/in/abhishek-p-jain) - abhishekjain11.devops@gmail.com

Project Link: [https://github.com/Abhishekjain1106/terrascribe-ai-iac-generator](https://github.com/Abhishekjain1106/terrascribe-ai-iac-generator)
