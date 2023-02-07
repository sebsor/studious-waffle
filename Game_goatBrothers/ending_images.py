
import requests
import PIL
from PIL import Image

# Alla bockarna dör
# Send a GET request to the website to download the image
def everyoneDies() :
    response = requests.get('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8d13c590-e54f-44a5-8d21-c5c4c3016cc9/d9ctjm6-c76832f4-b393-478d-bc6b-68fba1013a98.png/v1/fill/w_1600,h_900,q_80,strp/mission_failed_screen_by_coulden2017dx_d9ctjm6-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTAwIiwicGF0aCI6IlwvZlwvOGQxM2M1OTAtZTU0Zi00NGE1LThkMjEtYzVjNGMzMDE2Y2M5XC9kOWN0am02LWM3NjgzMmY0LWIzOTMtNDc4ZC1iYzZiLTY4ZmJhMTAxM2E5OC5wbmciLCJ3aWR0aCI6Ijw9MTYwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.od3W-S2mDj57GDp3_lHqV4Ed9OpnKxv1o1Uga8JyUb8')

    # Check the HTTP status code to make sure the request was successful
    if response.status_code == 200 :
    # Save the image data to a file
        with open('image.jpg', 'wb') as f :
            f.write(response.content)

    # Open the file using Pillow
    img = Image.open('image.jpg')
    img.show()

# # Minst en av bockarna dör
# # Send a GET request to the website to download the image
# def someoneDies() :
#     response = requests.get('https://wearepf.com/wp-content/uploads/2015/05/npbgood.jpg')

#     # Check the HTTP status code to make sure the request was successful
#     if response.status_code == 200 :
#     # Save the image data to a file
#         with open('image.jpg', 'wb') as f :
#             f.write(response.content)

#     # Open the file using Pillow
#     img = Image.open('image.jpg')
#     img.show()

# Alla bockarna överlever
# Send a GET request to the website to download the image
def everyoneSurvives() :
    response = requests.get('https://preview.redd.it/8fyo1xzuqqc41.jpg?auto=webp&s=1d3cb938d41ddb9f41fd3b5d7bc168cec77aad48')

    # Check the HTTP status code to make sure the request was successful
    if response.status_code == 200 :
    # Save the image data to a file
        with open('image.jpg', 'wb') as f :
            f.write(response.content)

    # Open the file using Pillow
    img = Image.open('image.jpg')
    img.show()



    