from flask import Flask, request, render_template
from model import Model


app = Flask(__name__)
## Method 1: HTML

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tenure_months = int(request.form['tenure_months'])
        total_monthly_fee = int(request.form['total_monthly_fee'])
        avg_long_distance_fee_monthly = int(request.form['avg_long_distance_fee_monthly'])
        total_refunds = int(request.form['total_refunds'])
        num_referrals = int(request.form['num_referrals'])
        total_charges_quarter = float(request.form['total_charges_quarter'] or 0)
        has_phone_service = float(request.form['has_phone_service'] or 0)
        avg_gb_download_monthly = float(request.form['avg_gb_download_monthly'] or 0)
        ## loan_amount_term = float(request.form['loan_amount_term'] or 0)
        # credit_history = float(request.form['credit_history'] or 0)
        # property_area = request.form['property_area']
        # total_income = applicant_income + coapplicant_income
        # loan_amt_income_ratio = loan_amount / total_income

        print([avg_long_distance_fee_monthly,total_refunds,tenure_months,num_referrals,total_charges_quarter,total_monthly_fee,has_phone_service,avg_gb_download_monthly])

        # Make the prediction
        model_inputs = [avg_long_distance_fee_monthly,total_refunds,tenure_months,num_referrals,total_charges_quarter,total_monthly_fee,has_phone_service,avg_gb_download_monthly]
        prediction = Model().predict(model_inputs)
        print(model_inputs)
        print(prediction)

        # Return the result along with the form
        return render_template('home.html', prediction=prediction)

    # If it's a GET request, just render the form
    return render_template('home.html')

## Method 2: Json API Predict

@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    tenure_months = int(request_data['tenure_months'])
    total_monthly_fee = int(request_data['total_monthly_fee'])
    avg_long_distance_fee_monthly = int(request_data['avg_long_distance_fee_monthly'])
    total_refunds = int(request_data['total_refunds'])
    num_referrals = int(request_data['num_referrals'])
    total_charges_quarter = float(request_data['total_charges_quarter'] or 0)
    has_phone_service = float(request_data['has_phone_service'] or 0)
    avg_gb_download_monthly = float(request_data['avg_gb_download_monthly'] or 0)

    model_inputs = [avg_long_distance_fee_monthly,total_refunds,tenure_months,num_referrals,total_charges_quarter,total_monthly_fee,has_phone_service,avg_gb_download_monthly]

    prediction = Model().predict(model_inputs)
    print(model_inputs)
    print(prediction)


    return {'prediction': prediction}


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
