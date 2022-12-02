import requests
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

def test_create_pictures():
    url = 'http://127.0.0.1:8000/pictures/create'
    multipart_form_data = {
        'product_id': (None, 1),
        'file': ('test.jpeg', open(os.path.join(BASE_DIR, 'test_routers/images/test.jpeg'), 'rb')),
    }
    response = requests.post(url, files=multipart_form_data)
    assert response.status_code == 200

