# E-Commerce Customer Churn Prediction

## 1. Project Overview

This project analyzes e-commerce customer behavior to identify customers who are at risk of **churning** and to uncover the key factors that contribute to customer churn.

E-commerce businesses rely heavily on repeat purchases and customer retention to sustain long-term revenue. However, retention efforts are often reactive, making it difficult for businesses to identify customers who are likely to churn before they stop transacting.

To address this problem, this project applies **Exploratory Data Analysis (EDA)** and **Machine Learning classification** to predict customer churn risk. The results can help the business prioritize high-risk customers and enable the implementation of proactive, targeted retention strategies.

### Problem Statement

The business needs to identify customers who are likely to churn before they become inactive, allowing the retention team to intervene proactively rather than relying solely on reactive retention efforts.

### Key Objectives

* Identify customers who have a high risk of churning.
* Analyze customer behavior and characteristics associated with churn.
* Determine the key factors that contribute to customer churn.
* Build a classification model to predict customer churn risk.
* Prioritize the identification of potential churners by optimizing for **Recall and F2-Score**.
* Provide actionable recommendations to support proactive customer retention and protect long-term revenue.

---

## 2. Data Sources

The project uses an e-commerce customer dataset containing information about customer characteristics, behavior, and transaction-related activity.

The dataset is used to analyze patterns associated with customer churn and to develop a machine learning classification model for churn prediction.

### Dataset

* **E-Commerce Customer Churn Dataset** – Customer demographic, behavioral, and transactional information used for exploratory analysis and churn prediction.
  E-Commerce Customer Churn Dataset – Contains customer-level information used to analyze customer behavior and predict whether a customer is likely to churn.

---

## 3. Technologies Used

### Programming Language

* Python

### Data Manipulation & Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Statistical Analysis

* SciPy
* scikit-posthocs

### Machine Learning

* Scikit-learn
* Classification algorithms
* Cross-validation
* Hyperparameter tuning
* Model evaluation

### Development Environment

* Jupyter Notebook
* Visual Studio Code

### Version Control

* Git
* GitHub

---

## 4. Project Structure

```text
├── README.md
│
├── data
│   ├── external       <- Data from third-party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- Final datasets prepared for analysis or modeling
│   └── raw            <- Original, immutable datasets
│
├── models             <- Trained models, predictions, and model summaries
│
├── notebooks          <- Jupyter notebooks containing the analysis workflow
│
├── references         <- Data dictionaries and supporting documentation
│
├── reports            <- Generated reports and analysis outputs
│   └── figures        <- Charts and visualizations used in reporting
│
├── requirements.txt   <- Python dependencies required to reproduce the project
│
└── src                <- Source code used for data processing and analysis
```

---

## 5. Analysis & Machine Learning Workflow

The project follows a structured data science workflow:

### 5.1 Data Understanding

The dataset is examined to understand the structure of the data, the meaning of each feature, and the target variable used to represent customer churn.

### 5.2 Exploratory Data Analysis

Exploratory analysis is performed to:

* Understand the distribution of customer churn.
* Examine customer characteristics and behavioral patterns.
* Identify relationships between features and churn.
* Detect potential patterns that may indicate increased churn risk.

### 5.3 Data Cleaning & Preprocessing

The data preparation process includes relevant steps such as:

* Handling missing values.
* Checking for duplicate records.
* Identifying and handling outliers where appropriate.
* Preparing categorical and numerical features.
* Encoding categorical variables.
* Scaling numerical features when required.
* Preparing the dataset for machine learning.

### 5.4 Feature Engineering & Selection

Relevant customer behavioral and transactional features are prepared and evaluated to improve the model's ability to distinguish between customers who are likely to churn and those who are likely to remain active.

### 5.5 Machine Learning Modeling

Classification models are evaluated to identify the model that best supports the business objective of detecting potential churners.

Model selection is performed using cross-validation and appropriate evaluation metrics.

### 5.6 Model Evaluation

Because the business priority is to identify as many potential churners as possible, **Recall** is prioritized alongside the **F2-Score**.

* **Recall** measures the proportion of actual churners that the model successfully identifies.
* **F2-Score** places greater emphasis on Recall than Precision, making it suitable when missing a potential churner is considered more costly than incorrectly flagging a customer as high risk.

The selected model is therefore evaluated based on its ability to capture potential churners and support proactive retention activities.

---

## 6. Summary of Findings

### 6.1 Business Insights

The analysis provides insights into customer behavior and the factors associated with churn.

The machine learning approach enables the business to move from a **reactive retention strategy** toward a more **proactive, data-driven customer retention strategy** by identifying customers who are at higher risk of churn.

Key findings from the analysis include:

* Customer churn can be predicted using behavioral and customer-related features.
* Certain customer characteristics and behaviors are associated with a higher likelihood of churn.
* Machine learning can help prioritize customers who require retention attention.
* Optimizing for Recall and F2-Score supports the business objective of minimizing missed potential churners.

> **Note:** Insert the specific numerical findings and most important features from the final notebook analysis here.

### 6.2 Actionable Recommendations

Based on the analysis and churn prediction results, the business should:

1. **Prioritize High-Risk Customers**
   Use the churn prediction model to identify customers with a high probability of churning and prioritize them for retention actions.
2. **Implement Proactive Retention Campaigns**
   Contact high-risk customers before they become inactive rather than waiting until they have already churned.
3. **Personalize Retention Strategies**
   Develop targeted offers, incentives, or communication strategies based on customer characteristics and behavioral patterns associated with churn.
4. **Monitor Customer Behavior Continuously**
   Regularly update churn predictions as new customer activity becomes available, allowing the business to respond to changes in customer risk.
5. **Measure Retention Campaign Effectiveness**
   Track the performance of retention initiatives by monitoring changes in churn rates, customer retention, and customer reactivation.

---

## 7. Business Impact

The expected business impact of this project is to help the e-commerce business:

* Increase customer retention.
* Reduce preventable customer churn.
* Protect recurring revenue from existing customers.
* Improve the efficiency of retention campaigns.
* Enable targeted allocation of retention resources.
* Improve customer experience through more relevant and proactive engagement.

The ultimate goal is to **move from reactive retention to proactive customer retention using data-driven insights and machine learning**.

---

## 8. Contact

* **Name:** Mika Mahaputra
* **Email:** [Your Email]
* **LinkedIn:** [Your LinkedIn]
* **GitHub:** [Your GitHub]
