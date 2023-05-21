import speech_recognition as sr
import pyttsx3
import openai

# Create an instance of the recognizer class
speachReconizer = sr.Recognizer()

# Initialize the pyttsx3 engine
textEngine = pyttsx3.init()

# Second till listner will stop listing
sec = 5

openai.api_key = 'YOUR_API_KEY'  # Replace with your API key

# Call openai and send the query to get response
def send_prompt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the language model
        prompt=prompt,
        max_tokens=50,  # Adjust the value as per your requirement
        temperature=0.8,  # Adjust the value as per your requirement
        n=1  # Number of responses to generate
    )

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        return None
    
# Set the voice properties for the selected emotion
textEngine.setProperty("rate", 150)
textEngine.setProperty("volume", 1)
textEngine.setProperty("voice", "english")

# Use the microphone as source of audio input
with sr.Microphone() as source:
    print("Speak anything: ")
    # Adjust for ambient noise
    speachReconizer.adjust_for_ambient_noise(source)

    # Continuously listen for audio until there is 5 seconds of silence
    audio_data = speachReconizer.listen(source, phrase_time_limit=sec)

    try:
        # Recognize speech using Google Speech Recognition
        text = speachReconizer.recognize_google(audio_data, language="en-US")

        # Get the recognized text
        words = text.split() if isinstance(text, str) else []
        text_without_silence = " ".join(word for word in words if isinstance(word, str))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

prompt = text_without_silence

# Use GPT api here 
gptResponse = send_prompt(prompt)

# Convert text to speech
textEngine.say(gptResponse)

# Run the pyttsx3 engine
textEngine.runAndWait()
