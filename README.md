# TITLE
Type of Institution Prediction App

## link to the app
https://federalapp-czerwazqmnat2k72zufebn.streamlit.app/

#Business understanding 
The goal of this app is to allow users to input the features of an educational institution and predict whether it is a federal or non-federal institution in the UAE. This prediction can be useful for decision-making and analysis in the education sector.

#Data understanding 
The dataset used for training the model contains various features of educational institutions in the UAE, such as the number of masters, total students, bachelors, doctorate, certificates, and Diplomas.

#Data preparation – How do we organize the data for modeling?
The data was preprocessed before training the model by scaling  features using StandardScaler and encoding the categorical features.


#Modelling
Several models were trained such as the Logistic Regression model, Random Forest Classifier, and SVM. Random Forest had the best-performing metrics. The model was optimized using hyperparameter tuning to improve its performance. The optimized model was saved as `rf_optimized3.pkl` and was loaded into the app for making predictions.


#Evaluation.
The model's performance was evaluated during the training phase using cross-validation and various evaluation metrics such as accuracy, precision, recall, and F1-score.

#Deployment 
The app has been deployed using Streamlit library.

#Challenges
The challenge was ensuring that only one campus zone was selected for making a prediction. This was solved by counting the number of selected campus zones and displaying an error message if more than one zone is selected.

#Future Plans
In the future, the model can be further improved by incorporating additional features that may have an impact on predicting the type of institution. 




