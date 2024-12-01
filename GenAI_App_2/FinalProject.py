'''FINAL PROJECT - DS & Gen AI Internship (Nov 11-Dec 19, 2024)
AI powered Web Application for Visually Impaired Users

submitted by : Abhinaya A.S.(IN9240740)'''

# IMPORTING REQUIRED DEPENDENCIES
import streamlit as st # to design application interface
from PIL import Image # to load the user uploaded image
import time # to keep track of progress when the app functions
import google.generativeai as genai # to borrow and configure the LLM
from gtts import gTTS # to deal with text-to-speech conversion & audio
import cv2 # for object detection purpose
import numpy as np # to convert the image into model friendly manner

# CONFIGURING MODEL FROM GOOGLE AI

# accessing the API key
# API key is confidential, hence stored in a text file in the project folder and not explicitly written
f = open("Keys/GeminiDemo2.txt")
key = f.read()
# configuring the API key
genai.configure(api_key = key)

# instruction to the model
# what I want the LLM to do?
# how do I customize the LLM to behave according to cases?
# system prompt - Functionality 01
sys_1 = '''You are meant to help blind or visually impaired user. The blind or visually impaired user will upload an image. 
You should help the user to visualize and understand the image by describing it.
Remember, the user is blind, so you should describe the scene in a way that they can understand and relate. 
Your description shall not exceed 400 words. 
'''
# system prompt - Functionality 02
sys_2 = '''You are meant to help blind or visually impaired user. The blind or visually impaired user will upload an image.
Your task is to help the user read the text in the image. So, all you need to do is to extract text from within the image like an OCR and output the extracted text as a string.
The text you extract will be converted to speech audio and will be delivered to the user. 
If there is no text in the image, return the text string "No text detected".
'''

# system prompt - Functionality 03
sys_3 = '''You are meant to help blind or visually impaired user. The blind or visually impaired user will upload an image.
You should detect objects in the uploaded image and 
you should write a brief description including the name and the relative position of the object in a pointwise manner. 
Eg. "There is a dog on the bottom left corner, behind a tall piller". In doing so, your aim is to offer insights to enhance user safety and situational awareness
for safe navigation. If there are no objects in the image, like if the image has only text or if the image is blank, politely inform it to the blind user.'''

# system prompt - Functionality 04
sys_4 = '''You are meant to help blind or visually impaired user. The blind or visually impaired user will upload an image.
Your task is to provide task-specific guidance to the user based on the uploaded image. 
You will have to recognize items, read labels, provide context-specific information according to the uploaded image. Your aim should be to help the blind user
do the specific task associated with the image. If the image does not imply a specific task, politely inform it to the user. Need not ask the user any question.
'''

# setting up the model
# here, we have chosen gemini-1.5-flash model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# to detect and highlight objects, we need an object detection model
# to know in detail about this model, please refer the notebook "Prerequisites.ipynb"
# Load YOLO model (pre-trained)
# the files "yolov4.weights", "yolov4.cfg", "coco.names" should be downloaded and saved in the project directory
model3_1 = cv2.dnn.readNet('yolov4.weights', 'yolov4.cfg')
# Loading class labels of YOLO
with open('coco.names', 'r') as f :
    classes = [line.strip() for line in f.readlines()]
# getting names of the layers in model3_1
layer_names = model3_1.getLayerNames()
# identifying the output layers
output_layers = [layer_names[i-1] for i in model3_1.getUnconnectedOutLayers()]


# BUILDING THE WEB APP UI

# giving a title to the app's UI - name of the web app
st.title(":cyclone: :robot_face: :rainbow-background[ :violet[ __INFI__]:green[__SIGHT__]]:eye-in-speech-bubble: ")

# a brief slogan that describes the web app, sort of a USP(Unique Selling Proposition)
st.markdown(
    """
    <p style="color: black; font-family: 'Comic Sans MS'; font-size: 16px;">
        Get Infinite Sight with INFISIGHT powered by Generative AI....
    </p>
    """,
    unsafe_allow_html=True)

# drawing a horizontal rule in the UI below the main title
# to demarcate a new section
st.subheader("", divider="orange")

# including a small polite message for the user
# this message will be read out by the visually impaired user's screen reader
# it gives the user an idea about what is there next in the UI and also what to do
# it also takes into account the case were the user will use the web app a 2nd time
st.write('''__To know about how we can help you, please expand and read the following "What we offer" section. You need not do this if you're already a user and is familiar with us.__ :smile:''')
# the blind user will now wait for the screen reader to announce the word "What we offer" to expand it by pressing enter

