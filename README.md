# VoxGPT
This is a Repository for VoxGPT application. The application is implemented in python 

Libraries used: speech_recognition, pyttsx3, openai

Functionlity:

1.	User Interaction: The app provides a user-friendly interface that allows users to interact with the application using speech. Users can speak their prompts or questions into the app, eliminating the need for typing.
2.	Speech-to-Text Conversion: The app utilizes a speech recognition system to convert the user's spoken prompts into text format. This may involve integrating a speech recognition API or library that can accurately transcribe spoken words into text.
3.	Prompt Processing: Once the user's spoken prompt is converted into text, the app performs necessary processing on the text. This may include removing any irrelevant or unnecessary information, normalizing the text, or applying any specific formatting or structure required for the GPT API.
4.	API Integration: The app connects to the GPT API, sending the processed prompt as a request and retrieving the generated response. This involves making API calls using appropriate libraries or SDKs, including the processed prompt as input, and receiving the generated text response.
5.	Text-to-Speech Conversion: The app takes the generated text response and converts it into speech format. This can be achieved by integrating a text-to-speech (TTS) system or service that can convert the text into an audio file or real-time speech output. The TTS system may require selecting appropriate voice options, adjusting speech parameters, and generating high-quality speech output.
6.	Speech Output: The app plays the generated speech response to the user. Depending on the platform, you'll utilize the appropriate audio playback functionality to ensure the user can hear the response clearly. This can involve using built-in audio playback features or integrating audio player libraries.
