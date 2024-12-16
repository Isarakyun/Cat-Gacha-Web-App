from flask import Flask, render_template, flash, redirect, url_for, jsonify
import random
import threading
import time

app = Flask(__name__, template_folder='project/templates', static_folder='project/static')
# to do flash messages, secret key is needed
app.secret_key = 'nyannyanchan'

cats = ['5_star_cat.png', '4_star_cat.png', '4_star_cat_2.png', '4_star_cat_3.png', '4_star_cat_4.png', '4_star_cat_5.png', '3_star_cat.png', '3_star_cat_2.png', '3_star_cat_3.png', '3_star_cat_4.png', '3_star_cat_5.png', '3_star_cat_6.png', '3_star_cat_7.png', '3_star_cat_8.png', '3_star_cat_9.png']
obtained_cats = []
total_coins = 100
coins_reset_countdown = None

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/collections')
def collections():
    return render_template('collections.html', cats=cats, obtained_cats=obtained_cats)

# player budget
total_coins = 100
coins_reset_countdown = None
def coins_left(coin):
    global total_coins, coins_reset_countdown
    total_coins -= coin
    """
    so the logic here is that:
    when total_coins == 0
    coins_reset_countdown = current time + 60 seconds (countdown time)
    the threading library is used to start the countdown
    """
    if total_coins <= 0:
        total_coins = 0
        coins_reset_countdown = time.time() + 60
        threading.Thread(target=reset_coins).start()
    return total_coins

# reset coins to 100 after 60 seconds
def reset_coins():
    global total_coins, coins_reset_countdown
    time.sleep(60)
    total_coins = 100
    coins_reset_countdown = None
    return total_coins, coins_reset_countdown

# so that total_coins (global variable) can be shown anywhere (i put it in base.html)
@app.context_processor
def inject_total_coins():
    return dict(total_coins=total_coins)

# the countdown for resetting coins every 60 seconds when total_coins == 0
@app.route('/get_countdown')
def get_countdown():
    global coins_reset_countdown, total_coins
    if coins_reset_countdown:
        countdown = int(coins_reset_countdown - time.time())
        return jsonify({'countdown': countdown, 'total_coins': total_coins})
    return jsonify({'countdown': 0, 'total_coins': total_coins})

# 1 pull
@app.route('/gacha_1')
def gacha_one_pull():
    if total_coins < 1:
        flash('Not enough coins to do a single pull', 'warning')
        return redirect(url_for('main'))
    pulls = random.choices(cats, weights=[1, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20], k=1)
    coins = coins_left(1)

    for pull in pulls:
        if pull not in obtained_cats:
            obtained_cats.append(pull)

    return render_template('result.html', pulls=pulls, total_coins=coins)

# 5 pulls
@app.route('/gacha_5')
def gacha_five_pulls():
    if total_coins < 5:
        flash('Not enough coins to do 5 (five) pulls', 'warning')
        return redirect(url_for('main'))
    pulls = random.choices(cats, weights=[1, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20], k=5)
    coins = coins_left(5)

    for pull in pulls:
        if pull not in obtained_cats:
            obtained_cats.append(pull)
            
    return render_template('result.html', pulls=pulls, total_coins=coins)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)