# Website-Checker-Using-ML-model-

Identifying Malicious Websites Using Python Machine Learning
Introduction
The Python code used lo identity dangerous phishing websites is explained in this article. The algorithm uses a variety of characteristcs from the URL and webste structure to classify websites as malware. "phishing.""benign." or "defacement
 Statement
The case study you menbon addresses the topic of mult-class classification in the context of malcous URL Getecton The URLs are aivided into four groups: defacement. malare phishing. and benign (or sate). in cybersecurity, this categorizaton is essenbal since & protects users from hazardous informaton and helps identty possible dangers
 Work Flow
Three distinct machine learning models-Random Forest, XGBoost, and LightGBM-are useg by the Python code in the case study to carry out this categorization A dataset of URLs is used to train and test each model, and the accuracy of each model is computed and reported. A tunction to guess the dlass of a given URL is aliso induded in the code. This functon puls various nformation trom the URL, induding the length of the URLthe exstence of suspicous terms, the presence of particular characters, and the number d directones. The LightGBM model then uses these attributes as input to forecast the URL's class
 Dataset
We are going to use a dataset e 6,51.191 malicious URLs, of which 32.520 are malware URLs, 94,111 are phishing URLs, 4,28.103 are benign or safe URLs,and 96,457 are defacement URLs. Let's now talk about the various kinds of URLs that are included in our dataset. benign, malicious, phishing. and defacement URLs.
