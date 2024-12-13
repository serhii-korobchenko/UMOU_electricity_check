from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.debug = True
app.env = "development"

# Store received messages in memory (for demonstration purposes)
received_messages = []


@app.route('/')
def home():
    # Render the template with the list of received messages
    return render_template('index.html', messages=received_messages)


@app.route('/callback', methods=['POST'])
def message_callback():
    try:
        # Retrieve JSON payload from the POST request
        data = request.json

        # Log the received message
        print("Received Message:", data)

        # Append the received message to the list
        received_messages.append(data)

        # Return a success response
        return jsonify({"status": "success", "message": "Message received successfully"}), 200
    except Exception as e:
        # Handle any errors
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')