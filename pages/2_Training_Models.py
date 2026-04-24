import streamlit as st
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import main_reg
import main_label

st.set_page_config(page_title="FlowGuard Models", page_icon="🩸", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --primary:#dc2626;
    --primary-dark:#991b1b;
    --primary-light:#fecaca;
    --bg:#04191a;
    --surface:#0a2829;
    --border:rgba(220,38,38,0.2);
    --text:#f3f4f6;
    --muted:#9ca3af;
}

html, body, .stApp {
    background: var(--bg);
    color: var(--text);
    font-family:'DM Sans',sans-serif;
}
.block-container {max-width:850px;}

.card {
    background:var(--surface);
    padding:18px;
    border-radius:14px;
    border:1px solid var(--border);
    margin-bottom:15px;
}

.result-good {
    background:#052e16;
    border:1px solid #16a34a;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

.result-bad {
    background:#450a0a;
    border:1px solid #dc2626;
    padding:15px;
    border-radius:12px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align:center;color:#dc2626'>🩸 FlowGuard Models</h2>
<p style='text-align:center;color:#9ca3af'>Understand and test both prediction systems</p>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📐 Threshold Model", "🔬 Risk Classifier"])

with tab1:
    st.markdown("### Patient Data")

    c1, c2 = st.columns(2)

    with c1:
        age = st.number_input("Age",18,85,45)
        sys_bp = st.number_input("Systolic BP",90,200,120)
        dia_bp = st.number_input("Diastolic BP",60,120,80)

    with c2:
        bmi = st.number_input("BMI",17.0,45.0,24.0)
        diabetes = st.selectbox("Diabetes",["No","Yes"])
        smoker = st.selectbox("Smoker",["No","Yes"])

    if st.button("Calculate Threshold"):

        threshold = main_reg.prediction_function(
            age, sys_bp, dia_bp, bmi,
            1 if diabetes=="Yes" else 0,
            1 if smoker=="Yes" else 0
        )[0]

        st.markdown(f"""
        <div class="card">
        <h4>Safe IR Threshold</h4>
        <h2 style='color:#22c55e'>{threshold:.1f}</h2>
        <p>If sensor value falls below this → clot risk increases</p>
        </div>
        """, unsafe_allow_html=True)

        # visual indicator
        st.progress(min(max(threshold/1000,0),1))

        # BMI interpretation
        if bmi < 18.5:
            st.warning("Underweight → may affect circulation")
        elif bmi < 25:
            st.success("Normal BMI → optimal blood flow")
        elif bmi < 30:
            st.warning("Overweight → increased viscosity")
        else:
            st.error("Obese → high clot risk")


with tab2:
    st.markdown("### Patient + Sensor Data")

    c3, c4 = st.columns(2)

    with c3:
        age2 = st.number_input("Age ",18,85,45)
        sys2 = st.number_input("Systolic BP ",90,200,120)
        dia2 = st.number_input("Diastolic BP ",60,120,80)
        ir = st.number_input("IR Reading",880.0,999.0,965.0)

    with c4:
        bmi2 = st.number_input("BMI ",17.0,45.0,24.0)
        diabetes2 = st.selectbox("Diabetes ",["No","Yes"])
        smoker2 = st.selectbox("Smoker ",["No","Yes"])

    if st.button("Predict Risk"):

        result = main_label.prediction_function(
            age2, sys2, dia2, bmi2,
            1 if diabetes2=="Yes" else 0,
            1 if smoker2=="Yes" else 0,
            ir
        )[0]

        if result == 0:
            st.markdown("""
            <div class="result-good">
            <h3>✅ Normal Flow</h3>
            <p>No clot detected</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-bad">
            <h3>⚠️ Clot Risk</h3>
            <p>Medical attention recommended</p>
            </div>
            """, unsafe_allow_html=True)

        # simple risk bar
        risk_score = 1 if result==1 else 0.2
        st.progress(risk_score)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("FlowGuard AI · Medical Decision Support ")