from flask import Flask, render_template, url_for

TITLE = "YaLycGames"


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title=TITLE, cssFile=url_for('static', filename='css/style.css'))


@app.route('/company/<companyname>')
def company(companyname):
    return render_template('company.html',
                           title=f"{companyname} - on {TITLE}",
                           logoPic=url_for("static", filename="images/test_logo.png"),
                           cssFile=url_for("static", filename="css/style.css"),
                           companyname=companyname)


if __name__ == '__main__':
    app.run()
