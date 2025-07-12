# Platte API Routes

Base URL: `http://backend:8000/platte` (Docker)  
Local URL: `http://localhost:8000/platte`

## Endpoints

### POST `/`
Create a new platte
```json
{
  "name": "string",
  "koerperteil": "string",
  "status": 100,
  "productzustand": "string",
  "sdk": "string",
  "masse": "string",
  "hersteller": "string",
  "bewahrungsort": "string",
  "bestellungstag": "2025-01-01",
  "ansprechpartner": "string",
  "beschreibung": "string",
  "chartData": [1, 2, 3]
}
```

### GET `/`
Get all platten

### GET `/{platten_id}`
Get platte by ID

### PATCH `/{platten_id}`
Update platte (all fields required, use `null` for empty values)
```json
{
  "name": "Updated Name",
  "koerperteil": null,
  "status": null,
  "productzustand": null,
  "sdk": null,
  "masse": null,
  "hersteller": null,
  "bewahrungsort": null,
  "bestellungstag": null,
  "ansprechpartner": null,
  "beschreibung": null,
  "chartData": null
}
```

### DELETE `/{platten_id}`
Delete platte by ID

## Response Format
```json
{
  "status": "success",
  "result": {...}
}
``` 