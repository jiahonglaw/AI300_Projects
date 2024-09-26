# Capstone Customer Churn Prediction Model - Final
GitHub Capstone Project for AI300 - Customer Churn Prediction

## Name
Law Jia Hong (Project Group p04 - Aug-Sep24 Heicoders Batch)

## Website URL of deployed web app
https://ec2-52-62-117-23.ap-southeast-2.compute.amazonaws.com/

https://52.62.117.23/

## Info on final chosen model and parameters

We went with a catboost model with the following features and parameters after doing hyperparameter tuning via GridSearch CV and feature selection via np.array

Model algorithm used: CatBoostClassifier
Parameters used: (learning_rate= 0.01, depth=3, random_state=5)
Features selected: ['avg_long_distance_fee_monthly','total_refunds','tenure_months','num_referrals','total_charges_quarter','total_monthly_fee','has_phone_service','avg_gb_download_monthly']

Please refer to capstone_final.ipynb for the full notebook research done.

## Offline AUC metrics of Final chosen model

AUC is obtained by metrics.roc_auc_score.

AUC obtained: 0.8695043560160114

Completed 26 September 2024.# aug24-p04
# aug24-p04
# aug24-p04
