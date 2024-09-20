from flask import Flask, request, render_template
from model import Model


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = int(request.form['dependents'] or 0)
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'] or 0)
        coapplicant_income = float(request.form['coapplicant_income'] or 0)
        loan_amount = float(request.form['loan_amount'] or 0)
        loan_amount_term = float(request.form['loan_amount_term'] or 0)
        credit_history = float(request.form['credit_history'] or 0)
        property_area = request.form['property_area']
        total_income = applicant_income + coapplicant_income
        loan_amt_income_ratio = loan_amount / total_income

        # Make the prediction
        model_inputs = [gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area, total_income, loan_amt_income_ratio]
        prediction = Model().predict(model_inputs)

        # Return the result along with the form
        return render_template('home.html', prediction=prediction)

    # If it's a GET request, just render the form
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
