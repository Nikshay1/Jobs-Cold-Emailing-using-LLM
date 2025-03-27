# 📧COLD EMAILING PROJECT

This README provides instructions on how to set up and run this project.

## Prerequisites

Before you begin, ensure you have the following installed:

* Python
* pip (package installer for Python)

## Setting up the Environment

It is highly recommended to create a new virtual environment to isolate the project dependencies. This prevents conflicts with other Python projects.

### Creating a New Environment

Open your terminal or command prompt and navigate to the project directory. Then, run the following command to create a new virtual environment named `venv`:

    python -m venv venv

**Note:** If you are using an older version of Python, you might need to use `virtualenv`:

    pip install virtualenv
    virtualenv venv

### Activating the Environment

Once the virtual environment is created, you need to activate it. The activation command depends on your operating system:

**On Windows:**

    venv\\Scripts\\activate

**On macOS and Linux:**

    source venv/bin/activate

You should see the name of the environment (`(venv)`) appear at the beginning of your terminal prompt, indicating that the environment is active.

## Installing Dependencies

There are two ways to install the project dependencies: manually or using a `requirements.txt` file.

### Manual Installation

You can install the required libraries one by one using pip. Make sure your virtual environment is activated before running these commands:

    pip install chromadb
    pip install langchain-groq
    pip install langchain_community beautifulsoup4
    pip install streamlit

### Installing from `requirements.txt`

Alternatively, if a `requirements.txt` file is provided in the project, you can install all the dependencies at once. First, ensure you have created and activated your virtual environment. Then, navigate to the project directory in your terminal and run:

    pip install -r requirements.txt

This command will read the `requirements.txt` file and install all the listed packages and their dependencies.

## Configuring the GROQ API Key

This project utilizes the Langchain GROQ integration, which requires an API key. Follow these steps to obtain and configure your API key:

1.  **Create a GROQ API Key:** Visit the [GROQ Console](https://console.groq.com/keys) and create a new API key.
2.  **Create a `.env` file:** In the root directory of the project, create a new file named `.env`.
3.  **Add the API Key to `.env`:** Open the `.env` file and add your GROQ API key in the following format:

    ```
    GROQ_API_KEY=YOUR_GROQ_API_KEY
    ```

    Replace `YOUR_GROQ_API_KEY` with the actual API key you obtained from the GROQ Console.

## Running the Project

To run the project, open your terminal, navigate to the root directory of the project, and then execute the following command:

    streamlit run main.py
