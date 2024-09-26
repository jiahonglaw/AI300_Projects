import joblib


class Model:
    
    def __init__(self):
        self.threshold = 0.5
        self.model = self._load('model/catboost_model.pkl')

    def _load(self, model_file_path):
        return joblib.load(model_file_path)

    def predict(self, input_features):
        probability = self.model.predict_proba(input_features)[1]
        return probability
