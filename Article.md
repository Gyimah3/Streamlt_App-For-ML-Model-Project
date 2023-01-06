
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

##Streamlit

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
