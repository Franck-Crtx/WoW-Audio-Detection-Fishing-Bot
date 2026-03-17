import pyaudio

print("--- Recherche des périphériques GoXLR ---")
p = pyaudio.PyAudio()
count = p.get_device_count()

for i in range(count):
    dev = p.get_device_info_by_index(i)
    # On affiche tout ce qui peut recevoir du son
    if dev['maxInputChannels'] > 0:
        print(f"ID {i}: {dev['name']}")

p.terminate()
print("--- Fin de la liste ---")
