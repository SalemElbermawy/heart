# FlowGuard - Blood Clot Risk Detection System


## The Problem

Blood clots (thrombosis) are a leading cause of heart attacks and strokes. Detecting the risk early can save lives. Traditional blood tests are expensive and not always available. FlowGuard offers a simple and affordable alternative.



## The Problem with a Fixed Threshold

It would be easy to say: "if the reading is below 960, the person is at risk." However, this is not accurate. A 70-year-old diabetic smoker naturally has thicker blood, so their normal reading might be around 945. The same reading of 945 for a healthy 25-year-old would indicate serious risk. This is why machine learning is needed.

---

## The Machine Learning Solution

Instead of using a single fixed number for everyone, the system learns a personalized safe threshold for each patient based on their medical profile.

The factors used are:

- Age
- Systolic blood pressure (the upper number)
- Diastolic blood pressure (the lower number)
- Whether the patient has diabetes (yes or no)
- Whether the patient is a smoker (yes or no)
- BMI (body mass index)


## The Two Models

### Model 1 - Threshold Predictor (Regression)

This model takes the six patient factors listed above and outputs the minimum safe infrared reading for that specific patient. If the sensor reads a value equal to or above this number, the patient is considered safe. If it reads below, there is a risk of clotting.



### Model 2 - Risk Classifier (Classification)

This model takes the same six patient factors plus the actual sensor reading and directly outputs a classification: Normal or Clot Risk.



## The Three Zones

Based on the infrared sensor readings, there are three zones:

Safe zone: readings of 960 and above. The blood flow is normal.

Transition zone: readings between 950 and 960. The result is uncertain and the patient should be monitored.

Danger zone: readings of 950 and below. The blood is thick enough to suggest a clotting risk.

These zones are personalized. A patient's personal threshold shifts up or down based on their medical profile. The zone boundaries (950 and 960) remain fixed as reference points, but the model adjusts the threshold for each individual.



Run a prediction from the regression model:

 (age, systolic_bp, diastolic_bp, bmi, has_diabetes, is_smoker)

Run a prediction from the classification model:
    enter (age, systolic_bp, diastolic_bp, bmi, has_diabetes, is_smoker, ir_reading)


