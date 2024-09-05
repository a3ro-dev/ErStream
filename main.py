"""
This is a Flask application that streams video content from a provided URL.

The application has three routes:

1. `/` - The index route that renders the `index.html` template.
2. `/play` - This route accepts POST requests with a `video_url` parameter in the form data. It renders the `play.html` template with the provided `video_url`.
3. `/stream/<path:video_url>` - This route streams the video content from the provided `video_url`. It uses the `Range` header from the request to stream the video in chunks.

The application uses the `requests` library to make HTTP requests and Flask's `Response` object to stream the video content.

The application is started by running the `main.py` script, which prompts the user to enter the host and port for the server.
"""

# main.py

from flask import Flask, render_template, request, Response
import requests
import os

app = Flask(__name__)

def get_session() -> requests.Session:
    """Create and return a Session object to reuse the TCP connection."""
    return requests.Session()

@app.route('/')
def index() -> str:
    """Render the index page."""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play() -> str:
    """
    Render the play page with the provided video URL.

    The video URL is provided in the form data of the POST request.
    """
    video_url = request.form['video_url']
    return render_template('play.html', video_url=video_url)

@app.route('/stream/<path:video_url>')
def stream(video_url: str) -> Response:
    """
    Stream the video content from the provided URL.

    The video is streamed in chunks of 1024 bytes. The `Range` header from the request is used to request specific parts of the video.
    """
    session = get_session()
    headers = {'Range': request.headers.get('Range', '')}
    response = session.get(video_url, headers=headers, stream=True)

    def generate():
        """Generate the video content in chunks."""
        try:
            for chunk in response.iter_content(chunk_size=1024):
                yield chunk
        except requests.RequestException as e:
            app.logger.error(f"Error streaming video: {e}")
            yield b''

    return Response(generate(), content_type=response.headers.get('content-type', 'application/octet-stream'))

if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')  # Use environment variable or default to '127.0.0.1'
    port = int(os.getenv('FLASK_RUN_PORT', 5000))  # Use environment variable or default to 5000
    app.run(host=host, port=port)