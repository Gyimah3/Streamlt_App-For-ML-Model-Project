
# Deploying a Retail Sales Prediction Model with Streamlit
![image](https://th.bing.com/th/id/R.6d386881a09bda6427e3841c2a942f6e?rik=NIxpybYcM0cagg&pid=ImgRaw&r=0)


# INTRODUCTION

## Why Prediction?

Companies can improve their products and services based on consumer needs by applying machine learning algorithms to their data. They can also better predict consumer behavior, which means they will plan more accurately.

The commercial application of machine learning is more evident in business processes like marketing, planning, and sales forecasting than in others. For example, a salesperson can accurately use predictive analytics to forecast a potential customer’s behavior. This means they can determine/ utilize the most effective plan.

Sales forecasts can be used to identify benchmarks, determine new initiatives’ incremental impacts, plan resources in response to expected demand, and project future budgets. This article will show how to implement an ML model to predict sales.

The data for this demonstration can be found on GitHub and the full code as well.

Gyimah3/Store-Sales — — Time-Series-Forecasting-Regression-project- (github.com)

## Why deployment?

Deployment is the method by which you integrate a machine learning model into an existing production environment to make practical business decisions based on data

In order to start using my model for practical decision-making, it needs to be effectively deployed into production. If anyone cannot reliably get practical insights from my model, then the impact of my model is severely limited.

In order to get the most value out of my machine learning model, it was important to seamlessly deploy it into production so a business can start using it to make practical decisions by using Streamlit.

Here is the link to the app https://huggingface.co/spaces/Gyimah3/App

## Streamlit

Streamlit is an open-source Python app framework for building and deploying web-based data science applications. It allows users to create and share interactive data analyses and machine learning tools without having to write complex web application code. It does all this with a Python script.

# The Process

The workflow is summarized as follows:
* Export ML items
* Set up environment
* Import ML items
* Build interface
* Set up the backend to process inputs and display outputs
* Deploy
* ML Items Export

The first step in the procedure is to export the important components I used for my modeling process from my notebook. The ML Items typically include the encoder, and the model. For ease of access, these items were put together in a dictionary and exported. Pickle was initially imported in this instance because it was being used for exports.

import pickle

The dictionary can then be created and exported with pickle as shown below;

![image](https://github.com/Gyimah3/Streamlt_App-For-ML-Model-Project/blob/main/images2/Screenshot%202023-01-03%20150309.png)

![image](https://github.com/Gyimah3/Streamlt_App-For-ML-Model-Project/blob/main/images2/Screenshot%202023-01-02%20190755.png)

Made an ML dictionary and exported it using Pickle

Keep in mind that the dictionary’s values reflect my encoder, and model.. Additionally, the output file names can be modified as needed.

Since my workflow likely used specific libraries and modules, they also have to be exported with the help of the OS library into a text file called requirements:

## import os

After importing OS, I then exported the requirements with:

### Exporting the requirements
requirements = ‘\n’.join(f’{m.__name__}=={m.__version__}’ for m in globals().values() if getattr(m, ‘__version__’, None))

with open(‘requirements.txt’, ‘w’) as f:

f.write(requirements)

Other things being equal, this should be the last major action you take in your notebook when you are setting up your own. Next up is VS code.

### Setting up my environment

I created a resource folder to hold the ML items I exported from my notebook and the requirements file. VS code was used to open that folder.

To prevent any conflicts with my variables, I used the following code to create a virtual environment, activated it in my terminal, and installed the requirements in my requirements file:

### Creating and activating virtual environment
python -m venv venv; venv\Scripts\activate; python -m pip install -q — upgrade pip; python -m pip install -qr requirements.txt

## Importing ML Items
Next , I defined a function to load my ML items. In my case, I used the code below which has a default value for the file path:

### Function to import the Machine Learning Items
@st.cache(allow_output_mutation=True)

def Load_ml_items(relative_path):

“Load ML items to reuse them”

with open(relative_path, ‘rb’) as file:

loaded_object = pickle.load(file)

return loaded_object

@st.cache, it is used to store the function in cache so that the script doesn’t have to recreate the function each time a change is made.

### Loading the ML_Items
loaded_object=Load_ml_items(‘ML_items’)

## Building my interface
From there I built my interface using the components provided by Streamlit. The most common ones used are:

st.columns(n): to define columns in your workspace. Replace n with the number of columns you want to create
st.sidebar: for a sidebar
st.date_input(): to receive date inputs
st.selectbox(): for a dropdown box
st.number_input(): for number inputs
st.radio(): for a radio
st.checkbox(): for a checkbox
st.expander(): for an expander
st.form(): to create a form to receive inputs from users

## Setting up the backend
After building my interface, I then set up my backend to receive inputs, process them, and return outputs to the user. Here, the workflow must be same as in your notebook, and is typically: Inputs -> Encoding -> Predicting -> Returning predictions.

In my situation, I assigned the inputs to variables after receiving them via Streamlit components. As can be seen in the notebook, I then transformed the variables into a dictionary and a DataFrame and processed them accordingly. I ran the app using

streamlit run “appl_main.py”

To ease the effects of changes in real-time, I set the app to “Always rerun” so that changes reflect in real-time.

## Deployment
One can deploy an app in two ways;

· visit https://streamlit.io/cloud, sign in and connect your GitHub (if you haven’t). You can then select new app and the repo of the app for deployment.

· https://huggingface.co/ ,deploying an app on hugging face

I deployed my app on hugging face by going through the following steps

1. Set up a Hugging Face Account. Create a Hugging Face account here: https://huggingface.co/

2. Create a New Space.

I started by creating new space https://huggingface.co/new-space and choosing streamlit as my SDK. Hugging Face Spaces are Git repositories, meaning that you can work on your Space incrementally(and collaboratively) by pushing commits

3. Upload App Files to your New Hugging Face Space. …

Take a look at this to guide https://huggingface.co/docs/hub/repositories-getting-started to guide you learn about how to create,edit and upload files

4. My Public App was Live

## Notes

Thank you for reading this far, I hope the article was helpful to you.
