from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def generateTweet(handle,name,tweet_text,avatar):


    def wait_for_download_to_complete(download_dir, expected_filename, temp_extension):
        final_file_path = os.path.join(download_dir, expected_filename)
        temp_file_path = os.path.join(download_dir, expected_filename + temp_extension)


        while not os.path.exists(temp_file_path) and not os.path.exists(final_file_path):
            time.sleep(0.2) 

        while os.path.exists(temp_file_path):
            time.sleep(0.2)

        while not os.path.exists(final_file_path):
            time.sleep(0.2)


    def delete_old_tweet_preview(file_path):
        # check if old file exists
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                return f"deleted old file: {file_path}"
            except Exception as e:
                return f"error delting the file: {e}"
        else:
            return f"no file at: {file_path}"


    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage") 


    current_dir = os.path.dirname(os.path.abspath(__file__))  
    download_dir = os.path.join(current_dir, "images/")
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)

    
    chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)


    driver.get("https://typefully.com/tools/fake-tweet-generator")

    

    def injectInput(elementName,text):
        input_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, elementName))
        )

        input_field.clear()
        time.sleep(0.2)
        input_field.clear()
        input_field.clear()
        input_field.clear()
        input_field.clear()
        input_field.clear()
        input_field.clear()
        input_field.send_keys(text)

    injectInput('handle',handle)
    injectInput('name',name)
    injectInput('tweet-text',tweet_text)

    avatar_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#\:R1cjaqqlla\:"))
    )

    avatar_field.clear()
    time.sleep(0.2)
    avatar_field.clear()
    avatar_field.clear()
    avatar_field.clear()
    avatar_field.clear()
    avatar_field.clear()
    avatar_field.clear()
    avatar_field.send_keys(avatar)


    
    expected_filename = "tweet-preview.png"
    temp_extension = ".tmp"
    final_file = os.path.join(download_dir, expected_filename)

    delete_old_tweet_preview(download_dir+expected_filename)



    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/div/button')) 
    )

    time.sleep(1)

    download_button.click()

    wait_for_download_to_complete(download_dir, expected_filename, temp_extension)


    driver.quit()

if __name__ == '__main__':
    generateTweet('notelonmusk',
                'Elon Fucking Musk',
                'Tesla is shit, im gonna sell it',
                'https://d1kd6h2y8iq4lp.cloudfront.net/avatars/elonmusk'
                )