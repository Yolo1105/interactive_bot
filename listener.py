import pvporcupine
import pyaudio
import struct
import subprocess

# Initialize Porcupine with the wake word
porcupine = pvporcupine.create(keywords=["hey chatgpt"])

# Open the microphone stream
pa = pyaudio.PyAudio()
stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length)

print("Listening for the wake word...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        # Detect the wake word
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Wake word detected, launching the ChatGPT interaction script...")
            subprocess.Popen(["python", "chatgpt_interaction.py"])  # Launch the interaction script
            break

except KeyboardInterrupt:
    print("Listener terminated")

finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
    porcupine.delete()
