import streamlit as st, time
import joblib
import pandas as pd

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:

    st.title("🩺 Diabetes AI")

    st.markdown("## About Me")

    st.write("""
    ** Timothy Folorunsho **

    Aspiring Mechatronics Engineer, Machine Learning Engineer and Mobile App Developer passionate about building AI solutions that solve real-world problems.
    """)

    st.markdown("---")

    st.markdown("### 🚀 Available for Projects")

    st.write("""
    I build beginner-friendly Machine Learning applications including:

    • Diabetes Prediction

    • Heart Disease Prediction

    • Student Performance Prediction

    • House Price Prediction

    • Loan Eligibility Prediction

    • Customer Churn Prediction

    • Chat bot Development

    • Spam Detection
    """)

    st.markdown("---")

    st.warning("""
    Patients should obtain accurate medical measurements from a hospital or licensed healthcare provider before using this tool.

    Incorrect values may produce inaccurate predictions.
    """)

    st.markdown("---")

    st.markdown(
        "**📧 Email:**\
        [timothyfolorunsho995@gmail.com](mailto:timothyfolorunsho995@gmail.com)"
    )

    st.markdown(
        "[💼 LinkedIn](https://www.linkedin.com/in/timothy-folorunsho-36579b299)"
    )

# ── Load saved model and scaler ──
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('diabetes_scaler.pkl')


st.title("🩺 Diabetes Risk Prediction System")

st.markdown("""
Predict the likelihood of diabetes using Machine Learning.

This application is designed for **educational screening purposes only** and should **not replace professional medical diagnosis**.
""")

c1, c2, c3 = st.columns(3)
with c1:
    st.info("🤖 AI Powered")

with c2:
    st.success("⚡ Instant Prediction")

with c3:
    st.warning("🔒 Secure & Private")
    
# ── Collect input from user ──
with st.form("diabetes_prediction_form"):
    st.write("Enter all values below, then click Predict.")
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies (e.g. 2) ', min_value=0, value=None, step=1, format='%d')
        glucose = st.number_input('Glucose level mg/dL (e.g. 120): ', min_value=0, value=None, step=1, format='%d')
        blood_press = st.number_input('Blood pressure mm Hg (e.g. 70): ', min_value=0, value=None, step=1, format='%d')
        skin_thick = st.number_input('Skin thickness mm (e.g. 20): ', min_value=0, value=None, step=1, format='%d')
    with col2:
        insulin = st.number_input('Insulin mu U/ml (e.g. 80): ', min_value=0, value=None, step=1, format='%d')
        bmi = st.number_input('BMI kg/m² (e.g. 25.0): ', min_value=0.0, value=None, step=0.1, format='%.1f')
        dpf = st.number_input('Diabetes pedigree function (e.g. 0.5): ', min_value=0.0, value=None, step=0.01, format='%.2f')
        age = st.number_input('Age in years (e.g. 35): ', min_value=0, value=None, step=1, format='%d')

    submitted = st.form_submit_button(
    "🩺 Predict Diabetes",
    use_container_width=True
     )



if submitted:
    values = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_press,
        'SkinThickness': skin_thick,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }

    missing = [name for name, value in values.items() if value is None]
    if missing:
        st.warning('Please enter all required values before predicting.')
        st.stop()

    pregnancies = float(values['Pregnancies'])
    glucose = float(values['Glucose'])
    blood_press = float(values['BloodPressure'])
    skin_thick = float(values['SkinThickness'])
    insulin = float(values['Insulin'])
    bmi = float(values['BMI'])
    dpf = float(values['DiabetesPedigreeFunction'])
    age = float(values['Age'])

    patient = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_press],
        'SkinThickness': [skin_thick],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    with st.spinner(":green[Analyzing patient data...]"):
        time.sleep(3)

        # ── Scale using the SAVED scaler ──
        patient_scaled = scaler.transform(patient)
        # ── Predict ──
        prediction = model.predict(patient_scaled)[0]
        probability = model.predict_proba(patient_scaled)[0]
        # ── Display Result ──

        st.divider()
        st.subheader("Prediction Result")
        confidence = probability[1] 
        if prediction == 1:
        
            st.error("⚠️ High Risk of Diabetes")
            st.write(f' CONFIDENCE: {probability[1]*100:.1f}% likely diabetic')
            st.progress(float(confidence))
            st.markdown("""
                ### Recommended Next Steps

                ✅ Consult a qualified doctor.

                ✅ Schedule a laboratory blood glucose test.

                ✅ Reduce sugary drinks.

                ✅ Increase physical activity.

                ✅ Maintain healthy body weight.

                ✅ Monitor blood sugar regularly.

                ✅ Follow medical advice before taking medication.
                        """)
        else:
            st.success("✅ Low Risk of Diabetes")
        
            st.write(f' CONFIDENCE: {probability[0]*100:.1f}% likely healthy')
            st.progress(float(confidence))
            st.markdown("""
### Healthy Lifestyle Tips

✅ Continue exercising regularly.

✅ Eat balanced meals.

✅ Stay hydrated.

✅ Maintain healthy weight.

✅ Have routine health checkups.

✅ Monitor your health if symptoms appear.
""")
        
            st.subheader("Prediction Probabilities")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
        "Healthy",
        f"{probability[0]*100:.1f}%"
    )

        with col2:

            st.metric(
        "Diabetic",
        f"{probability[1]*100:.1f}%"
    )
        st.write('\nNOTE: This is an ML prediction, NOT medical advice.')
        st.write('Always consult a qualified healthcare professional.')




st.divider() 

st.caption("""
Developed by ** Timothy Folorunsho **

Machine Learning Engineer | Mobile App Developer | Mechatronics Engineering Student

📧 timothyfolorunsho995@gmail.com


This tool is intended for educational purposes only and does not replace professional medical diagnosis.
""")

st.markdown("[GitHub Repo](https://github.com/timdav-tech/Diabetes-Prediction-SYS.git)")


#git commit -m "Add current project files"
#git push -u origin main