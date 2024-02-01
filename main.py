"""
This is a Flask application that streams video content from a provided URL.

The application has three routes:

1. `/` - The index route that renders the `index.html` template.
2. `/play` - This route accepts POST requests with a `video_url` parameter in the form data. It renders the `play.html` template with the provided `video_url`.
3. `/stream/<path:video_url>` - This route streams the video content from the provided `video_url`. It uses the `Range` header from the request to stream the video in chunks.

The application uses the `requests` library to make HTTP requests and Flask's `Response` object to stream the video content.

The application is started by running the `main.py` script, which prompts the user to enter the host and port for the server.
"""

from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)
session = requests.Session()  # Create a Session object to reuse the TCP connection

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    """
    Render the play page with the provided video URL.

    The video URL is provided in the form data of the POST request.
    """
    video_url = request.form['video_url']
    return render_template('play.html', video_url=video_url)

@app.route('/stream/<path:video_url>')
def stream(video_url):
    """
    Stream the video content from the provided URL.

    The video is streamed in chunks of 1024 bytes. The `Range` header from the request is used to request specific parts of the video.
    """
    headers = {'Range': request.headers.get('Range', '')}
    response = session.get(video_url, headers=headers, stream=True)

    def generate():
        """Generate the video content in chunks."""
        for chunk in response.iter_content(chunk_size=1024):
            yield chunk

    return Response(generate(), content_type=response.headers['content-type'])

if __name__ == '__main__':
    host = str(input("Host: "))  # Prompt the user to enter the host
    port = int(input("Port: "))  # Prompt the user to enter the port
    app.run(host=host ,port=port)