# The Elephant Story - Interactive Adventure

This project is a Flask-based interactive adventure game where players make choices that shape their journey through a mysterious cave. Players take on the role of an elephant exploring various paths, discovering hidden treasures, and encountering challenges.

## Features

- **Interactive Storyline**: Players navigate through a richly detailed story with multiple choices and outcomes.
- **Session Management**: The game keeps track of player choices and items collected (like keys) using Flask sessions.
- **Error Handling**: Comprehensive error handling with custom messages for different HTTP errors.
- **Responsive Design**: The game interface is designed to work on multiple screen sizes with CSS styling.

## Getting Started

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to [http://localhost:5000](http://localhost:5000)

## Game Structure

- **`map.json`**: Contains the story's structure, including text for each page and available choices.
- **`app.py`**: The main Flask application file that manages routes and handles game logic.
- **Templates**: HTML files located in the `templates/` directory to render the game pages.
- **Static Files**: CSS and JavaScript files for styling and functionality located in the `static/` directory.

## Customization

Feel free to modify the `map.json` file to create new story paths and enhance the existing adventure. The game's structure is highly customizable, allowing you to introduce new characters, events, and settings.

## License

This project is licensed under the MIT License.

---

Enjoy your adventure as you explore the depths of the cave!