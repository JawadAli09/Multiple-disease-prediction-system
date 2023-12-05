import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit.components.v1 as components



page_bg_img="""

<style>
[class="css-7ym5gk e1ewe7hr10"]{ 
  font-size: 18px;
  letter-spacing: 2px;
  text-transform: uppercase;
  display: inline-block;
  text-align: center;
  font-weight: bold;
  padding: 0.7em 2em;
  border: 3px solid black;
  border-radius: 2px;
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.1);
  color: black;
  text-decoration: none;
  transition: 0.3s ease all;
  z-index: 1;
}

[class="css-7ym5gk e1ewe7hr10"]:before {
  transition: 0.5s all ease;
  position: absolute;
  top: 0;
  left: 50%;
  right: 50%;
  bottom: 0;
  opacity: 0;
  content: '';
  background-color: black;
  z-index: -1;
}

[class="css-7ym5gk e1ewe7hr10"]:hover, button:focus {
  color: white;
}

[class="css-7ym5gk e1ewe7hr10"]:hover:before, [class="css-7ym5gk e1ewe7hr10"]:focus:before {
  transition: 0.5s all ease;
  left: 0;
  right: 0;
  opacity: 1;
}

[class="css-7ym5gk e1ewe7hr10"]:active {
  transform: scale(0.9);
}

}



[class="css-10trblm eqr7zpz0"]{
color:red;

}



[class="css-6qob1r e1akgbir3"]{
background-color:red;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

heart_model=pickle.load(open('C:/Users/Lenovo/OneDrive/Desktop/Mulitple disease prediction/fickle files/heart_model.pkl','rb'))
parkinsons_model=pickle.load(open('C:/Users/Lenovo/OneDrive/Desktop/Mulitple disease prediction/fickle files/parkinsons_model.pkl','rb'))
diabetes_model=pickle.load(open('C:/Users/Lenovo/OneDrive/Desktop/Mulitple disease prediction/fickle files/diabetes_model.pkl','rb'))

# def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# add_bg_from_url()


# st.markdown(page_bg_img, unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          [
                           'Heart Disease Prediction System',
                          'Parkinsons Prediction System',
                          'Diabetes Prediction System'],
                          icons = ['heart','person','check'],
                          default_index=0)
   
if (selected == 'Heart Disease Prediction System'):
        
        st.title('Heart Disease Prediction System')
        def add_bg_from_url():
            st.markdown(
               f"""
               <style>
               .stApp {{
                     background-image: url("https://pixabay.com/get/g71ef50702078a531bc20b8a9663de4774f825d382c3280c66ff07f1c6d127e8512d7b4267acf7041ff51b5c5486fbee9_1280.jpg");
                     background-attachment: fixed;
                     background-size: cover
            }}
            </style>
               """,
            unsafe_allow_html=True
      )

        add_bg_from_url()
      #   image=(Image.open('pexels-caio-65550.jpg'))
      #   st.image(image, caption=None)
 
        
        col1, col2 = st.columns(2)
        
        with col1:
          age = st.text_input('Age')
        
        with col2:
          sex = st.text_input('Sex')
        
        with col1:
          cp = st.text_input('Chest Pain types')
        
        with col2:
          trestbps = st.text_input('Resting Blood Pressure')
        
        with col1:
          chol = st.text_input('Serum Cholestoral in mg/dl')
        
        with col2:
          fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
        with col1:
          restecg = st.text_input('Resting Electrocardiographic results')
        
        with col2:
          thalach = st.text_input('Maximum Heart Rate achieved')
        
        with col1:
          exang = st.text_input('Exercise Induced Angina')
        
        with col2:
          oldpeak = st.text_input('ST depression induced by exercise')
        
        with col1:
          slope = st.text_input('Slope of the peak exercise ST segment')
        
        with col2:
          ca = st.text_input('Major vessels colored by flourosopy')
        
        with col1:
          thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
        heart_diagnosis = ''
    
    # creating a button for Prediction
    
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
            if heart_prediction[0] == 1:
              heart_diagnosis = 'The person is having heart disease'
            else:
              heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)
        
        
        
if selected == 'Parkinsons Prediction System':
     st.title('Parkinsons Prediction System')

     def add_bg_from_url():
            st.markdown(
               f"""
               <style>
               .stApp {{
                     background-image: url("https://pixabay.com/get/g0dd38c3779a08767089b9a033b9dddedef6c279660dea3dd274bc7f599c24e3136143d4a7dc04c319f45f4c0f8b1ab260f4325f6000f911c523b47fb44d52d62_1280.jpg");
                     background-attachment: fixed;
                     background-size: cover
            }}
            </style>
               """,
            unsafe_allow_html=True
      )
     add_bg_from_url()
     
     col1, col2, col3, col4, col5 = st.columns(5)  
    
     with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
     with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
     with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
     with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
     with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
     with col1:
        RAP = st.text_input('MDVP:RAP')
        
     with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
     with col3:
        DDP = st.text_input('Jitter:DDP')
        
     with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
     with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
     with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
     with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
     with col3:
        APQ = st.text_input('MDVP:APQ')
        
     with col4:
        DDA = st.text_input('Shimmer:DDA')
        
     with col5:
        NHR = st.text_input('NHR')
        
     with col1:
        HNR = st.text_input('HNR')
        
     with col2:
        RPDE = st.text_input('RPDE')
        
     with col3:
        DFA = st.text_input('DFA')
        
     with col4:
        spread1 = st.text_input('spread1')
        
     with col5:
        spread2 = st.text_input('spread2')
        
     with col1:
        D2 = st.text_input('D2')
        
     with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
     parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
     if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
     st.success(parkinsons_diagnosis)

# Diabetes Prediction Page
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction System'):
        st.title('Diabetes Prediction System')
        def add_bg_from_url():
            st.markdown(
               f"""
               <style>
               .stApp {{
                     background-image: url("https://pixabay.com/get/g5d2e919554af27d6d92c49f7069273b81b0bdb0d9ea9087774e2f3917bed00b8eb30ce7cf457f9c50064ffdffa5727d0a28e7349f751701b0e2a2b48362d8b63_1280.jpg");
                     background-attachment: fixed;
                     background-size: cover
            }}
            
            </style>
               """,
            unsafe_allow_html=True
      )
        add_bg_from_url()
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
         Pregnancies = st.text_input('Number of Pregnancies')
        
        with col2:
         Glucose = st.text_input('Glucose Level')
    
        with col3:
         BloodPressure = st.text_input('Blood Pressure value')
    
        with col1:
         SkinThickness = st.text_input('Skin Thickness value')
    
        with col2:
         Insulin = st.text_input('Insulin Level')
    
        with col3:
         BMI = st.text_input('BMI value')
    
        with col1:
          DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
        with col2:
         Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
        diabetes_diagnosis = ''
    
    # creating a button for Prediction
    
        if st.button('Diabetes Test Result'):
          diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
          if (diabetes_prediction[0] == 1):
             diabetes_diagnosis = 'The person is diabetic'
          else:
            diabetes_diagnosis = 'The person is not diabetic'
        
        st.success(diabetes_diagnosis)
    
    