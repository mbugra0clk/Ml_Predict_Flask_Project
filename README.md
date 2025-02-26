# Student GPA Prediction with Flask and Machine Learning

## I made a ml that predicts students' GPA columns: physical, sleep status, study hours, stress, etc. <br/>

**It has 44% accuracy.** <br/>
**If we focus a little more on preprocessing and model, we can get a high accuracy rate.** <br/>

**I tried with models like XGboos, lighytbm, but they did not give good results. The model I used is random forest model.** <br/>

**I learned a lot in this project: the importance of models when creating a ml project.** <br/>

**I learned a lot about integration with Flask api. So did HTML codes.** <br/>


This project is a Flask web application that predicts a student's GPA based on various lifestyle factors using a trained RandomForestRegressor model.

## Features
- Predicts student GPA based on input lifestyle factors.
- Uses One-Hot Encoding for categorical variables.
- Trained using a dataset of student lifestyles.
- Flask web application with an interactive UI.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install flask pandas scikit-learn
```

## Project Structure
```
ML_Flask_Project/
│── app.py                # Main Flask application
│── student_lifestyle_dataset.csv  # Dataset
│── templates/
│   ├── index.html        # Home page
│   ├── result.html       # Result page
│── static/
│   ├── styles.css        # CSS files
│── README.md             # Project documentation
```

## How to Run the Project
1. Clone the repository:
```bash
git clone <repository_url>
cd ML_Flask_Project
```
2. Run the Flask app:
```bash
python app.py
```
3. Open your browser and go to:
```
http://127.0.0.1:5000/
```

## How it Works
1. The dataset is loaded and preprocessed (removes unnecessary columns and applies One-Hot Encoding).
2. A RandomForestRegressor model is trained using the dataset.
3. The user provides input values through the web interface.
4. The model predicts the student's GPA based on the given inputs.
5. The results are displayed on the `result.html` page.

## Example Input
- Study Hours Per Day: `4`
- Extracurricular Hours Per Day: `2`
- Sleep Hours Per Day: `6`
- Social Hours Per Day: `3`
- Physical Activity Hours Per Day: `1`
- Stress Level: `Moderate`

## Example Output
- Predicted GPA: `3.45`
- Model Accuracy Score: `0.87`

## Future Improvements
- Improve model accuracy with hyperparameter tuning.
- Enhance UI for better user experience.
- Deploy the application on a cloud platform.

[Linkedin] (https://www.linkedin.com/in/muhammed-bu%C4%9Frahan-%C3%A7elik-227761283/)

## License
This project is licensed under the MIT License.

