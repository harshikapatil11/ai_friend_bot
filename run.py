from app import create_app
from app_config import Config  # Import the Config class

app = create_app(Config)  # Pass the Config class

if __name__ == "__main__":
    app.run(debug=True)