with st.expander(":green[__What We Offer?__]", expanded=False):
    # expander is set to False in order to consider 2nd time users
    # for them it is a wastage of time if the screen reader will go on reading the message in the expander
    st.markdown(
        """
        <p style="color: purple; font-family: 'Comic Sans MS'; font-size: 24px;">
        Welcome, friend! We are pleased to help you.
        </p>
        <p style="color: green; font-family: 'Comic Sans MS'; font-size: 18px;">
        You can upload an image you wish to explore, on our platform. We can help you by doing any of the following 4 tasks :
        <ol style="color: green; font-family: 'Comic Sans MS'; font-size: 18px;">1. giving real time scene description using our <b>"Describe Scene"</b> feature</ol>
        <ol style="color: green; font-family: 'Comic Sans MS'; font-size: 18px;">2. extracting text from the image you have uploaded and reading it aloud using our <b>"Read for me"</b> feature</ol>
        <ol style="color: green; font-family: 'Comic Sans MS'; font-size: 18px;">2. detecting objects in the image you have uploaded using our <b>"What's there on my path?"</b> feature</ol>
        <ol style="color: green; font-family: 'Comic Sans MS'; font-size: 18px;">2. providing task-specific guidance based on the image you have uploaded using our <b>"Help me do"</b> feature</ol>  
        </p>
        """,unsafe_allow_html=True)
        # this message will convey the functionalities offered by this web app

# beginning a new section, horizintal rule
st.subheader("", divider="orange")

# brief instruction to the user
st.write("Please upload an Image file below:")
st.write(":warning:__Only 1 file shall be uploaded__")

# make a facitlity for the user to upload their image file
uploaded_file = st.file_uploader(
    "Upload Image File (png, jpg, jpeg or gif)",
    type=["png", "jpg", "jpeg", "gif"],  # Specify allowed image formats
    accept_multiple_files=False           # Don't Allow multiple file uploads
)

if uploaded_file:
    # give user a small message
    st.write(":violet[__Hey friend! below we have displayed the image you just uploaded :smile:__]")
    # display the uploaded image to the user
    with st.container(height=200, key="img"):
        # Open the image using PIL
        input_img = Image.open(uploaded_file)
        st.write("__The image you have uploaded :__ The image is displayed in a scrollable rectangular box of height 200px. ")
        # Display the image using PIL
        st.image(input_img, caption="", use_container_width=True)
"This is just below and outside the rectangular box in which the uploaded image is displayed"
# again clear and polite instruction to the user
# making them aware of what's next in the UI & what to do
st.write('''Now please choose all the features you want to use by 
         clicking on the buttons given below and then click the submit button. Name of the features are written on the respective buttons. Please press 'Enter' as soon as your screen reader reads the button names :''')

# enabling clickable buttons for the user for selecting features
options = [":violet-background[:violet[__Describe Scene__]]", ":violet-background[:violet[__Read for me__]]", ":violet-background[:violet[__What's on my way__]]", ":violet-background[:violet[__Help me do__]]"]
selection = st.pills("Features", options, selection_mode="multi")

# enabling a button for the user to submit the image and service requests
btn_click = st.button(":green-background[:green[__Submit__]]")

