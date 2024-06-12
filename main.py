import ugit
import time

def readme():
    try:
        # Open the README.md file in read mode
        with open('README.md', 'r') as file:
            # Read the contents of the file
            content = file.read()
            # Print the contents
            print(content)
            return content
    except OSError as e:
        print("Error reading README.md:", e)


while True:
    ugit.ota_mqtt_check(readme())
    time.sleep(1)
    
    