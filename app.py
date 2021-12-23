from flask import Flask, render_template, request

app = Flask(__name__)

# print(__name__)

@app.route("/")
def index_page():
	return render_template("home.html")

@app.route("/product", methods=["GET", "POST"])
def product_page():
	msg = ""
	name = ""
	pwd = ""
	if request.method == "POST":
		name = request.form.get("name")
		pwd = request.form.get("pwd")

		msg = f"{name} {pwd}"

	return render_template("product.html", msg=msg, n=name, p=pwd)

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