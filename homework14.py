import datetime, random
from gtts import gTTS
import speech_recognition as sr

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("It's %I:%M %p")  # 12-hour format
    tts = gTTS(text=time_str, lang=lang)
    tts.save(filename)
    print("Time:", time_str)

def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    '''
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said: no problem, I’ll go to sleep.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    joke = random.choice(jokes)
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)
    print("Joke:", joke)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.
    '''
    now = datetime.datetime.now()
    date_str = now.strftime("Today is %A, %B %d, %Y.")
    url = f"https://calendar.google.com/calendar/r/month/{now.year}/{now.month}/1"
    tts = gTTS(text=date_str, lang=lang)
    tts.save(audiofile)
    print("Date:", date_str)
    return url

def personal_assistant(lang, filename):
    '''
    Listen to the user and respond appropriately.
    '''
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say something like: What time is it? What day is it? Tell me a joke!")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language=lang)
        command = command.lower()
        print("You said:", command)

        if "time" in command:
            what_time_is_it(lang, filename)
        elif "day" in command or "date" in command:
            url = what_day_is_it(lang, filename)
            print("Check calendar at:", url)
        elif "joke" in command:
            tell_me_a_joke(lang, filename)
        else:
            text = "Sorry, I didn't understand that."
            tts = gTTS(text=text, lang=lang)
            tts.save(filename)
            print(text)

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Speech Recognition service error:", e)
