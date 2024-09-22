from flask import Flask, render_template, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/redirected/<redirect>')
def redirected(redirect):
    return render_template("redirected.html", redir=redirect)

@app.route('/meta')
def meta():
    return render_template("redirect.html", usemeta=True, usejavascript=False)

@app.route('/java')
def javascript():
    return render_template("redirect.html", usejavascript=True, usemeta=False)

@app.route('/code/<int:code>')
def doCode(code):
    response = make_response()
    response.headers['location'] = url_for('redirected', redirect=code)
    response.status = code
    return response


if __name__ == '__main__':
    app.run()
