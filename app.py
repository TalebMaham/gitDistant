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
        user = {
            'name': request.json['name'],
            'email': request.json['email']
        }
        users.append(user)
        return jsonify({'message': 'User added successfully!', 'user': user}), 201
    else:
        # Lister tous les utilisateurs
        return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)
