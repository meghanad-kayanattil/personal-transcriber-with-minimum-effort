from threading import Thread
import pyaudio
import streamlit as st
import queue
from threading import Thread
import helper_functions as hf

# Defining a call back function to use with pyaudio recording stop button
def callback():
    st.session_state['control loop'] = False
    messages.get()

# Initialize 3 queues for recording and outut and to chen when to start and stop recording
messages = queue.Queue()
recordings = queue.Queue()
output = queue.Queue()

st.title("Personal transcriber 🎤")

st.write("""
### A simple speech to text app
""")
# Create option list for recording devices available
p=pyaudio.PyAudio()
list_device = []
for i in range(p.get_device_count()):
    list_device.append(p.get_device_info_by_index(i)['name'])
p.terminate()
device = st.selectbox(label='Select the corresponding input device', options=list_device)
for index, d in enumerate(list_device):
    if d==device:
        break

st.session_state['control loop'] = True
# Start recordning and transcribing if the button is pressed
if st.button(label = 'Record', key = 'start'):
    messages.put(True)
    record = Thread(target=hf.record_microphone, args=(messages, index, recordings,))
    record.start()
    transcribe = Thread(target=hf.speech_recognition, args=(messages, recordings, output,))
    transcribe.start()
    st.write('Recording started with '+ str(device)+' of index = '+str(index)+' There will be a small delay between recording and the transcription being produced, thank you for your patience')    

    # Stop recording if the stop button is pressed 
    if st.button("Stop recording", key = 'stop_'+str(i), on_click=callback):
        st.write("Recording stopped")

    # creating a placeholder for the fixed sized textbox
    logtxtbox1 = st.empty()
    logtxt = ""
    while st.session_state['control loop'] == True:
        logtxt += output.get()
        logtxtbox1.text_area("Live transcribe: ", logtxt, height = 500)
        st.session_state['logged text'] = logtxt
# Show final transcript post recording
if st.button("Show final tanscipt"):
    st.write(st.session_state['logged text'])
