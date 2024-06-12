import ugit
import time

def read_readme_to_string():
    try:
        # Open the README.md file in read mode
        with open('README.md', 'r') as file:
            # Read the contents of the file and store it in a string
            content = file.read()
        return content
    except OSError as e:
        print("Error reading README.md:", e)
        return ""


while True:
    readme_content = read_readme_to_string()
    print(readme_content)
    ugit.ota_mqtt_check(readme_content)
    time.sleep(2)
    
    



    






