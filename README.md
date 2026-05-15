# Email Spam Detection

This project is an NLP-based Machine Learning model that classifies emails as Spam or Not Spam (Ham).

## Project Overview

Spam emails are unwanted messages that often contain advertisements, scams, or harmful links. This project uses Natural Language Processing (NLP) techniques and Machine Learning algorithms to automatically detect spam messages.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit 
- Jupyter Notebook

## Machine Learning Model Used

- Naive Bayes Classifier

## NLP Techniques Used

- Text Cleaning
- Tokenization
- Stopword Removal
- Bag of Words 
- TF-IDF Vectorization

## Dataset

Dataset used: Email Spam Collection Dataset

Example columns:

- Label (Spam-1 / Ham-0)
- Message Text

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction using TF-IDF & Bow
5. Model Training
6. Model Evaluation
7. Prediction System

# Model Performance in Naive Bayes Classifier
1. For Bag of Words Accuracy=0.987
2. For TF-IDF       Accuracy=0.875

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
streamlit run app.py
