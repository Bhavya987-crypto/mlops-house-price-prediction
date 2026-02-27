# 🚀 End-to-End MLOps House Price Prediction System

## 📌 Overview

This project demonstrates a **production-ready end-to-end Machine Learning system** for house price prediction using **ZenML** and **MLflow**.

Unlike traditional ML projects that stop at model training in a notebook, this system focuses on:

- Modular pipeline design  
- Reproducibility  
- Clean architecture  
- Experiment tracking  
- Production deployment readiness  

The goal was to design a scalable, maintainable ML system — not just achieve high accuracy.

---

## 🏗 System Architecture

GitHub → ZenML → MLflow → Deployment

- **ZenML** orchestrates modular ML pipelines  
- **MLflow** tracks experiments, metrics, artifacts, and model versions  
- Separate **Training** and **Inference** pipelines  
- Structured for production promotion of validated models  

---

## 🔄 End-to-End ML Workflow

1. Data Ingestion (Factory Design Pattern)
2. Exploratory Data Analysis (EDA)
3. Structured Preprocessing Pipeline
4. Model Training (Strategy Pattern)
5. Experiment Tracking (MLflow)
6. Pipeline Orchestration (ZenML)
7. Production Model Deployment
8. Inference Pipeline for serving predictions

---

## 🧩 Key Design Decisions

### 🏭 Factory Design Pattern (Data Ingestion)

- Supports multiple data sources (CSV, future extensions)
- Avoids hardcoding ingestion logic
- Makes the pipeline extensible
- New data sources can be added without modifying core pipeline logic

---

### 🧠 Structured Preprocessing Pipeline

Built using **Scikit-learn Pipelines and ColumnTransformers**.

Includes:

- Missing value handling  
- One-hot encoding  
- Numerical transformations  
- IQR-based outlier detection  
- Outlier capping  

Using pipelines ensures:

- Consistency between training and inference  
- Prevention of data leakage  
- Reproducibility  

---

### 🎯 Strategy Pattern (Model Training)

Implemented an abstract base class with strategy pattern to:

- Easily switch between models  
- Enable cleaner architecture  
- Improve experimentation  
- Support better model comparison  

---

## 📊 Experiment Tracking (MLflow)

MLflow tracks:

- Parameters  
- Metrics  
- Artifacts  
- Model versions  

Benefits:

- Compare multiple models  
- Reproducibility  
- Version control  
- Model rollback capability  
- Smooth integration with deployment workflows  

---

## 🔀 Training vs Inference Pipelines

### 🔹 Training Pipeline
- Trains and validates models  
- Tracks experiments via MLflow  
- Promotes best-performing validated model  

### 🔹 Inference Pipeline
- Completely separate from training  
- Retrieves active production model  
- Applies consistent preprocessing  
- Serves predictions on new data  

This separation ensures production stability and avoids data leakage.

---

## 🛠 Tech Stack

- Python  
- Scikit-learn  
- ZenML  
- MLflow  
- Pandas  
- NumPy  

---

## 🎯 Final Outcome

A scalable, reproducible, and maintainable ML system designed using real-world MLOps principles.

This project demonstrates understanding of:

- Production ML architecture  
- Pipeline orchestration  
- Experiment tracking  
- Clean code design patterns  
- Deployment-ready ML workflows  

---

## 🚀 Future Enhancements

- CI/CD integration for automated training  
- Docker containerization  
- Cloud deployment (AWS/GCP/Azure)  
- Model monitoring and drift detection  

---

## 👩‍💻 Author

Bhavya Sri 
Master’s in Information Systems  
