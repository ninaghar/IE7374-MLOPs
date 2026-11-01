## Lab Modifications

For this lab, I modified the original FastAPI Iris classification project to implement a Banknote Classification API using the UCI Machine Learning Repository.

**Modifications:**
1. Replaced the Iris dataset with the UCI Banknote Authentication dataset containing 1,372 records and four numerical features.
2. Replaced the Decision Tree Classifier with a Random Forest Classifier.
3. Updated the training pipeline to load the new dataset and evaluate classification performance using accuracy, precision, recall, and F1-score.
4. Updated the API request schema to accept banknote image-derived features.
5. Enhanced the prediction endpoint to return both the predicted class and its estimated probability.
6. Added a `/model-info` endpoint to provide information about the trained model.

**Dataset Source:** UCI Machine Learning Repository — Banknote Authentication (Dataset ID: 267).

These changes extend the original lab by demonstrating custom dataset integration, ensemble learning, model evaluation, and enhanced REST API functionality.