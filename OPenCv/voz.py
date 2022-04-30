import pyttsx3

engine=pyttsx3.init()

engine.setProperty("rate",158)
engine.say("Azul")
engine.say("Rojo")
engine.say("Verde")
engine.say("Amarillo")
engine.say("Naranjo")

engine.runAndWait()