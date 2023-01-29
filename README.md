# Body-Fat-Predictor-WebApp

**Problem Statement**:
This is a regression project to predict the body fat percentage based on limited athropological measurement data available.
Obesity, associated with having excess body fat, is a critical  public health problem that causes serious illness.This project illustrates the used of multiple regression techniques in evaluating and estimating the percentage of body fat. Accurate measurement of body fat is inconvenient/costly and it is desirable to have easy methods of estimating body fat that are not inconvenient/costly.(However, there are standard methods. for instance, the abdomen 2 circumference is measured "laterally, at the level of the iliac crests, and anteriorly, at the umbilicus".)

Nevertheless, there is need for easy method to estimate the percentage of body fat.The predicted feature is Accident_severity which is a multi-class variable. The task is to classify this variable based on the other 31 features step-by-step by going through each day's task. Your metric for evaluation will be rmse and r2score.

Source of dataset: Link to the dataset

**Web application**
flask webApp

**Tasks and techniques used**

2. Data preparation and pre-processing
- variable tansformation using log
- feature selection using simple filter

3. Modelling using sci-kit learn library
Baseline model using linear regression and random forest using default techniques
Tuned hyperparameters using n_estimators and max_depth parameters in the case of random forest

4. Evaluation

Evaluation metric was rmse and r2score.

Final model evaluation r2_score = 67%
