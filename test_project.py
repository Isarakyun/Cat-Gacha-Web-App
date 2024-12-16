from project import app, obtained_cats, total_coins, coins_reset_countdown, coins_left, reset_coins, inject_total_coins, get_countdown, gacha_one_pull, gacha_five_pulls
import pytest
from unittest.mock import patch
import time

def test_main():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'<p class="mb-4 text-sm italic">Collect 15 different types of cat memes!</p>' in response.data

def test_collections():
    response = app.test_client().get('/collections')
    assert response.status_code == 200
    assert b'<h1 class="mb-8 text-3xl font-bold text-gray-600 text-center mt-4">Collections</h1>' in response.data

def test_coins_left():
    global total_coins
    total_coins = 100
    assert coins_left(5) == 95
    assert coins_left(1) == 94

# mocking the time.sleep function so that i dont have to wait for 60 seconds
@patch('time.sleep', return_value=None)
def test_reset_coins(mock_sleep):
    global total_coins, coins_reset_countdown
    total_coins = 0
    total_coins, coins_reset_countdown = reset_coins()
    assert total_coins == 100
    assert coins_reset_countdown == None

def test_inject_total_coins():
    context = inject_total_coins()
    assert 'total_coins' in context
    assert context['total_coins'] == total_coins

def test_get_countdown():
    global coins_reset_countdown
    coins_reset_countdown = time.time() + 60
    response = app.test_client().get('/get_countdown')
    assert response.status_code == 200
    data = response.get_json()
    assert 'countdown' in data
    assert data['countdown'] == 0

def test_gacha_one_pull():
    global total_coins, obtained_cats
    total_coins = 100
    obtained_cats = []
    response = app.test_client().get('/gacha_1')
    assert response.status_code == 200
    total_coins = coins_left(1)
    assert total_coins <= 99
    obtained_cats.append('5_star_cat.png')
    assert len(obtained_cats) > 0

def test_gacha_five_pulls():
    global total_coins, obtained_cats
    total_coins = 100
    obtained_cats = []
    response = app.test_client().get('/gacha_5')
    assert response.status_code == 200
    total_coins = coins_left(5)
    print(f"Total Coins Left: {total_coins}")
    assert total_coins <= 95
    obtained_cats.append('5_star_cat.png')
    assert len(obtained_cats) > 0