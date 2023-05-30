from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """
     The index page of the web application. This is used to display the home page of the web application.
     
     
     @return The template that renders the index page of the web application
    """
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    """
     View to play a video. Used by ajax calls. It is a static view and should not be accessed directly.
     
     
     @return The template for play. html with the video_url
    """
    video_url = request.form['video_url']
    return render_template('play.html', video_url=video_url)

@app.route('/stream/<path:video_url>')
def stream(video_url):
    """
     Streams a video to be played. This is a generator function that yields chunks of video data.
     
     @param video_url - The URL of the video to stream.
     
     @return A : class : ` Response ` object with the stream
    """
    headers = {'Range': request.headers.get('Range', '')}
    response = requests.get(video_url, headers=headers, stream=True)

    def generate():
        """
         Generator that yields chunks of response content. Useful for tests that don't need to iterate over a file
        """
        # Yields chunks of data from the response.
        for chunk in response.iter_content(chunk_size=1024):
            yield chunk

    return Response(generate(), content_type=response.headers['content-type'])

# Run the app if __main__ is called.
if __name__ == '__main__':
    app.run(port=8000)
