House Price Prediction using Linear Regression and Decision Tree
Project Description:
This project involves building machine learning models to predict the price of a house based on several features such as number of rooms, area, location, and other property attributes. Two algorithms are implemented: Linear Regression and Decision Tree Regressor. The performance of both models is compared, and hyperparameter tuning is applied to improve accuracy.
 
 Objective:
To predict the price of a house using regression techniques and determine which model gives better performance.

Machine Learning Models Used:
1. Linear Regression - For modeling linear relationships between features and house price.
2. Decision Tree Regressor - For capturing non-linear patterns and interactions between features.

Features Used:
- Number of Rooms
- Area (sq.ft)
- Location
- Number of Bathrooms
- Age of the House
- Garage
- Proximity to City Center (or similar features depending on dataset)

Hyperparameter Tuning:
Hyperparameters were tuned using GridSearchCV or RandomizedSearchCV to improve model performance.

For Decision Tree, tuned parameters included:
max_depth	Maximum depth of the tree	[None, 5, 10, 20]
min_samples_split	Minimum samples required to split an internal node	[2, 5, 10]
min_samples_leaf	Minimum samples required at a leaf node	[1, 2, 4]

 Model Evaluation Metrics:
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

Streamlit Deployment :
An interactive Streamlit app allows users to input house details (e.g., rooms, area, location) and get the predicted price. It also shows model comparison metrics.

 Conclusion:
Both Linear Regression and Decision Tree models were implemented for house price prediction. While Linear Regression is simpler and works well for linearly distributed data, Decision Tree can better handle complex, non-linear patterns. Hyperparameter tuning improved accuracy significantly, especially for the Decision Tree model.
