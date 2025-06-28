# Backbone Backend

FastAPI backend for the Backbone project.

## Features

- RESTful API with FastAPI
- CORS enabled for frontend communication
- Pydantic models for data validation
- Health check endpoint
- CRUD operations for items

## Setup

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Docker

Build and run with Docker Compose from the root directory:
```bash
docker-compose up backend
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /items` - Get all items
- `GET /items/{item_id}` - Get specific item
- `POST /items` - Create new item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 