## **OVERVIEW**
  * Visually impaired individuals often face challenges in
      - understanding their environment
      - reading visual content
      - performing tasks that rely on sight


## **PROBLEM STATEMENT**

  * Leverage Generative AI to assist visually impaired individuals in perceiving and interacting with their surroundings
  * Build an intelligent, adaptable, user-friendly solution that provides:
      - Real-time scene understanding
      - Text-to-speech conversion for reading visual content
      - Object and obstacle detection for safe navigation
      - Personalized assistance for daily tasks
  * **Allowed Utilities for Implementation :**
    1. Streamlit
    2. Google generative AI
    3. Python

## **GOAL**

  1. Develop an AI-powered application using Streamlit that provides assistive functionalities through image analysis. 
  2. The application should allow users to upload an image
  3. The application should implement at least 2 of the following functions
      (i) **Real-Time Scene Understanding**
          - generate descriptive textual output that interprets the content of the uploaded image
          - enable users to understand the scene effectively
      (ii) **Text-to-Speech Conversion for Visual Content**
          - extract text from the uploaded image using OCR techniques
          - convert that text into audible speech for seamless content accessibility
      (iii) **Object and Obstacle Detection for Safe Navigation**
          - identify objects/obstacles within the image
          - highlight those objects
          - offer insights to enhance user safety and situational awareness
      (iv) **Personalized Assistance for Daily Tasks**
          - provide task-specific guidance based on the uploaded image
          - recognize items, read labels, provide context-specific information


## **Exploring the Problem Domain**

**Q : What are the different types of visual impairments?**
   
   1. **Low Vision** characterised by reduced clarity, contrast sensitivity, or field of vision that glasses or lenses cannot fully correct
   2. **Blindness** viz. the complete or near-total lack of visual perception
   3. **Color Blindness** viz. the difficulty in distinguishing certain colors

**Q : What are the strengths of visually impaired individuals which they develop over time?**
    
* their sense organs except eyes are enhanced in terms of functionality
* they develop stronger reliance on hearing, touch, and spatial awareness.
* they use sound and hearing for navigation, communication, and environmental awareness
* they are highly sensitivity to tactile information (e.g., Braille, textures)
* they are proficiency in using accessible tools and assistive software (e.g., voice assistants, screen readers)
* they are skilled in alternative input methods such as voice commands or tactile devices
* they have enhanced memory and problem-solving skills for tasks like navigation or identifying objects using alternative cues
* they are skilled in using mental mapping and spatial reasoning to compensate for lack of visual input

**Q : Some of the visually impaired people may be blind by birth. How do these people learn language?**
 * they rely entirely on auditory and tactile input for learning language
 * they cannot associate words with visual images, but rather with sounds, textures, and physical experiences only
 * Eg. they learn words like "red" or "bright" conceptually; "red is associated with heat or intensity"
 * they use touch to associate objects with their names (e.g., feeling a ball while hearing the word "ball")
 * they may learn Braille script early as a means of literacy
 * they use tone, pitch, and context of speech for understanding meaning
 * they also develop strong auditory memory for language acquisition

**Q : Some of the visually impaired people may have become blind due to some accidents. How do such people try to cope up with their environment?**
 * they are already aware of the language
 * they can retain visual memories
 * they can associate language with pre-existing visual knowledge (e.g., "tree" evokes a visual image from memory)
 * they will usually undergo a transition from visual learning to relying on auditory and tactile cues
 * for such people it is easier to learn Braille because they are familiar with written language visually
 * may face challenges in adapting communication habits if they heavily relied on visual cues, such as lip-reading or observing body language
     
**Q : Summarize the differences between the 2 categories of blind people discussed above.**
  
| Aspect| Blind by Blind| Blind Due to Accident|
|------|------|-------|
| **Language Learning**      | Auditory and tactile-focused; conceptual imagery | Initially visual, shifts to auditory/tactile |
| **Visual Knowledge**       | No visual references; conceptual understanding  | Strong visual memories; may fade over time   |
| **Communication**          | Verbal focus, limited gestures                  | Visual references and retained gestures       |
| **Social Adaptation**      | Intuitive reliance on sound and touch           | Adjustment required to new sensory reliance  |

**Q : What are screen readers?**
  * they are assistive software tools 
  * designed to help people who are blind or visually impaired use computers, smartphones, and other devices
  * work by converting text and other visual elements on a screen into speech, Braille output, or both
  * enables visually impaired users to interact with digital content, applications, and web pages

**Q : How do screen readers work?**
  * identifies text on the screen and reads it aloud using synthetic speech
  * users can control how the contents on the screen is read (e.g., line-by-line, word-by-word, or character-by-character)
  * provide keyboard shortcuts or gesture-based commands to navigate through content:
    1. Moving between headings, links, buttons, and other elements
    2. Skipping to sections like "next paragraph" or "previous heading"
  * interpret web and application elements:
    - Links: Indicating clickable hyperlinks
    - Buttons: Announcing interactive controls
    - Forms: Describing input fields, labels, and instructions

 **Q : List out the features of screen readers that are specifically helpful for visually impaired.**
  * Users can adjust the reading speed and voice type for comfort
  * Navigate web pages by headings, landmarks, links, tables, and more
  * Heavily reliant on keyboard shortcuts for efficiency
  * Provide information about the context of elements (e.g., "button," "link," "checkbox")
  * Users can hear text spelled out or correct mispronunciations of specific words

**Q : Give examples of some popularly used screen readers.**
  JAWS (Job Access With Speech), NVDA (NonVisual Desktop Access), VoiceOver, Narrator

**Q : Suggest some app design flaws that can bother the smooth functioning of screen readers**.
  * Streamlit widgets like st.button(), st.slider(), and st.selectbox() without meaningful labels and help text.
  * Not using elements like st.title(), st.header(), and st.subheader() to create a logical hierarchy for screen readers.
  * not using the caption parameter or st.markdown() to describe visual elements like charts, images, or graphs.
  * Streamlit doesn’t directly support alt text for visualizations, so not describing the key insights in text form using st.write() will not help screen reader to serve their true purpose
  * Streamlit’s default widgets are keyboard-navigable. Using custom JavaScript or CSS that may disrupt this functionality.
  * Streamlit doesn’t natively support adding ARIA roles directly. So, not using st.markdown() to embed custom HTML if necessary.
  * Screen readers may struggle to identify changes in dynamic content. So, not using st.toast() or clear textual updates with st.write() to inform users of changes.
  * Do not rely on color alone to convey information (e.g., green for "success," red for "error"). Hence, not adding text-based indicators alongside color.
  * No sufficient contrast between text and background colors.
  * not providing links to skip to specific sections using markdown or buttons, provided the app has long pages
  * Overly dynamic or visually cluttered pages can confuse screen readers.

### **Key Learnings used in this project**
   * ✅ google.generativeai library 🔍
   * ✅ streamlit library for web app 🈸 development
   * ✅ UI 👁️‍🗨️ design 💻
   * ✅ writing suitable system prompt to interact with the pre-built LLMs & LVMs 🤖
   * ✅ Prompt engineering ⚙️
   * ✅ documentation reading 📄 & learning 🤓
   * ✅ gTTS 🔊
   * ✅ Object detection using YOLOv4(OpenCV) 🔎

For details about **object detection model** used, refer the notebook **Prerequisites.ipynb**.
