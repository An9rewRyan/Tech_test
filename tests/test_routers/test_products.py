import requests
import pytest

def test_create_products():
    url = 'http://127.0.0.1:8000/products/create'
    product = {'name': 'test_chair', 'material': 'wood', 'price': 100.00,
               'category_id': 141, 'description': 'fine new chair from premium wood'}
    response = requests.post(url, json = product)
    assert response.status_code == 200

def test_get_product_extended():
    url = 'http://127.0.0.1:8000/products/get/1?extended=True'
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize("url",[('http://127.0.0.1:8000/products/get'), #Без параметров
                                ('http://127.0.0.1:8000/products/get?limit=10'), #С параметром на пагинацию
                                #Фильтрация по первым двум категориям и сортировка по рейтингу
                                ('http://127.0.0.1:8000/products/get?category=1&order_by=rating'),
                                #Фильтрация по первым двум категориям и сортировка по цене
                                ('http://127.0.0.1:8000/products/get?category=1&order_by=price')
                        ])
def test_get_all_products(url: str):
    response = requests.get(url)
    assert response.status_code == 200






    
