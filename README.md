# Website-Checker-Using-ML-model

# Identifying Malicious Websites Using Python Machine Learning

## Introduction

This project focuses on identifying malicious websites using Python and Machine Learning techniques. The system analyzes various characteristics of URLs and website structures to classify websites into four categories: **Malware**, **Phishing**, **Defacement**, and **Benign (Safe)**. By leveraging machine learning algorithms, the solution helps improve cybersecurity by detecting potentially harmful websites before users interact with them.

## Problem Statement

This case study addresses the problem of **multi-class classification** in the context of malicious URL detection. URLs are categorized into four classes:

* **Benign (Safe)** – Legitimate and non-malicious websites.
* **Phishing** – Websites designed to steal sensitive information such as usernames, passwords, and financial data.
* **Malware** – Websites that distribute malicious software or harmful code.
* **Defacement** – Websites that have been compromised and modified by attackers.

Accurate classification of these URLs is critical for protecting users from cyber threats and enhancing online security.

## Workflow

The solution uses three machine learning models:

* **Random Forest**
* **XGBoost**
* **LightGBM**

Each model is trained and evaluated using a labeled dataset of URLs. The performance of each model is measured and compared using classification accuracy and other evaluation metrics.

A prediction function is also implemented to classify new URLs. This function extracts various features from the URL, including:

* URL length
* Presence of suspicious keywords
* Number of special characters
* Number of redirects
* Domain-related attributes
* Structural URL characteristics

These extracted features are then passed to the trained LightGBM model, which predicts the category of the URL.

## Dataset

The dataset contains **651,191 URLs**, distributed as follows:

| URL Type      |   Count |
| ------------- | ------: |
| Benign (Safe) | 428,103 |
| Defacement    |  96,457 |
| Phishing      |  94,111 |
| Malware       |  32,520 |

This diverse dataset enables the machine learning models to learn patterns associated with both malicious and legitimate websites, resulting in improved detection accuracy and classification performance.

## Conclusion

By combining feature engineering with advanced machine learning algorithms such as Random Forest, XGBoost, and LightGBM, this project provides an effective solution for detecting malicious websites. The system can help organizations and users identify cyber threats early and improve overall web security.
