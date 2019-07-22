from flask import url_for, render_template

from application import app
from application import scrap


@app.route('/')
def top_page():
    title = 'ようこそ日本語!!'
    msg = 'TEST 一覧ページ'
    return render_template('index.html', title = title, msg = msg)

@app.route('/list')
def show_list():
    title = "はてな人気リスト"
    results = scrap.get_hatena_entries('https://b.hatena.ne.jp/hotentry/it')
    return render_template('list.html', title = title, results = results)
