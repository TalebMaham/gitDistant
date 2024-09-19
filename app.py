from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Stockage temporaire des utilisateurs
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        # Ajouter un utilisateur
        if 'email' not in request.json or request.json['email'] == '':
            return jsonify({'error': 'Email is required!'}), 400
        if 'name' not in request.json or request.json['name'] == '':
            return jsonify({'error': 'Name is required!'}), 400
        user = {
            'name': request.json['name'],
            'email': request.json['email']
        }

        users.append(user)
        return jsonify({'message': 'User added successfully!', 'user': user}), 201
    else:
        # Lister tous les utilisateurs
        return jsonify(users), 200

@app.route("/exemple_for_merge", methods = ['GET'])
def exemple_for_merge():
    return jsonify({'message': 'User added successfully!', 'user': "sidi"}), 201

if __name__ == '__main__':
    app.run(debug=True)
