from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    video_url = request.form['video_url']
    return render_template('play.html', video_url=video_url)

@app.route('/stream/<path:video_url>')
def stream(video_url):
    headers = {'Range': request.headers.get('Range', '')}
    response = requests.get(video_url, headers=headers, stream=True)

    def generate():
        for chunk in response.iter_content(chunk_size=1024):
            yield chunk

    return Response(generate(), content_type=response.headers['content-type'])

if __name__ == '__main__':
    app.run(port=8000)
