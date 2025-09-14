# 🍷 Wine Quality Predictor (Django REST + ML)

A simple machine learning project that predicts wine quality scores using the [UCI Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality).  
The model is trained with RandomForestClassifier algorithm and exposed via a Django REST API.

---

## 📌 Problem Statement
Train a ML model to predict wine quality score and expose an API endpoint `/wines/predict` that:
- Accepts wine chemical properties as JSON input.
- Returns the predicted quality score.

---

## 🚀 Features
- ML model trained with **RandomForestClassifier**.
- Model serialized and loaded in Django.
- Django REST Framework API with serializer validation.
- Example `curl` commands for testing.

---

## ⚙️ Tech Stack
- Python 3
- Django + Django REST Framework
- scikit-learn
- joblib (for model persistence)

---

## 📊 Dataset
The dataset is available [here](https://archive.ics.uci.edu/ml/datasets/wine+quality).  
It contains physicochemical properties of wines such as acidity, sugar, pH, etc., with a target variable **quality** (score 0–10).

---

## 🔧 Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/hisuperaman/wine-quality-predictor.git
   cd wine-quality-predictor
   ```

2. Create virtual environment & install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Train and save the model (save in models/ directory) by opening `jupyter` folder in `Jupyter Notebook`.

4. Run server:
   ```bash
   python manage.py runserver
   ```

---

## 📡 API Usage
**Endpoint:**  
`POST /wines/predict/`

**Sample Request:**
```bash
curl -X POST http://localhost:8000/wines/predict/ \
-H "Content-Type: application/json" \
-d '{
  "fixed_acidity": 6.5,
  "volatile_acidity": 0.2,
  "citric_acid": 0.3,
  "residual_sugar": 1.5,
  "chlorides": 0.05,
  "free_sulfur_dioxide": 15.0,
  "total_sulfur_dioxide": 35.0,
  "density": 0.995,
  "ph": 3.4,
  "sulphates": 0.65,
  "alcohol": 11.0
}'
```

**Sample Response:**
```json
{
    "data": {
        "quality": 6.0
    }
}
```
