from flask import Flask, render_template, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html", infinite=False)

@app.route('/redirected/<redirect>')
def redirected(redirect):
    return render_template("redirected.html", redir=redirect)

@app.route('/meta/<int:inf>')
def meta(inf):
    return render_template("redirect.html", usemeta=True, usejavascript=False, inf=inf)

@app.route('/java/<int:inf>')
def javascript(inf):
    return render_template("redirect.html", usejavascript=True, usemeta=False, inf=inf)

@app.route('/code/<int:code>/<int:inf>')
def doCode(code, inf):
    response = make_response()
    if inf:
        response.headers['location'] = url_for('doCode', code=code, inf=1)
    else:
        response.headers['location'] = url_for('redirected', redirect=code)
    response.status = code
    return response

@app.route('/infinite')
def infinite():
    return render_template("index.html", infinite=1)


if __name__ == '__main__':
    app.run()
