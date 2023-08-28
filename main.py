import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    while(True):
        print("Welcome to the Robo Speaker created by VS")
        sample = input("Enter what you want me to speak:")
        if(sample == "q"):
            engine.say("Bye Bye friend")
            engine.runAndWait()
            break
        engine.say(sample)
        engine.runAndWait()
