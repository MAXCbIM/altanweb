from flask import Flask, render_template, request
from pwdGenerator import hashing

app = Flask(__name__)

# print(__name__)

@app.route("/")
def index_page():
	return render_template("home.html")

@app.route("/product", methods=["GET", "POST"])
def product_page():
	msg = ""
	if request.method == "POST":
		name = request.form.get("salt")
		pwd = request.form.get("pwd")
		num_char = request.form.get("num_char")

		if pwd:
			raw_pwd = pwd + salt

			if num_char == '-':
				int_num_char = 0

			msg = hashing(raw_pwd, int(num_char))

	return render_template("product.html", msg=msg)

# http://127.0.0.1:5000/test?v1=hello&v2=1234
@app.route("/test")
def test_page():
	var_1 = request.args.get("v1")
	return f"""
	<h3>Test</h3>
	<p> Var 1: {var_1} </p>
	"""

# точка входа
if __name__ == "__main__":
	app.run(debug=True)