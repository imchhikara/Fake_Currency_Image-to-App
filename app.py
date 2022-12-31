import pickle
import streamlit as st
import PIL as pil 
  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

#Our prediction model
def prediction(variance,skewness,curtosis,entropy):
    prediction = model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


html_temp = """
        <div style ="background-color:black;padding:10px">
        <h1 style ="color:yellow;text-align:center;">Currency - Real or Fake</h1>
        </div>
        """      
st.markdown(html_temp, unsafe_allow_html = True)

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)