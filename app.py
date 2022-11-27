from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/main")
def page():
    return render_template("mainpage.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    model = tf.keras.models.load_model('./predictor')
    lst = [int(x) for x in request.form.values()]
    final = np.array([lst])
    prediction = model.predict(final)
    output = prediction[0, 0]
    return render_template('mainpage.html',pred = "Predicted Rent :   Rs. " + str(int(output)))


if __name__ == "__main__":
    app.run(debug = True)
