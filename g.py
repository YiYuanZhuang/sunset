# Import the necessary modules
import os

# Define the paths to the image and audio files
image_path = 'C:/Users/ZJH/Desktop/static/static/sunset.jpg'
audio_path = 'C:/Users/ZJH/Desktop/static/static/meet.m4a'

# Define the HTML code to display the image and play the audio
html_code = '''
<html>
  <head>
    <title>My Webpage</title>
  </head>
  <body>
    <h1>Welcome to my webpage!</h1>
    <img src="{image}" alt="My Image">
    <audio controls>
      <source src="{audio}" type="audio/mpeg">
    </audio>
  </body>
</html>
'''.format(image=image_path, audio=audio_path)

# Write the HTML code to a file called "index.html"
with open('index.html', 'w') as f:
    f.write(html_code)

# Commit the "index.html" file to the Github repository
os.system('git add index.html')
os.system('git commit -m "Add index.html"')
os.system('git push')
