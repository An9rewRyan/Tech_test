import requests

def test_create_reviews():
    url = 'http://127.0.0.1:8000/reviews/create'
    review = {'username': 'admin', 'content': 'This chair is cool as fuck, i like it!', 'product_id': '1', 'rating':5}
    response = requests.post(url, json = review)
    assert response.status_code == 200