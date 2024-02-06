import os

voice = os.listdir('voice')

for i in range(len(voice)):
  voice[i] = int(voice[i][:-4])

voice.sort(reverse=True)

new_file_name = voice[0] + 1
print(str(new_file_name) + ".mp3")