if uploaded_file:

    # the submit button should only be enabled once the file is uploaded
    if btn_click==True:

        # now we need to show progress bar and message to the user, because the llms will take time to generate their response
        # let's start the timer before we request the models to generate responses
        start = time.time()

        # Initialize a progress bar in Streamlit at 0%. 
        # It can be updated with value 100%, once the models have generated responses
        progress = st.progress(0)

        # let's show a message to the user with a spinner
        # also we will call the models to generate responses
        with st.spinner(''':violet[__Please wait :hourglass_flowing_sand: while we go through :mag:
                        the image you have uploaded for generating requested responses...:smile:__]'''):
             # for each of the selected feature, call the corresponding (model+system prompt)
             if ":violet-background[:violet[__Describe Scene__]]" in selection:
                 response_1 = model.generate_content([input_img, sys_1])
                 progress.progress(25)
             if ":violet-background[:violet[__Read for me__]]" in selection:
                 response_2 = model.generate_content([input_img, sys_2])
                 if response_2.text != "No text detected":
                     tts = gTTS(response_2.text)
                     tts.save("output.mp3")
                 progress.progress(50)
             if ":violet-background[:violet[__What's on my way__]]" in selection:
                 # OBJECT DETECTION
                 # loading the uploaded image into Open CV's pipeline
                 # Convert PIL image to OpenCV format (NumPy array)
                 input_img = input_img.convert("RGB")
                 img = np.array(input_img)
                 # extracting dimensions of the image
                 height, width = img.shape[0], img.shape[1]
                 # converitng the image into YOLO-friendly blob
                 blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0,0,0), True, crop=False)
                 # feeding the blob into model3_1
                 model3_1.setInput(blob)
                 # getting output from the deep net
                 outs = model3_1.forward(output_layers)
                 # collecting and organizing informations about detected objects
                 boxes, confidences, class_ids = [], [], []
                 for out in outs:
                     for detection in out:
                         scores = detection[5:]
                         class_id = np.argmax(scores)
                         confidence = scores[class_id]
                         if confidence > 0.5:
                             center_x = int(detection[0] * width)
                             center_y = int(detection[1] * height)
                             w = int(detection[2] * width)
                             h = int(detection[3] * height)
                             x = int(center_x - w / 2)
                             y = int(center_y - h / 2)
                             boxes.append([x, y, w, h])
                             confidences.append(float(confidence))
                             class_ids.append(class_id)
                 # removing overlapping or redundant bounding boxes
                 indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                 # getting interpretable labels of valid detections
                 detected_objects = []
                 for i in range(len(boxes)):
                      if i in indexes:
                           x, y, w, h = boxes[i]
                           label = str(classes[class_ids[i]])
                           detected_objects.append(label)
                           # drawing the bounding boxes around detected objects
                           cv2.rectangle(img, (x, y), (x + w, y + h), (200, 255, 0), 2)
                           # putting labels for boxes
                           cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                 
                 response_3 = model.generate_content([input_img, sys_3])
                 progress.progress(75)
             if ":violet-background[:violet[__Help me do__]]" in selection:
                 response_4 = model.generate_content([input_img, sys_4])

        # End the timer as responses have been generated
        end = time.time()

        # Calculate elapsed time
        elapsed_time = end - start
        st.write(f":green[__Response has been generated in {elapsed_time:.2f} seconds.__]")

        # Now update progress bar to 100% 
        progress.progress(100)

        # organizing OUTPUTS
        # Custom CSS for the container
        st.markdown("""<style>.custom-container {border: 6px solid #4CAF50; /* Green border */
                    padding: 20px;
                    border-radius: 10px; /* Rounded corners */
                    margin-bottom: 20px;}</style>""",unsafe_allow_html=True)


        # for each feature selected output shall be displayed in a container
        if ":violet-background[:violet[__Describe Scene__]]" in selection :
            st.write(":orange[___Describe Scene; the real time scene description___]")
            with st.container(border = True, key = "feat1"):
                st.write(":green-background[:violet[__The following is the requested Real time Scene description__ :]]")
                st.markdown('<div class="custom-container">'+response_1.text, unsafe_allow_html=True)
                # st.markdown(response_1.text, unsafe_allow_html=True)
        
        if ":violet-background[:violet[__Read for me__]]" in selection :
            st.write(":orange[___Read for me; Text-to-Speech Conversion for Visual Content :___]")
            with st.container(border = True, key = "feat2"):
                if "No text detected" in response_2.text :
                    st.write(":green-background[:violet[__Sorry! :pleading_face: The image you have uploaded doesn't contain any text content. We can only process the text that is directly visible from the image.__]]")
                else :
                    st.write(":green-background[:violet[__The following is the requested audio of the extracted text from the image__]]")
                    st.audio("output.mp3")

        if ":violet-background[:violet[__What's on my way__]]" in selection :
            st.write(":orange[___What on my path?; the object and obstacle detection for safe navigation :___]")
            with st.container(height=480, border=True, key='obj'):
                st.image(img, caption=":blue[__Detected Objects__]", use_container_width=True)
            with st.container(border = True, key = "feat3"):
                st.write(":green-background[:violet[__The following is the requested Object or Obstacle detection :__]]")
                st.markdown('<div class="custom-container">'+response_3.text, unsafe_allow_html=True)

        if ":violet-background[:violet[__Help me do__]]" in selection :
            st.write(":orange[___Help me do; Personalized Assistance for Daily Tasks___ :]")
            with st.container(border = True, key = "feat4"):
                st.write(":green-background[:violet[__The following is the requested task specific guidance related to the image :__]]")
                st.markdown('<div class="custom-container">'+response_4.text, unsafe_allow_html=True)


else :
    if btn_click == True:
        st.write("__Sorry! :pleading_face: You have not uploaded any image file....__")









    
