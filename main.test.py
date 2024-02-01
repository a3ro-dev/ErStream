import pytest
from flask import Flask, request
from main import stream
from unittest.mock import patch, MagicMock

def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

def test_stream():
    app = create_test_app()

    with app.test_request_context('/stream/test_url'):
        with patch('main.session.get') as mock_get:
            mock_response = MagicMock()
            mock_response.iter_content.return_value = [b'test data']
            mock_response.headers = {'content-type': 'video/mp4'}
            mock_get.return_value = mock_response

            response = stream('test_url')

            assert request.path == '/stream/test_url'
            assert mock_get.called
            assert list(response.response) == [b'test data']
            assert response.content_type == 'video/mp4'