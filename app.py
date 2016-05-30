from flask import Flask, render_template, request, redirect, url_for
from collections import namedtuple
from backend import get_graph, get_data

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/graph', methods=['Post'])
def graph():
	print request.form

	# cp = None
	# acp = None
	# op = None
	# aop = None

	cp = request.form.get('cp')
	acp = request.form.get('acp')
	op = request.form.get('op')
	aop = request.form.get('aop')
	Checkboxes = namedtuple('Checkboxes', 'cp acp op aop')
	cb = Checkboxes(cp=cp, acp=acp, op=op, aop=aop)
	ticker_name = request.form.get('tckr')
	script, div = get_graph(get_data(ticker_name), cb, ticker_name)
	return render_template('graph.html', graph_div=div, graph_script=script, ticker=ticker_name.upper())

if __name__ == '__main__':
	app.run(debug=True, port=33507)
