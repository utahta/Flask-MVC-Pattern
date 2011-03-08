# vim:fileencoding=utf8
from flask import Flask
from myapp.controller.projects import projects

# Flask App
app = Flask(__name__)
app.secret_key = ';\x85\x0fd\x05\x96\xbf6`7nj\xb3\xc0U\xafF\xc5tL\xfdN\x93\xc8'

# Module
app.register_module(projects, url_prefix='/projects')

if __name__ == '__main__':
    app.run(debug=True)