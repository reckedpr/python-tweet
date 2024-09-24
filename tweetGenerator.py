from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os
import random

def generateTweet(handle,name,tweet_text,avatar,popularity):

    def generate_post_stats(popularity):
        # Ensure popularity is between 1 and 100
        popularity = max(1, min(100, popularity))
        
        # Calculate views such that a popularity of 50 gives 2.5M views
        views = int(2000000 * (popularity / 50))
        
        # Generate likes as a percentage of views
        like_percentage = 0.05 + (popularity / 1000)  # Increase slightly with popularity
        likes = int(views * like_percentage)
        
        # Generate reposts as a fraction of likes
        repost_percentage = 0.1 + (popularity / 500)  # Increase with popularity
        reposts = int(likes * repost_percentage)
        
        # Generate comments as a fraction of likes
        # Comments are less common than reposts, around 5% to 15% of likes
        comment_percentage = 0.05 + (popularity / 1000)  # Increase slightly with popularity
        comments = int(likes * comment_percentage)
        
        # Generate saves as a fraction of likes
        # Saves are rarer than comments, typically around 5% to 10% of likes
        save_percentage = 0.05 + (popularity / 2000)  # Increase slightly with popularity
        saves = int(likes * save_percentage)
        
        # Return the calculated statistics as a dictionary
        return {
            "views": views,
            "likes": likes,
            "reposts": reposts,
            "comments": comments,
            "saves": saves
        }
    


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
                print(f"deleted old file: {file_path}")

            except Exception as e:
                print(f"error delting the file: {e}")
        else:
            print(f"no file at: {file_path}")


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
        for i in range(5):
            input_field.clear()
        input_field.send_keys(text)

    injectInput('handle',handle)
    injectInput('name',name)
    injectInput('tweet-text',tweet_text)

    date_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'dateTime'))
    )

    now = datetime.now()
    date_value = now.strftime('%Y-%m-%dT%H:%M')

    # Use JavaScript to update the value and dispatch the change event
    script = """
    var input = arguments[0];
    var value = arguments[1];
    var lastValue = input.value;

    input.value = value;

    // React tracks changes via the "value" property and doesn't always react to direct DOM changes.
    // Dispatch an input event to simulate user interaction and trigger React's state updates.

    var event = new Event('input', { bubbles: true });
    var tracker = input._valueTracker;
    if (tracker) {
        tracker.setValue(lastValue);
    }
    input.dispatchEvent(event);
    """

    # Execute the script in Selenium
    driver.execute_script(script, date_field, date_value)

    # Locate the date input using its XPath
    #date_input = driver.find_element(By.NAME, 'dateTime')

    # Use JavaScript to set the value of the date input (e.g., "2023-09-24 12:00")
    #driver.execute_script('arguments[0].value = "2020-12-12T12:24";', date_input)

    # Optionally trigger a 'change' event to ensure the page recognizes the updated value
    #driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)

#   2024-09-10T12:24

    avatar_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#\:R1cjaqqlla\:"))
    )

    avatar_field.clear()
    time.sleep(0.2)
    for i in range(5):
        avatar_field.clear()
    avatar_field.send_keys(avatar)

    advanced_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[1]/div/button')) 
    )

    advanced_button.click()

    stats = generate_post_stats(popularity)

    injectInput('views', stats['views'])
    injectInput('likes', stats['likes'])
    injectInput('quotes', stats['comments'])
    injectInput('saves', stats['saves'])
    injectInput('retweets', stats['reposts'])

    
    expected_filename = "tweet-preview.png"
    temp_extension = ".tmp"
    final_file = os.path.join(download_dir, expected_filename)

    delete_old_tweet_preview(os.path.join(download_dir, expected_filename))


    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/div/div/button')) 
    )

    time.sleep(1)

    download_button.click()

    wait_for_download_to_complete(download_dir, expected_filename, temp_extension)


    driver.quit()

if __name__ == '__main__':
    generateTweet('elonmusk',
                'TTV Xx_Elon_xX',
                'reckedpr is an absolute legend, holy shit',
                'https://d1kd6h2y8iq4lp.cloudfront.net/avatars/elonmusk',
                12)