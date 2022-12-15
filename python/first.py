import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak (audio):
 engine.say(audio)
 engine.runAndWait()


def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour >=0 and hour<12:
  speak("Good Morning sir")
 elif hour > 12 and hour <18:
  speak("Good afternoon sir")
 else:
  speak("good evening sir")


 speak("I am your assistant ATST sir. please tell me How may i help you sir.")

def takeCommand():
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Listening....")
  r.pause_threshold = 1
  audio=r.listen(source)

  try:
   print("Recognizing....")
   query = r.recognize_google(audio, language='en-in')
   print(f"User said: {query}\n")

  except Exception as e:
   #print(e)

    print("say that again please ...")
    return "None"
  return query

if __name__ == "__main__":
 wishMe()
takeCommand()