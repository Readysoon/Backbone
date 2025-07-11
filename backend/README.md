# Backbone Backend API

## Quick Start URLs

### Docker (Production)
```
http://backend:8000/platte
```

### Local Development
```
http://localhost:8000/platte
```

## Available Endpoints

- `POST /platte/` - Create platte
- `GET /platte/` - Get all platten
- `GET /platte/{id}` - Get platte by ID
- `PATCH /platte/{id}` - Update platte
- `DELETE /platte/{id}` - Delete platte

## Documentation

See `API_DOCS.md` for detailed endpoint documentation.

## Running

```bash
# Local
python -m uvicorn main:app --reload

# Docker
docker-compose up
``` 