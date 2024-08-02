from flask import Flask, jsonify
import random

app = Flask(__name__)

# Initialize a counter for IDs
current_id_1 = 1
current_id_2 = 1

@app.route('/get_coords', methods=['GET'])
def get_coords():
    # Generate random coordinates between 10 and 800 for x, y, and z
    def generate_random_coords(id):
        coords = {
            "id": id,
            "x": round(random.uniform(10, 800), 2),
            "y": round(random.uniform(10, 800), 2),
            "z": round(random.uniform(10, 800), 2)
        }
        return coords

    # Generate two objects with random coordinates
    object1 = generate_random_coords(current_id_1)
    object2 = generate_random_coords(current_id_2)
    # Return the list of objects as JSON
    return jsonify([object1, object2])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
