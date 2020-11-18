from flask import Flask, render_template, url_for, request
import subprocess


T = ["INFO", "LEXEM", "ERROR", "STATUS", "TW", "TD", "TID", "TNUM"]
app = Flask(__name__)



@app.route("/", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		textin = request.form.get('INPUT')
		text = subprocess.Popen(['Test3.exe', textin.replace('\r\n', '_')], stdout=subprocess.PIPE)
		decode_text = text.stdout.read().decode('cp1251')
		# modifier_text_mas = [i.split('\r\n') for i in map(str.strip, decode_text.split("-----"))]
		modifier_text_mas = list(map(str.lstrip, decode_text.replace("\r","").split("-----")))
		ictT = {k:v for k,v in zip(T, modifier_text_mas)}
		return render_template("index.html", LEXEM=[ictT["LEXEM"], ictT["ERROR"],ictT["STATUS"]], TW=ictT["TW"], TD=ictT["TD"], TID=ictT["TID"], TNUM=ictT["TNUM"], INPUT=textin)
		
	return render_template("index.html")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')


if __name__ == "__main__":
	app.run(debug=True)
