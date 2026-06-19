# Medical-Insurance-Cost-Prediction-ML
# 🏥 Medical Insurance Cost Prediction using Machine Learning

![Medical Insurance](https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)

## 📌 Project Overview

This project predicts **medical insurance charges** based on personal information such as:

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region

A **Linear Regression Machine Learning model** is trained to estimate insurance costs.

---

# 🔄 Machine Learning Workflow

```
Data Collection
        ↓
Data Analysis
        ↓
Data Preprocessing
        ↓
Feature Encoding
        ↓
Train Test Split
        ↓
Linear Regression Model Training
        ↓
Model Evaluation
        ↓
Insurance Cost Prediction
```

---

# 📂 Dataset

Dataset contains **1338 records** and **7 columns**

Features:

| Feature | Description |
|-|-|
| age | Age of person |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of children |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance cost (Target) |

---

# 📊 Exploratory Data Analysis

## Age Distribution

![Age Distribution](age%20vs%20count.png)

---

## Gender Distribution

![Gender Distribution](gender%20vs%20count.png)

---

## BMI Distribution

![BMI Distribution](BMI%20vs%20count.png)

---

## Smoker Analysis

![Smoker](smoker%20vs%20count.png)

---

## Region Analysis

![Region](region%20vs%20count.png)

---

## Children Analysis

![Children](children%20vs%20count.png)

---

## Insurance Charges Distribution

![Charges](charge%20vs%20count.png)

---

# 🧹 Data Preprocessing

Categorical variables were converted into numerical values.

### Gender Encoding

```
male → 0
female → 1
```

### Smoker Encoding

```
yes → 0
no → 1
```

### Region Encoding

```
southeast → 0
southwest → 1
northeast → 2
northwest → 3
```

---

# 🤖 Machine Learning Model

Algorithm Used:

## Linear Regression

Linear Regression learns the relationship between input features and insurance charges.

---

# 📈 Model Evaluation

Dataset split:

```
Training Data : 80%
Testing Data  : 20%
```

### Results:

Training R² Score:

```
0.7515
```

Testing R² Score:

```
0.7447
```

The model explains approximately **74% of the variation** in insurance charges.

---

# 🔮 Prediction System

Example Input:

```
Age = 31
Sex = Female
BMI = 25.74
Children = 0
Smoker = No
Region = Southeast
```

Prediction:

```
THE INSURANCE COST IN USD: 3760.08
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

# 📁 Project Structure

```
Medical-Insurance-Cost-Prediction-ML

│
├── Medical Insurance Cost prediction.py
│
├── insurance.csv
│
├── README.md
│
├── age vs count.png
├── gender vs count.png
├── BMI vs count.png
├── smoker vs count.png
├── children vs count.png
├── region vs count.png
└── charge vs count.png

```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/allen745/Medical-Insurance-Cost-Prediction-ML.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run project:

```bash
python "Medical Insurance Cost prediction.py"
```

---

# 📌 Future Improvements

- Add Random Forest Regression
- Add XGBoost model
- Create Web Application using Streamlit
- Deploy ML model using Flask/API
- Add better feature engineering

---

# 👨‍💻 Author

**Allen Christian**

Machine Learning Project 🚀
