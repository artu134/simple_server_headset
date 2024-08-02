
# Flask Server for Generating Random Coordinates

This project implements a simple Flask server that listens for GET requests at the `/get_coords` endpoint and returns a JSON response containing two objects with randomly generated coordinates (x, y, z) and unique IDs.

## Requirements

- Python 3.6+
- Flask

## Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the server, execute the following command in the project directory:

```bash
python app.py
```

The server will start listening on `0.0.0.0` at port `5000`.

## Endpoint

### GET `/get_coords`

This endpoint returns a JSON response with two objects. Each object contains the following fields:

- `id`: A unique integer identifier for the object.
- `x`: A float representing the x-coordinate (randomly generated between 10 and 800).
- `y`: A float representing the y-coordinate (randomly generated between 10 and 800).
- `z`: A float representing the z-coordinate (randomly generated between 10 and 800).

#### Example Response

```json
[
    {
        "id": 1,
        "x": 123.45,
        "y": 678.90,
        "z": 234.56
    },
    {
        "id": 2,
        "x": 345.67,
        "y": 456.78,
        "z": 567.89
    }
]
```

## License

This project is licensed under the MIT License.
