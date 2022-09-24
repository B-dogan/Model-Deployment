import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config("Reliable Forecast")


html_temp = """
<div style="background-color:#FBD603;padding:1.5px">
<h1 style="color:black;text-align:center;">Auto Scout </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)



html_temp2 = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:black;text-align:center;">Car Features</h1>
</div><br>"""
st.sidebar.markdown(html_temp2,unsafe_allow_html=True)



# dataframe

# df = pd.read_csv("final_scout_not_dummy.csv", nrows=(100))

# # df'leri gösterme yöntemleri
# st.table(df.head())
#st.write(df.head()) #dynamic, you can sort
# st.dataframe(df.head())#dynamic, you can sort




import pickle
filename = 'auto_scout.pickle'
model = pickle.load(open(filename, 'rb'))


make_model = st.sidebar.selectbox("Car",('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia',
                          'Renault Clio', 'Renault Duster', 'Renault Espace'))
km = st.sidebar.slider("km:",min_value=0, max_value=317000)
age = st.sidebar.selectbox("Age:",(0,1,2,3))
gearing_type = st.sidebar.selectbox("Gearing Type", ('Automatic', 'Manual', 'Semi-automatic'))
gears = st.sidebar.number_input("Gears:",min_value=5, max_value=8)
hp_kw = st.sidebar.slider("horsepower(kw):",min_value=40, max_value=239)

new_data = {"make_model" : make_model,
			"km" : km,
			"age" : age,
			"Gearing_Type" : gearing_type,
			"Gears" : gears,
			"hp_kW" : hp_kw}
           
            
                                   # sıra farklı olsa sıkıntı olur mu ?

new_obs = pd.DataFrame.from_dict([new_data])



st.markdown("## The features of your car is below")
st.write(new_obs.head())

st.markdown("#### if the properties are correct, press **Predict** for prediction")


if st.button("Predict"):
	import time 
	with st.spinner("Calculating"):
		 time.sleep(1)
		 pred = model.predict(new_obs)
		 st.info(f'Analyze Results are: € {round(pred[0])}')
		 if make_model == 'Audi A1':
		 	st.video("https://www.youtube.com/watch?v=9EggRCYplc8")
		 elif make_model == 'Audi A3':
		 	st.video("https://www.youtube.com/watch?v=u26xl5VYXh4")
		 elif make_model == 'Opel Astra':
		 	st.video("https://www.youtube.com/watch?v=8Tg1F5ay6HA")
		 elif make_model == 'Opel Corsa':
		 	st.video("https://www.youtube.com/watch?v=1pAAFAUGvCY")
		 elif make_model == 'Opel Insignia' :
		 	st.video("https://www.youtube.com/watch?v=OaHfxILGdOI")
		 elif make_model == 'Renault Clio':
		 	st.video("https://www.youtube.com/watch?v=2VfcoNXjnus")
		 elif make_model == 'Renault Duster':
		 	st.video("https://www.youtube.com/watch?v=qBhZpcsT7QU")
		 else :
		 	st.video("https://www.youtube.com/watch?v=yRK77pesJ0Y")           


	







	
























































