## **BUILDING AN 'AI Code Reviewer' web app**

#### **Overview**
Generative AI is very powerful. Ever thought of building applications like Chat GPT, that leverages pre-built Large Language Models? Here, I have tried to build an "AI Code Reviwer " web app using Google AI's pre-built LLM 'gemini-1.5-flash'.

#### **Goal**
    * to build an AI code reviewer web app leveraging Gen AI
    * use any of the Google AI's avalilable LLM to generate review of the Python code written by the user
    * use streamlit library to create a beautiful, simple, neat UI for the web app

####  **How to get acess to Google AI's LLM**
    * companies like Open AI, Google AI have developed various powerful LLMs
    * to enhance our Generative AI applications, we can take help of these LLMs
    * to access Google AI's LLM, follow these steps :

        1. Go to the **Google Cloud Platform** [here](https://console.cloud.google.com)
        2. Click on "**console**" in the top RHS corner
        3. Click on "**Dashboard**"
        4. Select a Project you want to work with from the drop-down located at the top-left corner, adjacent to the Google Cloud logo or you can create a new project also in the same section and then select it
        5. We have to generate an API key to be able to access & use Google AI's models.So, go to the "**Google AI studio**" [here](https://aistudio.google.com)
        6. Click on **Get API key**
        7. Click on **Create API key** & select our current project
        8. Click **Create API key in existing project** & copy the generated key
        9. Store this key in a text file

#### **Building the Web App**
 
All details like :

* how to configure the api key generated
* how to access the Google AI's LLM
* using functionalities of google.generativeai library 
* writing suitable system prompt
* designing UI using streamlit

are available as comments and code in the **CodeReviewer.py** file.

Also find the output in my linkedin post [here]()



