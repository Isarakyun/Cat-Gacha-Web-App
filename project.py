from flask import Flask, render_template, flash
import random

app = Flask(__name__)

cats = ['Cat 1 - 5 star', 'Cat 2 - 4 star', 'Cat 3 - 4 star', 'Cat 4 - 4 star', 'Cat 5 - 4 star', 'Cat 6 - 4 star', 'Cat 7 - 3 star', 'Cat 8 - 3 star', 'Cat 9 - 3 star', 'Cat 10 - 3 star', 'Cat 11 - 3 star', 'Cat 12 - 3 star', 'Cat 13 - 3 star', 'Cat 14 - 3 star', 'Cat 15 - 3 star']
total_coins = 100

@app.route('/')
def main():
    return render_template('index.html')

# player budget
def coins_left(coin):
    global total_coins
    total_coins -= coin
    return total_coins

@app.context_processor
def inject_total_coins():
    return dict(total_coins=total_coins)

# 1 pull
@app.route('/gacha_1')
def gacha_one_pull():
    if total_coins < 1:
        flash('Not enough coins to do a single pull', 'warning')
        return render_template('index.html', total_coins=total_coins)
    pulls = random.choices(cats, weights=[1, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20], k=1)
    coins = coins_left(1)
    return render_template('result.html', pulls=pulls, total_coins=coins)

# 5 pulls
@app.route('/gacha_5')
def gacha_five_pulls():
    if total_coins < 5:
        flash('Not enough coins to do 5 pulls', 'warning')
        return render_template('index.html', total_coins=total_coins)
    pulls = random.choices(cats, weights=[1, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20], k=5)
    coins = coins_left(5)
    return render_template('result.html', pulls=pulls, total_coins=coins)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)