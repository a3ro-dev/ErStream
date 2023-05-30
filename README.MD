# ErStream

ErStream is a Flask-based web application that allows you to stream videos directly in your browser. Simply input a video URL, and ErStream will load the video into a web player for seamless streaming.

## Features

- Stream videos directly from provided URLs in your web browser.
- Utilizes HTML5 video tags and JavaScript for smooth playback.
- Prevents unauthorized use by not allowing the application to be utilized for piracy or illegal activities.
- Simple and user-friendly interface.

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/a3ro-dev/ErStream
   ```

2. Navigate to the project directory:

   ```shell
   cd ErStream
   ```

3. Install the required dependencies. It is recommended to use a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   .\venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

4. Run the application:

   ```shell
   python main.py
   ```

5. Open your browser and visit `http://localhost:8000`.

6. Enter the video URL in the provided form and click "Play". The video will start streaming in the web player.

**Note: Do not use this application for piracy or any illegal activities. Respect copyright laws and use it responsibly.**

## License

The ErStream project is licensed under the [MIT License](LICENSE).

## Disclaimer

ErStream is intended for personal use and educational purposes only. The developers of ErStream do not endorse or promote any form of piracy or illegal activities. Users are responsible for complying with local laws and respecting intellectual property rights when using this application.

## Contributing

Contributions are welcome! If you would like to contribute to ErStream, please fork the repository and submit a pull request with your proposed changes.

## Support

If you encounter any issues or have any questions or suggestions, please [open an issue](https://github.com/a3ro-dev/ErStream/issues) on GitHub.

## Acknowledgments

- ErStream was inspired by the need for a simple and efficient video streaming solution.
- Special thanks to the Flask and HTML5 communities for their invaluable resources and documentation.

## Related Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [HTML5 Video Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)

## Need a video download URL?

If you are looking for a movie, try searching on Google using the following format:

```
index for {movie name}
```

Look for the search results that mention an "index" or a directory structure. Once you find the relevant download link, you can paste it into ErStream for streaming.
