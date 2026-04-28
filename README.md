
# there are screenshots.below to know how y
to use it 

# I was very loyal and I told using AI in frontend to show my work. Please look at the backend parts "Rag Model", ML models and etc. I have coded them line by line 0 usage of AI. I just used it in UI ( streamlit files ) and the time of using AI it was zero i just got the code to the file not write line by line from AI i got it copy , paste. i said that to avoid the penalty for a lack of points. i never write befor the AI. whole this time it was for backend. please be fair and appreciate my work and loyalty.


# And I have got these data from my doctor in the laboratory in my STEM high school on real samples. The data set comes from the reading of my sensor and some from the lab sensor by the docto5 and i did callibration and edit for it and preprocessing








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




## The data set comes from the reading of my sensor and some from the lab sensor and i did callibration and edit for it and preprocessing

# How to use it 

## Rag_Model 

you can use it to ask it about the idea of the project and the everything related to clot disease like that ::

<img width="1070" height="571" alt="Screenshot 2026-04-28 055142" src="https://github.com/user-attachments/assets/c2a081f1-8d9b-49e4-b22e-0fda246cd9d6" />


<img width="883" height="432" alt="image" src="https://github.com/user-attachments/assets/f0234fbf-f05e-4727-a23f-948077287aee" />

<img width="898" height="752" alt="image" src="https://github.com/user-attachments/assets/ed267f77-3b51-435f-94e9-1032c870db8a" />



## Training models

<img width="1081" height="724" alt="Screenshot 2026-04-25 063459" src="https://github.com/user-attachments/assets/ead7d1a1-90b3-41c8-a00b-bb7a1080ada8" />
<img width="1120" height="718" alt="Screenshot 2026-04-25 063728" src="https://github.com/user-attachments/assets/221ec9e3-2ad6-4f60-924d-835009ec5deb" />
<img width="1236" height="837" alt="Screenshot 2026-04-25 063658" src="https://github.com/user-attachments/assets/ea7e67d9-6801-47f3-aca0-4cab7fa64ffb" />
<img width="1152" height="758" alt="Screenshot 2026-04-25 063552" src="https://github.com/user-attachments/assets/2325eb46-1464-4e67-9706-d6c2f4c88db0" />





