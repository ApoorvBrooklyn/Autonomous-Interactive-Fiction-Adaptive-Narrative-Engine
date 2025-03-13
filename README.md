# Story-Telling Engine

## Overview
The **Story-Telling Engine** is an AI-powered application that generates unique and engaging stories based on user input. It leverages OpenAI's GPT model to craft creative narratives, making it an ideal tool for writers, content creators, and storytelling enthusiasts.

## Features
- Accepts user prompts to generate personalized stories
- Utilizes OpenAI's latest ChatCompletion API
- Supports FastAPI for backend integration
- Simple and intuitive REST API endpoints

## Technologies Used
- Python
- OpenAI API
- FastAPI
- Uvicorn

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip package manager
- OpenAI API key

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/story-telling-engine.git
   cd story-telling-engine
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
   (For Windows PowerShell)
   ```powershell
   $env:OPENAI_API_KEY="your-api-key"
   ```

## Usage
### Running the Server
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### API Endpoints
#### Generate a Story
**Endpoint:** `POST /generate_story`
- **Request Body:**
  ```json
  {
    "prompt": "A mysterious adventure in a haunted castle."
  }
  ```
- **Response:**
  ```json
  {
    "story": "Once upon a time, in a haunted castle..."
  }
  ```

## Troubleshooting
- If you encounter an `openai.ChatCompletion.create` error, ensure your OpenAI library is up-to-date:
  ```bash
  pip install --upgrade openai
  ```

- Ensure your API key is correctly set in the environment variables.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests or report issues on the GitHub repository!

## Contact
For inquiries, reach out to [apoorvssadhale@gmail.com].

