import pytest
import requests
from utils.config import Config

class TestAPI:
    def test_get_products(self):
        url = f"{Config.API_URL}/products"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        
        products = response.json()
        assert len(products) > 0, "No products returned"
        assert "id" in products[0], "Product object does not contain id"
        assert "title" in products[0], "Product object does not contain title"
        
    def test_get_single_product(self):
        product_id = 1
        url = f"{Config.API_URL}/products/{product_id}"
        response = requests.get(url)
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        
        product = response.json()
        assert product["id"] == product_id, f"Expected product ID {product_id}, got {product['id']}"
        assert product["title"] is not None, "Product title is empty"
        
    def test_auth_login(self):
        url = f"{Config.API_URL}/auth/login"
        payload = {
            "username": "mor_2314",
            "password": "83r5^_"
        }
        response = requests.post(url, json=payload)
        assert response.status_code in [200, 201], f"Expected 200 OK, got {response.status_code}"
        
        token = response.json().get("token")
        assert token is not None, "Auth token not returned"
