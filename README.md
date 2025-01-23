# AI Content Generator API

The AI Content Generator API is a FastAPI-based application that generates content based on input topics and keywords. This project was created and maintained by Marco Di Bella.

## Features

- Generate articles based on a topic and optional keywords.
- Customizable content length.
- API authentication using API keys.
- Dockerized for easy deployment.

## Requirements

- Python 3.10+
- OpenAI API key
- Docker (optional for containerized deployment)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-content-generator-api.git
   cd ai-content-generator-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

5. Access the API documentation at:

   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Docker Deployment

1. Build the Docker image:

   ```bash
   docker build -t ai-content-generator-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 --env OPENAI_API_KEY=your_openai_api_key ai-content-generator-api
   ```

3. The application will be accessible at:

   - [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints

### `GET /health`

- **Description:** Checks the health of the API.
- **Response:**
  ```json
  {
      "status": "API is running",
      "author": "Marco Di Bella"
  }
  ```

### `POST /generate`

- **Description:** Generates content based on the input.
- **Request Body:**
  ```json
  {
      "topic": "Artificial Intelligence",
      "keywords": ["machine learning", "deep learning"],
      "length": 300
  }
  ```
- **Response:**
  ```json
  {
      "author": "Marco Di Bella",
      "topic": "Artificial Intelligence",
      "content": "...generated content here..."
  }
  ```

## Authentication

- Use the `x-api-key` header to authenticate requests.
- Example:
  ```bash
  curl -X POST "http://127.0.0.1:8000/generate" \
       -H "x-api-key: example-key-123" \
       -H "Content-Type: application/json" \
       -d '{"topic": "Artificial Intelligence", "keywords": ["machine learning"], "length": 300}'
  ```

## Author

Marco Di Bella

## License

This project is licensed under the MIT License.
