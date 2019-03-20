import flask

app = flask.Flask('app')


@app.route('/<int:a>')
def test(a):
    return f'''
    <a href='{a - 1}'>prev</a>
    <p>{a}</p>
    <a href='{a + 1}'>next</a>
    '''


app.run('127.0.0.1', '8888')
