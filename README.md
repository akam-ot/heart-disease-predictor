# ❤️ Heart Disease Predictor (Streamlit App)

This is a simple machine learning web app built with **Streamlit** that predicts whether a person is likely to have heart disease based on clinical features.

The model is trained on the [Heart Failure Prediction Dataset by fedesoriano](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).

---

## 🚀 Live Demo

🌐 **Try the app:** [https://heart-disease-predictor-qnq4ejeepsrgtb8x3e9hf6.streamlit.app](https://heart-disease-predictor-qnq4ejeepsrgtb8x3e9hf6.streamlit.app)

---

## 🧠 Model Info

* **Model used:** Support Vector Machine (SVM with RBF kernel)
* **Accuracy:** \~89.7%
* **Preprocessing:** One-hot encoding + StandardScaler
* **Class balancing:** SMOTE (Synthetic Minority Oversampling)

---

## 📥 Input Features

The app takes the following user inputs:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar > 120
* Resting ECG
* Maximum Heart Rate Achieved
* Exercise-induced Angina
* ST Depression (Oldpeak)
* ST Slope

---

## 📦 Files in this Repo

| File                             | Description                   |
| -------------------------------- | ----------------------------- |
| `app.py`                         | Main Streamlit app            |
| `requirements.txt`               | Python dependencies           |
| `svm_heart_disease_model.joblib` | Trained SVM model             |
| `preprocessor.joblib`            | Fitted preprocessing pipeline |

---

## ✅ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/akam-ot/heart-disease-predictor.git
cd heart-disease-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📄 License

MIT License

---

## 🤝 Acknowledgements

* Dataset by [fedesoriano on Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
* Built using Scikit-learn, Streamlit, and SMOTE (imbalanced-learn)
