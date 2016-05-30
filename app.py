from flask import Flask, render_template, request, redirect, url_for
from collections import namedtuple

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/graph', methods=['Get', 'Post'])
def graph():
	cp = requests.form['cp']
	acp = requests.form['acp']
	op = requests.form['op']
	aop = requests.form['aop']
	Checkboxes = namedtuple('Checkboxes', 'cp acp op aop')
	cb = Checkboxes(cp=cp, acp=acp, op=op, aop=aop)
	ticker_name = requests.form['tckr']

	div, script = get_graph(get_data(ticker_name), cb, ticker_name)
	return render_template('graph.html', graph_div=div, graph_script=script, tckr=ticker_name)

if __name__ == '__main__':
	app.run(port=33507)
