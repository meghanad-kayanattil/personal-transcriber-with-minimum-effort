# A low code personal speech to text transcriber

The project uses, three popular opensource libraries to implement the speech to text transcriber:

<code>Pyaudio</code> :  for handling the audio recording devices
<code>Vosk</code> : For implementing the simple speech to txt transcription (Libraries like <code>SpeechRecognition</code> can also be used instead of vosk)
<code>Streamlit</code> : For creating the interactive user inteface as shown in the image below:


## Screen shots

![App Screenshot](https://github.com/meghanad-kayanattil/personal-transcriber-with-minimum-effort/blob/main/Screenshot.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/meghanad-kayanattil/personal-transcriber-with-minimum-effort
```

Go to the project directory



Create a virtual env and Install dependencies

```bash
  conda create --name virt_env
  conda activate virt_env
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```
You now have the app running in your system locally!
 
## References

The project was inspired based on [this](https://www.youtube.com/watch?v=2kSPbH4jWME&list=PLR04b6DveHfwoX2Z1Zwk84c2f48sDm6dF&index=1&t=1401s&ab_channel=Dataquest) video

