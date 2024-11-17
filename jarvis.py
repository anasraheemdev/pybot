import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Ya Assiatant Spaking k liya hy 
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speech kr rha hy
def listen():
    with sr.Microphone() as source:
        print("Sun rha ho bhi tu bol...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Mazrat Bhi jaan , I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, the service is down.")
            return ""

# Function to set a reminder
def set_reminder(task, time):
    speak(f"Reminder set for {task} at {time}.")
    # You can store this in a file or a database

# Function to create a to-do list
def add_to_todo_list(item):
    with open("todo_list.txt", "a") as file:
        file.write(f"{item}\n")
    speak(f"Added {item} to your to-do list.")

# Function to search the web
def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Main function
def main():
    speak("Hello, My name is Annnas Raheeem Bot , how can I assist you today?")
    while True:
        command = listen()

        if 'reminder' in command or 'remainder' in command:
            speak("What is the task?")
            task = listen()
            speak("At what time?")
            time = listen()
            set_reminder(task, time)

        elif 'to-do' in command or 'add' in command:
            speak("What would you like to add to your to-do list?")
            item = listen()
            add_to_todo_list(item)

        elif 'search' in command:
            speak("What do you want to search for?")
            query = listen()
            search_web(query)

        elif 'Who Developed You' in command or 'who developed you' in command or 'who made you' in command or 'made you' in command:
            speak("I was developed by Muhammad Annas Raheem on 25th August 2024 on 4 : 30 PM when he was the CEO of Synovate Technologies")
            query = listen()
            search_web(query)

        elif 'How are You' in command or 'How are u' in command or 'how are' in command or 'are you' in command:
            speak("I am Fine Sir, Thanks For Asking. How Can I help You today")
            query = listen()
            search_web(query)

        elif 'Can You tell me more about Annas Raheem' in command or 'Can you tell me more' in command or 'Can you' in command or 'more about anas rahim' in command:   
            speak("Anas Raheem is an ambitious individual currently pursuing a degree in Artificial Intelligence from Air University. He has a strong foundation in web development, with expertise in languages and frameworks such as C, C++, HTML, CSS, JavaScript, PHP, Laravel, React.js, and WordPress. Since February 2022, he has been freelancing in website development, and he founded a company named Tech Servent to provide web solutions, including e-commerce and business services. Anas has also gained professional experience through his work with Tricon Technologies and Trndza.pk. Beyond technical skills, he has contributed to the community by volunteering with the Niaz Foundation NGO to educate orphans. Recently, Anas has been focusing on professional content writing, SEO optimization, and developing projects like a functional calculator using HTML, CSS, and JavaScript/jQuery. He is also working on a full-fledged AI voice assistant named Jarvis utilizing Python and OpenAI's API to create a versatile and responsive tool that understands voice commands and performs various tasks.")
            query = listen()
            search_web(query)

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()