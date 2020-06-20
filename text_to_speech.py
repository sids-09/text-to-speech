#!/usr/bin/env python
# coding: utf-8

# In[4]:


from gtts import gTTS 
import os 
text='Hi my name is Siddhesh and I am studying at IIT Indore.'
language='en'
voice=gTTS(text=text,lang=language,slow=False) 
voice.save("voice.mp3") 
os.system("mpg321 voice.mp3") 

