# breast-cancer
This is about calculating accuracy of model using breast cancer dataset.
Perfect! Here’s a **professional, recruiter-friendly README** you can use for your GitHub repo:

---

# Breast Cancer Prediction API

A Flask-based web application that predicts whether a breast tumor is **Benign** or **Malignant** using a **Random Forest Machine Learning model**.

**Live Demo:** [https://breast-cancer-hvjw.onrender.com/](https://breast-cancer-hvjw.onrender.com/)

---

## Features

* User-friendly web form to input tumor features
* Real-time prediction of **Benign / Malignant**
* Returns prediction probability
* Built with **Python, Flask, NumPy, scikit-learn**
* Deployed live on **Render** using **Gunicorn**

---

## Technologies

* Python 3
* Flask
* scikit-learn
* NumPy
* Gunicorn
* Render (cloud deployment)

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/kinza20/breast-cancer.git
cd breast-cancer
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open a browser and visit:

```
http://127.0.0.1:5000
```

---

## API Endpoint

**POST** `/predict`

* Content-Type: `application/json`
* Body Example:

```json
{
  "mean radius": 14.2,
  "mean texture": 20.1,
  ...
}
```

* Response Example:

```json
{
  "prediction": 0,
  "probability": [0.85, 0.15]
}
```

> 0 = Benign, 1 = Malignant

---

## Notes

* The model is trained on the **Breast Cancer Wisconsin dataset**.
* Deployed using **Render** in a production-ready environment.

---


Do you want me to do that next?
