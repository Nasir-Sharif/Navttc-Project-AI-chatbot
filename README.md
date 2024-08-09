
# AI Chatbot Project

This project is an AI chatbot built using Flask for the backend and web technologies (HTML, CSS, JavaScript) for the frontend. The chatbot interface allows users to interact with an AI model, send text messages, and receive responses.

## Features

- **Text-Based Chat:** Users can input messages and receive AI-generated responses.
- **Voice Input:** Users can send voice messages that are converted to text.
- **Responsive Design:** The chatbot interface is responsive and works well on both desktops and mobile devices.
- **Bot and User Avatars:** Each message is accompanied by an avatar, with user messages displayed on the right and bot responses on the left.
- **Speech Synthesis:** The bot can read out its responses using the Web Speech API.

## Project Structure

- `app.py`: Contains the Flask backend that handles routing and communication with the AI model.
- `templates/index.html`: The main HTML file for the chatbot interface.
- `static/css/styles.css`: Custom CSS for styling the chatbot.
- `static/js/script.js`: JavaScript for handling user interactions, AJAX requests, and speech functionality.
- `static/images/`: Contains user and bot avatars.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Chatbot-Project.git
   cd AI-Chatbot-Project
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to use the chatbot.

## Contributing

Feel free to fork this project and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
