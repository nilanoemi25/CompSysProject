import requests
import os
import json

GLITCH_API_URL = "https://gentle-calico-nautilus.glitch.me/upload"  

def upload_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            response = requests.post(GLITCH_API_URL, files={'file': img_file})
            print(response)
            httpBody=json.loads(response.text)
            return httpBody["url"]
    else:
        return json.loads(f'{{"message":"Image not found: {image_path}" }}')
        

if __name__ == "__main__":
    result = upload_image("./images/sensehat_image.jpg")
    print(result)