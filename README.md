# 📊 Smart Business Analytics & Sales Prediction System

A professional **Business Analytics and Machine Learning dashboard** built with **Python and Streamlit** to analyze sales performance, generate business insights, predict sales, segment customers, and identify customer churn risk.

---

## 🚀 Project Overview

The **Smart Business Analytics & Sales Prediction System** transforms business sales data into meaningful insights through interactive dashboards and machine learning models.

Users can upload a CSV dataset or use the project's default sales dataset, apply business filters, explore key performance indicators, visualize sales trends, and run machine learning models directly from the web interface.

---

## ✨ Key Features

### 📊 Business Dashboard

* Revenue and profit KPIs
* Monthly sales analysis
* Regional sales performance
* Category performance
* Top-selling products
* Interactive charts and visualizations

### 🤖 Sales Prediction

* Train a machine learning sales prediction model
* Compare actual and predicted sales
* View:

  * MAE
  * RMSE
  * R² Score
* Interactive actual vs. predicted sales visualization

### 👥 Customer Segmentation

* Segment customers based on behavioral metrics
* Adjustable number of customer segments
* Customer segmentation table
* Interactive customer segment visualization
* Frequency vs. Monetary analysis

### 🚨 Customer Churn Analysis

* Analyze customer inactivity/churn risk
* Run a churn prediction model
* Display model accuracy
* Identify customers with higher churn risk

### 💡 Business Insights

Automatically generates insights including:

* Latest-month sales change
* Highest-revenue category
* Highest-revenue region
* Top product by sales
* Overall profit margin

### 📋 Data Management

* Upload custom CSV datasets
* Clean and process data
* Apply Region and Category filters
* View the processed dataset
* Download the filtered data as CSV

---

## 🛠️ Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Core programming language    |
| Streamlit    | Interactive web dashboard    |
| Pandas       | Data processing and analysis |
| Plotly       | Interactive visualizations   |
| Scikit-learn | Machine learning             |
| NumPy        | Numerical operations         |

---

## 📁 Project Structure

```text
Smart-Business-Analytics/
│
├── app.py
│
├── data/
│   └── sales_data.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── analytics.py
│   └── ml_models.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── sales_prediction.png
│   ├── customer_segmentation.png
│   └── churn_analysis.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/smart-business-analytics.git
```

### 2. Open the project folder

```bash
cd smart-business-analytics
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

## 📊 Dashboard Workflow

```text
             ┌─────────────────────┐
             │     Sales Dataset    │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Data Preprocessing  │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Business Analytics  │
             └──────────┬──────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
     Sales Analysis  Customer      Churn
                     Segmentation  Analysis
          │             │             │
          └─────────────┼─────────────┘
                        ▼
             ┌─────────────────────┐
             │ Business Insights   │
             └─────────────────────┘
```

---

## 📈 Analytics

The dashboard provides interactive analysis of:

* Monthly sales
* Regional sales
* Category sales
* Product performance
* Revenue
* Profit
* Profit margin

Users can filter the dashboard by **Region** and **Category**.

---

## 🤖 Machine Learning

The project includes machine learning functionality for:

### Sales Prediction

The sales prediction module evaluates model performance using:

* **MAE — Mean Absolute Error**
* **RMSE — Root Mean Squared Error**
* **R² — R-squared Score**

The application also provides an interactive comparison between:

```text
Actual Sales
      vs.
Predicted Sales
```

### Customer Segmentation

Customers can be grouped into multiple segments using customer behavior metrics such as:

* Frequency
* Monetary value

The number of segments can be adjusted within the application.

### Churn Analysis

The churn module analyzes customer inactivity risk and provides:

* Churn risk information
* Model accuracy
* Customer-level churn results

---

## 📷 Screenshots

Add your application screenshots inside the `screenshots` folder and update this section.

### Dashboard

```text
Add dashboard screenshot here
```

### Sales Prediction

```text
Add sales prediction screenshot here
```

### Customer Segmentation

```text
Add customer segmentation screenshot here
```

### Churn Analysis

```text
Add churn analysis screenshot here
```

---

## 📂 Dataset

The application supports:

* The default project sales dataset
* User-uploaded CSV files

The default dataset is loaded from:

```text
data/sales_data.csv
```

Users can also upload their own CSV dataset through the Streamlit sidebar.

---

## 🔮 Future Enhancements

Potential future improvements include:

* Advanced sales forecasting
* More machine learning models
* Automated model comparison
* Customer lifetime value prediction
* Advanced recommendation system
* Downloadable analytics reports
* Authentication and user accounts
* Cloud deployment
* Database integration
* Real-time business data integration

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Analyze business sales data.
2. Monitor important business KPIs.
3. Identify sales trends and patterns.
4. Predict future sales using machine learning.
5. Segment customers based on behavior.
6. Identify potential customer churn.
7. Generate actionable business insights.
8. Present analytics through an interactive dashboard.

---

## 👨‍💻 Author

**BTech Data Science Student**

Interested in:

* Data Analytics
* Data Science
* Machine Learning
* Python
* Business Intelligence

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Built with Python • Streamlit • Pandas • Plotly • Machine Learning**
