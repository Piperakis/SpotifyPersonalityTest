import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect, render_template
from query import query_llama
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure using environment variables
app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = os.getenv('FLASK_SECRET_KEY')
TOKEN_INFO = 'token_info'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=url_for('redirect_page', _external=True),
        scope='user-top-read playlist-modify-public'
    )

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():  
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('PredictPersonality'))

@app.route('/PersonalityResults')
def PredictPersonality():
    try:
        token_info = get_token()
    except:
        return redirect('/')

    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    top_tracks = sp.current_user_top_tracks(limit=25, time_range='long_term')['items']
    
    if not top_tracks:
        return render_template('error.html', message="No top tracks found. Listen to more music!")

    formatted_tracks = []
    for track in top_tracks:
        formatted_tracks.append({
            'name': track['name'],
            'artists': [artist['name'] for artist in track['artists']]
        })

    prediction = query_llama(" ".join([f"{i+1}. {t['name']}" for i, t in enumerate(formatted_tracks)]))
    
    formatted_prediction = prediction.replace('\n', '<br>').replace('•', '•')

    return render_template('results.html', 
                         prediction=formatted_prediction,
                         tracks=formatted_tracks)

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        return redirect(url_for('login'))

    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60

    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
        session[TOKEN_INFO] = token_info

    return token_info

if __name__ == '__main__':
    app.run(debug=True)