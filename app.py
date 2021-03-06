import os, json, random
from flask import Flask
from flask import render_template, send_from_directory, Response, url_for, request

# app initialization
app = Flask(__name__)
app.config.update(
	DEBUG = True,
)

# controllers
@app.route('/')
def index():
	banner_repo_url = 'https://github.com/opennamesystem/opendig'
	return render_template('index.html', banner_repo_url=banner_repo_url)

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# error handlers
@app.errorhandler(404)
def page_not_found(e):
	return "404", 404

# server launchpad
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)