# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
  - Analyze the factors that affect loan approvals
  - Build a Supervised Learning model to automate the loan eligibility process
  - Deploy the prediction model API to AWS Cloud

## Hypothesis
Applicants with higher incomes and an active credit history are more likely to have their loan approved because they have access to more funds and tend to handle debt better.

## EDA 
Baseline of approval rate in the dataset is 68.73%.
Applicants that are graduates have higher incomes.
The higher the total income, e.g. applicant income + coapplicant income, the likelier the applicant is approved for a loan.
More applicants that were approved had a credit history than not. In the case of applicants without a credit history, there was a lower percentage of loan approvals. 


## Process
The dataset was split into training and testing sets with the target set as Loan_Status. Then, the features were divided into numerical and categorical features in order to complete feature engineering which consisted of:
### Numerical Features: 
  - Sum of Applicant_Income and Coapplicant_Income into a single feature Total_Income
  - Log Transformation of LoanAmount and Total_Income
  - SimpleImputer to replace null values
  - Scaling using StandardScaler
  - Best feature selection with SelectKBest
### Categorical Features:
  - SimpleImputer to replace null values
  - OneHotEncoder to transform categorical data into dummy variables
  - Principle Component Analysis
 
 Preprocessing was done using ColumnTransformer and was fed into the pipelines of each prediction model.
 ### Prediction Models:
  - Logistic Regression
  - RandomForestClassifier
  - DecisionTreeClassifier
  - GradientBoostingClassifier
  - XGBClassifier

## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)
The model with the highest precision was Logistic Regression
![image](https://user-images.githubusercontent.com/22251105/179367583-d35e2ebf-4298-4493-84e6-78c76abecf7a.png)
![image](https://user-images.githubusercontent.com/22251105/179367618-c6861eb7-98b1-4c76-bba9-426cfd26a9f0.png)

Finally, the prediction model was pickled and loaded into the request notebook. A simple API was then created using Flask in order to retrieve the prediction of the aforementioned Logistic Regression model. The API app was then uploaded to an AWS EC2 instance in order to deploy the loan approval API to the Cloud.  

## Challanges 
I had difficulties deploying my API app in the beginning. At one point, I tried using the same point on more than one occasion and later, my AWS EC2 instance kept either denying access and ran low on memory.  

## Future Goals
If I had more time, I would:
  - further develop the features (feature selection, tweaking Imputer parameters, etc).
  - dig deeper into hyperparameters tuning for each and every model. 
  - have liked to improve my Cloud computing skills.
