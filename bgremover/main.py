import requests
from PIL import Image

url = "https://o.remove.bg/downloads/940146a3-c56d-40e7-9dcd-dad5d5889635/adwords-793034_1920-removebg-preview.png"

response = requests.get(url)
image = Image.open(response.content)

# Remove the background script
image.putalpha(0)

# Save the image
image.save("tux_no_background.png")
