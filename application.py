from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='POST':
        
        data = CustomData(
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=(request.form.get("cut")),
            color=(request.form.get("color")),
            clarity = request.form.get('clarity')
        )           
        new_data = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict_for_new_data(new_data)

        result = round(pred[0], 2)

        return render_template("form.html", final_result = result)
    else:
        return render_template('form.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)

    # python application.py
    # http://127.0.0.1:5000/predict
    # localhost:5000