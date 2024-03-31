# This is Heart Disease Predictor System

## How to setup the Project

` 
git clone https://github.com/AMRITESH240304/Heart-Disease-Predictor-System.git
`

`
pip install requirements.txt
`

### go to the connectDB.py file and paste the your mongodb URI 

### RUN the command to run backend 
`
python main.py
`

## To run frontend download the extention GO live and 
`cd frontend`
### open the index.html and press GOlive 
### Now you are good to go.

# TOOLS that are being used here

## Backend
1) using FastApi and mongodb
2) Heart Disease model using random forest to train and getting the accuracy of 86% 
3) using the methods of data analysis getting some of the unique feature in some column 
4) the main api consists two routes `/store` and `/predict`
5) the first route `/store` first checks if user already exits by the help of email if not then it stores the data into mongodb 
6) the second route `/predicts` find user by the help of email if user exits then it preoceeds and retrive the data of the user from mongodb and predicts the heart disease and then save the result back into mongodb 

## frontend 
1) using basic HTML,css,javascript made two pages index.html and result.html
2) when user fill up all the field and click the button it then makes a post request including header and body to the backend and after saving the result it then redirect to the result page
3) when coming to result it ask for your email to predict the disease of heart 
4) it then show the result wheather you have disease or not

