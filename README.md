# 🎓 Student Performance Predictor

A Machine Learning project that predicts whether a student is likely to **pass or struggle** based on study habits and personal factors.

---
## 📌 Problem Statement

Many students struggle academically, and identifying them early can help provide timely support.

This project builds a Machine Learning model to:
- Predict student performance
- Identify at-risk students
- Assist in educational decision-making

---

## 📊 Dataset

- Source: UCI / Kaggle Student Performance Dataset
- Total Records: 395 students
- Features include:
  - Study time
  - Past failures
  - Absences
  - Desire for higher education
  - Family and social factors

---

## 🧠 Machine Learning Approach

### 🔹 Target Variable
- `1` → Student likely to pass  
- `0` → Student may struggle  

---

## ⚙️ Models Used

- Logistic Regression ✅ (Final Model)
- Decision Tree (for comparison)
- Random Forest (for experimentation)

---

## 📈 Key Learnings

- ❌ Avoided **data leakage** (removed G1, G2)
- ⚖️ Handled **feature selection**
- 📉 Observed **underfitting & overfitting**
- 🔍 Compared multiple models

---

## 🏆 Final Model

- Model: Logistic Regression
- Accuracy: ~73%
- Reason:
  - Better generalization
  - Works well on small datasets
  - Avoids overfitting

---

## 🎯 Features Used in Final Model

- Study Time
- Past Failures
- Absences
- Higher Education Aspiration

---

## 💻 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---
