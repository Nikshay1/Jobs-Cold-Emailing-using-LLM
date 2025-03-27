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

    venv\Scripts\activate

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

## Running the Project

\In terminal write streamlit run main.py while being in the root directory. 
## Additional Notes

\[Include any other relevant information, such as configuration details, data setup, or troubleshooting tips.]
