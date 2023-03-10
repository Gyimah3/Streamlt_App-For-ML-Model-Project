# Importing required Library
import streamlit as st
import pandas as pd
import numpy as np
import os, pickle
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
from PIL import Image
import threadpoolctl
# Setting up page configuration and directory path





st.set_page_config(page_title="Sales Forecasting App", page_icon="🐞", layout="centered")
DIRPATH = os.path.dirname(os.path.realpath(__file__))


# Setting background image

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-color:black;
background-image:
radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px),
radial-gradient(rgba(255,255,255,.4), rgba(255,255,255,.1) 2px, transparent 30px);
background-size: 550px 550px, 350px 350px, 250px 250px, 150px 150px;
background-position: 0 0, 40px 60px, 130px 270px, 70px 100px;

}

</style>
'''
st.markdown(page_bg_img,unsafe_allow_html=True)



# Setting up logo
left1, left2, mid,right1, right2 = st.columns(5)
with left1:
    #image1= Image.open('https://github.com/Gyimah3/Streamlt_App-For-ML-Model-Project/blob/main/images/lo.jpg')
    st.image('https://th.bing.com/th/id/R.0fbe9296bcb3eccfd1da47a17b0f8c4c?rik=9gof%2bvdKHPQyYw&pid=ImgRaw&r=0', width=400,caption=None, use_column_width=None, clamp=100, channels="RGB", output_format='JPEG')
with right1:
   # image= Image.open("images\loi.jpg")
    st.image('https://th.bing.com/th/id/OIP.hOpxwsP1OFM5ebfOnHq_kQAAAA?pid=ImgDet&rs=1',caption=None, use_column_width=None, clamp=100, channels="RGB", output_format='JPEG', width=317,)

# 

# Setting up Sidebar
social_acc = ['Data Field Description', 'EDA', 'About App']
social_acc_nav = st.sidebar.radio('**INFORMATION SECTION**', social_acc)

if social_acc_nav == 'Data Field Description':
    st.sidebar.markdown("<h2 style='text-align: center;'> Data Field Description </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown("**Date:** The date you want to predict sales  for")
    st.sidebar.markdown("**Family:** identifies the type of product sold")
    st.sidebar.markdown("**Onpromotion:** gives the total number of items in a product family that are being promoted at a store at a given date")
    st.sidebar.markdown("**Store Number:** identifies the store at which the products are sold")
    st.sidebar.markdown("**Holiday Locale:** provide information about the locale where holiday is celebrated")

elif social_acc_nav == 'EDA':
    st.sidebar.markdown("<h2 style='text-align: center;'> Exploratory Data Analysis </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown('''---''')
    st.sidebar.markdown('''The exploratory data analysis of this project can be find in a Jupyter notebook from the linl below''')
    st.sidebar.markdown("[Open Notebook](https://github.com/Gyimah3/Store-Sales----Time-Series-Forecasting-Regression-project-/blob/main/Store%20Sales%20--%20Time%20Series%20Forecasting(Regression%20project).ipynb)")

elif social_acc_nav == 'About App':
    st.sidebar.markdown("<h2 style='text-align: center;'> Sales Forecasting App </h2> ", unsafe_allow_html=True)
    st.sidebar.markdown('''---''')
    st.sidebar.markdown("This App predicts the sales for product families sold at Favorita stores using regression model.")
    st.sidebar.markdown("")
    st.sidebar.markdown("[ Visit Github Repository for more information](https://github.com/Gyimah3/Store-Sales----Time-Series-Forecasting-Regression-project-)")
    st.sidebar.markdown("For mom❄️ and Delp❄️.")
    st.sidebar.markdown("")
    


@st.cache(allow_output_mutation=True)
def Load_ml_items(relative_path):
    "Load ML items to reuse them"
    with open(relative_path, 'rb') as file:
        loaded_object = pickle.load(file)
    return loaded_object


loaded_object = Load_ml_items('ML_items')


    #return loaded_object
Loaded_object = Load_ml_items('ML_items')
model, encoder, train_data, stores, holidays_event = Loaded_object['model'], Loaded_object['encoder'], Loaded_object['train_data'], Loaded_object['stores'], Loaded_object['holidays_event']

# Setting Function for extracting Calendar features
@st.cache(allow_output_mutation=True)

def getDateFeatures(df, date ):
    df['date'] = pd.to_datetime(df[date])
    df['month'] = df.date.dt.month
    df['day_of_month'] = df.date.dt.day
    df['day_of_year'] = df.date.dt.dayofyear
    df['week_of_year'] = df.date.dt.isocalendar().week
    df['day_of_week'] = df.date.dt.dayofweek
    df['year'] = df.date.dt.year
    df['is_weekend']= np.where(df['day_of_week'] > 4, 1, 0)
    df['is_month_start']= df.date.dt.is_month_start.astype(int)
    df['is_month_end']= df.date.dt.is_month_end.astype(int)
    df['quarter']= df.date.dt.quarter
    df['is_quarter_start']= df.date.dt.is_quarter_start.astype(int)
    df['is_quarter_end']= df.date.dt.is_quarter_end.astype(int)
    df['is_year_start']= df.date.dt.is_year_start.astype(int)
    
    return df

# Setting up variables for input data
@st.cache()
def setup(tmp_df_file):
    "Setup the required elements like files, models, global variables, etc"
    pd.DataFrame(
        dict(
            date=[],
            store_nbr=[],
            family=[],
            onpromotion=[],
            city=[],
            state=[],
            store_type=[],
            cluster=[],
            day_type=[],
            locale=[],
            locale_name=[],
        )
    ).to_csv(tmp_df_file, index=False)

# Setting up a file to save our input data
tmp_df_file = os.path.join(DIRPATH, "tmp", "data.csv")
setup(tmp_df_file)

# setting Title for forms
st.markdown("<h2 style='text-align: center;'> Sales Prediction </h2> ", unsafe_allow_html=True)
st.markdown("<h7 style='text-align: center;'> Fill in the details below and click on SUBMIT button to make a prediction for a specific date and item </h7> ", unsafe_allow_html=True)


# Creating columns for for input data(forms)
left_col, mid_col, right_col = st.columns(3)

# Developing forms to collect input data
with st.form(key="information", clear_on_submit=True):
    
    # Setting up input data for 1st column
    left_col.markdown("**PRODUCT DATA**")
    date = left_col.date_input('Select a date:',min_value= train_data['date'].min())
    family = left_col.selectbox("Item family:", options= list(train_data["family"].unique()))
    onpromotion = left_col.selectbox("Onpromotion code:", options= set(train_data["onpromotion"].unique()))
    store_nbr = left_col.selectbox("Store Number:", options= set(stores["store_nbr"].unique()))
    
    # Setting up input data for 2nd column
    mid_col.markdown("**STORE DATA**")
    city = mid_col.selectbox("City:", options= set(stores["city"].unique()))
    state = mid_col.selectbox("State:", options= list(stores["state"].unique()))
    cluster = mid_col.selectbox("Store Cluster:", options= list(stores["cluster"].unique()))
    store_type = mid_col.radio("Store Type:", options= sorted(set(stores["store_type"].unique())), horizontal = True)

    # Setting up input data for 3rd column
    right_col.markdown("**ADDITIONAL DATA**")
    check= right_col.checkbox("Is it a Holiday or weekend?")
    if check:
        right_col.write('Fill the following information on Day Type')
        day_type = right_col.selectbox("Holiday:", options= ('Holiday','Special Day:Transfered/Additional Holiday','No Work/Weekend'))
        locale= right_col.selectbox("Holiday Locale:", options= list(holidays_event["locale"].unique()))
        locale_name= right_col.selectbox("Locale Name:", options= list(holidays_event["locale_name"].unique()))
    else:
        day_type = 'Workday'
        locale = 'National'
        locale_name= 'Ecuador'
 
    submitted = st.form_submit_button(label="Submit")

# Setting up background operations after submitting forms
if submitted:
    # Saving input data as csv after submission
    pd.read_csv(tmp_df_file).append(
        dict(
                date = date,
                store_nbr = store_nbr,
                family=family,
                onpromotion= onpromotion,
                city=city,
                state=state,
                store_type=store_type,
                cluster=cluster,
                day_type=day_type,
                locale=locale,
                locale_name=locale_name
            ),
            ignore_index=True,
    ).to_csv(tmp_df_file, index=False)
    st.balloons()
     

    df = pd.read_csv(tmp_df_file)
    df= df.copy()
   
        
    # Getting date Features
    processed_data= getDateFeatures(df, 'date')
    processed_data= processed_data.drop(columns=['date'])
    
    # Encoding Categorical Variables
    encoder = preprocessing.LabelEncoder()
    cols = ['family', 'city', 'state', 'store_type', 'locale', 'locale_name', 'day_type']
    for col in cols:
        processed_data[col] = encoder.fit_transform(processed_data[col])
    
    # Making Predictions
    def predict(X, model= Loaded_object['model']):
        results = model.predict(X)
        return results
    
    prediction = predict(processed_data, model= Loaded_object['model'])
    df['Sales']= prediction 
    
    
    # Displaying prediction results
    st.markdown('''---''')
    st.markdown("<h4 style='text-align: center;'> Prediction Results </h4> ", unsafe_allow_html=True)
    st.success(f"Predicted Sales: {prediction[-1]}")
    st.markdown('''---''')

    # Making expander to view all records
    expander = st.expander("See all records")
    with expander:
        df = pd.read_csv(tmp_df_file)
        df['Sales']= prediction
        st.dataframe(df)
