# Spotify Personality Test  

## Overview  
The **Spotify Personality Test** is a web application that analyzes a user's top Spotify tracks and generates a personality prediction based on music psychology. Using the Spotify API and an AI model (LLaMA 3), this project correlates musical preferences with personality traits using the Big Five OCEAN model.  

## Features  
- Spotify authentication to access user listening history  
- AI-based personality analysis using music psychology  
- Personalized insights based on the user's music taste  
- Simple and interactive web interface  

## Technologies Used  
- **Python (Flask)** – Backend web framework  
- **Spotify API** – Fetching user listening history  
- **Spotipy** – Python wrapper for Spotify API  
- **Ollama** – Running the LLaMA 3 AI model locally  
- **HTML, CSS (Jinja Templates)** – Frontend rendering  
- **dotenv** – Secure environment variable management  

## Setup & Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/spotify-personality-test.git
cd spotify-personality-test
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv  
source venv/bin/activate  # On Windows use: venv\Scripts\activate  
pip install -r requirements.txt  
```

### 3. Set Up Environment Variables
Create a .env file in the project root and add the following credentials:
```bash
SPOTIPY_CLIENT_ID=your_spotify_client_id  
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret  
FLASK_SECRET_KEY=your_secret_key  
```

### 4.Run the application
```bash
flask run  
```