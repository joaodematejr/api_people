from routes import Routes

from flask import Flask, request, json
app = Flask(__name__)

routes = Routes()


@app.route('/user/', methods=['POST'])
def post_user():
    response = routes.user_create(request)
    return response


if __name__ == '__main__':
    app.run()
    use_debugger = True
    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
