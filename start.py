from flask import Flask, render_template, request, redirect
from crop import search_crop 
from pdf_gen import make_pdf_from_url
import wikipedia

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/submit")
def result():
	data = request.args
	data_dict = {key:val for key, val in data.items()}
	for key in data_dict:
		data_dict[key] = int(data_dict[key])
	result = search_crop(data_dict)
	image_link = '/static/'+ result.lower() + '.jpg'
	crop_summary = wikipedia.summary(result, sentences=5)
	return render_template('crop.html', crop=result, summary = crop_summary, image_link=image_link)

@app.route("/crop/<crop_name>")
def crop(crop_name):
	image_link = '/static/'+ crop_name.lower() + '.jpg'
	crop_summary = wikipedia.summary(crop_name, sentences=5)
	return render_template('crop.html', crop=crop_name, summary = crop_summary, image_link=image_link)


@app.route("/report/<crop_name>")
def gen_pdf(crop_name):
	url = 'http://deepanshurautela.pythonanywhere.com/crop/' + crop_name.lower()
	return redirect(make_pdf_from_url(url))


if __name__ == "__main__":
	app.run(debug = True)