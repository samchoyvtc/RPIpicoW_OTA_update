import ugit
import time


while True:
    try:
        # Open the README.md file in read mode
        with open('README.md', 'r') as file:
            # Read the contents of the file
            content = file.read()
            # Print the contents
            print(content)
    except OSError as e:
        print("Error reading README.md:", e)
    ugit.ota_mqtt_check("23:31")
    time.sleep(2)
    
    



    






