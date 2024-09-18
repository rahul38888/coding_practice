import whisper
from scipy.io import wavfile

model = whisper.load_model("medium")

audio = wavfile.read("audio.wav")[1]
transcribed = model.transcribe(audio)

text = transcribed["text"]

if __name__ == '__main__':
    print(text)