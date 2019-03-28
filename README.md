# SGEMM Product analysis
In this project I will try to analyse the optimization of various configurations for SGEMM products.
## Usage
All the project scripts use Python 3.
### Preprocess
To preprocess the data simply open a terminal at the `src` directory and run the following command:
```
python3 preprocess.py
```
After this the preprocessed data will be stored at the `data` directory with the name `sgemm_preprocessed.csv`.
### Analyse data
To see the plots of the data simply open a terminal at the `src` directory and run the following command:
```
python3 analyse_data.py
```
After this all the plots of each variable with the target values will be saved at the `doc/img` directory, and also will be displayed on the screen.
### Regression
To train a regression line model and then check its accuracy with a test, simply open a terminal at the `src` directory and run the following command:
```
python3 regression.py
```
### Regression
To train a Decision Tree Regressor model and then check its accuracy with a test, simply open a terminal at the `src` directory and run the following command:
```
python3 decisiontree.py
```
## Purpose
This project is done for the ADM subject from the MIRI of the UPC.
