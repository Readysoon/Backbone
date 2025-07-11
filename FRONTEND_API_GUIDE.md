# Frontend API Guide - Platte Routes

## Base URL (Docker)
```
http://backend:8000/platte
```

## 1. Create Platte
**POST** `http://backend:8000/platte/`

```javascript
const response = await fetch('http://backend:8000/platte/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    "name": "Platten (Osteosyntheseplatten)",
    "koerperteil": "Clavicle",
    "status": 100,
    "productzustand": "Verfügbar",
    "sdk": "13432332424322",
    "masse": "88mm",
    "hersteller": "DePuy Synthes",
    "bewahrungsort": "OG.6 | Raum: 777 | Schrank: 45",
    "bestellungstag": "2025-05-01",
    "ansprechpartner": "Frau Birkmann",
    "beschreibung": "Diese Osteosyntheseplatte eignet sich ideal für die Versorgung von Schlüsselbeinfrakturen.",
    "chartData": [30, 40, -50, -60, 0, 80, 90, 100, 125]
  })
});
```

## 2. Get All Platten
**GET** `http://backend:8000/platte/`

```javascript
const response = await fetch('http://backend:8000/platte/');
const data = await response.json();
```

## 3. Get Single Platte
**GET** `http://backend:8000/platte/{id}`

```javascript
const platteId = "0f5aqc6czeszjtjsyubz";
const response = await fetch(`http://backend:8000/platte/${platteId}`);
const data = await response.json();
```

## 4. Update Platte
**PATCH** `http://backend:8000/platte/{id}`

⚠️ **Important**: All fields are required, use `null` for empty values

```javascript
const platteId = "0f5aqc6czeszjtjsyubz";
const response = await fetch(`http://backend:8000/platte/${platteId}`, {
  method: 'PATCH',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    "name": "Updated Platte Name",
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
  })
});
```

## 5. Delete Platte
**DELETE** `http://backend:8000/platte/{id}`

```javascript
const platteId = "0f5aqc6czeszjtjsyubz";
const response = await fetch(`http://backend:8000/platte/${platteId}`, {
  method: 'DELETE'
});
```

## Response Format
All endpoints return:
```json
{
  "status": "success",
  "result": {...}
}
```

## Field Types
- `name`: string
- `koerperteil`: string
- `status`: integer
- `productzustand`: string
- `sdk`: string
- `masse`: string
- `hersteller`: string
- `bewahrungsort`: string
- `bestellungstag`: date (YYYY-MM-DD)
- `ansprechpartner`: string
- `beschreibung`: string
- `chartData`: array of integers 