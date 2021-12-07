import speech_recognition as sr
import json


def speechToText(audio, languageCode="en-MX"):
    # obtain path to "english.wav" in the same folder as this script
    from os import path
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")

    try:
        AUDIO_FILE = audio
        # use the audio file as the audio source
        r = sr.Recognizer()

        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition

        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        res = {
            "fail": False,
            "text": r.recognize_google(audio, language=languageCode)
        }

        return res
    except sr.UnknownValueError:
        res = {
            "fail": False,
            "text": "Speech Recognition could not understand audio"
        }

        return res

    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

        res = {
            "fail": False,
            "text": "Speech Recognition failed to connect to service"
        }

        return res

    except Exception as e:
        res = {
            "fail": False,
            "text": "Error al momento de procesar tu audio, verifica el formato del audio e intentalo mas tarde"
        }

        return res
