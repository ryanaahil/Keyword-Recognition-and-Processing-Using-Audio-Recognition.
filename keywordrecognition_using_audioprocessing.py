import speech_recognition as sr
import keyboard
import datetime
import gmaps

gmaps_key = "AIzaSyDdIE8FAOa3g9vx1xRkrfkayQgBOCIjAw8"
gmaps.configure(api_key=gmaps_key)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Press '1' to start recording...")
        keyboard.wait("1")
        print("Recording...")

        audio = recognizer.listen(source)

        print("Press '0' to stop recording...")
        keyboard.wait("0")
        print("Stopped recording.")

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said:", text)

        
            if "emergency" in text.lower():
                print("WARNING: Detected keyword 'emergency'")
                
            if "help" in text.lower():
                print("WARNING: Detected keyword 'help'")
            
            
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print("Timestamp:", timestamp)
            
            
            location = get_location()
            print("Location:", location)
            
    
            
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error with the request: {0}".format(e))
            
import requests

def get_location():
    
    address = "ChIJbU60yXAWrjsR4E9-UejD3_g"

    api_key = "AIzaSyDdIE8FAOa3g9vx1xRkrfkayQgBOCIjAw8"

    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?place_id=ChIJbU60yXAWrjsR4E9-UejD3_g&key={api_key}"

    try:
    
        response = requests.get(geocoding_url)
        data = response.json()

        if data['status'] == 'OK':

            result = data['results'][0]
            formatted_address = result['formatted_address']
            latitude = result['geometry']['location']['lat']
            longitude = result['geometry']['location']['lng']

            return f"Formatted Address: {formatted_address}, Latitude: {latitude}, Longitude: {longitude}"

    except Exception as e:
        print(f"Error getting location: {str(e)}")

    return "Bengaluru, Karnataka, India"


if __name__ == "__main__":
    recognize_speech()
