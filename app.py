from flask import Flask, render_template, url_for
from flask_login import login_required, LoginManager
from models import db, User
from flask_migrate import Migrate
from auth.views import auth_bp       # authは「authentication」の略。日本語に訳すと「認証」。
import MySQLdb

app = Flask(__name__)

# config.py読み込み
app.config.from_object("config.Config")
# データベースとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ（Flaskとdb）
migrate = Migrate(app, db)
# LoginManagerインスタンス
login_manager = LoginManager()
# LoginManagerとの紐づけ
login_manager.init_app(app)
# ログインが必要なページにアクセスしようとしたときに表示されるメッセージ
login_manager.login_message = "認証していません：ログインしてください"
# 未認証のユーザーがアクセスしようとした際に
# リダイレクトされる関数名を設定する
login_manager.login_view = "auth.login"

# Blueprintをアプリケーションに登録
app.register_blueprint(auth_bp)

@login_manager.user_loader   #ユーザー情報を読み込む関数として「Flask-Login」に登録
def load_user(user_id):
    return User.query.get(int(user_id))    #user_idに対応するユーザー情報を取得




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle')
<<<<<<< HEAD
@login_required     #ログインしてたらゲームのページに行けるよう設定
=======
#@login_required     #ログインしてたらゲームのページに行けるよう設定
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def puzzle():
    return render_template('game/15puzzle.html')

@app.route('/Shooting')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def Shooting():
    return render_template('game/Shooting.html')

@app.route('/Cards')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def Cards():
    return render_template('game/FlipCards.html')

@app.route('/reversi')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def Reversi():
    return render_template('game/ReversiblePiece.html')

@app.route('/Dungeon')
@login_required 
def Dungeon():
    return render_template('game/Dungeon.html')

@app.route('/FunkyBlocks')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def FunkyBlocks():
    return render_template('game/FunkyBlocks.html')

@app.route('/Jumper')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def Jumper():
    return render_template('game/jumper.html')

@app.route('/CarryIt')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def CarryIt():
    return render_template('game/CarryIt.html')

@app.route('/saturnvoyager')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def saturnvoyager():
    return render_template('game/saturnvoyager.html')

@app.route('/EggCatch')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def EggCatch():
    return render_template('game/EggCatch.html')

@app.route('/chase')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def chase():
    return render_template('game/Chase.html')

@app.route('/Billiard')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def Billiard():
    return render_template('game/Billiard.html')

@app.route('/yasai')
<<<<<<< HEAD
@login_required 
=======
#@login_required 
>>>>>>> 40481eada68ce37bfe632a6b06b28dd8bc29040a
def yasai():
    return render_template('game/yasai.html')

if __name__ == '__main__':
    app.run()
    #公開サーバー用↓
    #   app.run(debug=False, host='192.168.1.108', port=50004)