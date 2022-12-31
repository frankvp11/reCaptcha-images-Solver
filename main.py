import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import *
from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
import speech_recognition as sr
from pydub import AudioSegment
AUDIO_FILE = "myfile.wav"

# def initialize():
#     options = Options()
#     options.add_argument('--disable-dev-shm-usage')
#     # options.add_argument("--headless")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     wait = WebDriverWait(driver, 5)
#     return driver, wait
# def input_info():
#     name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/form/div[1]/input")
#     name.send_keys("usernamer12392103821")
#     password = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/form/div[2]/input")
#     password.send_keys("Password123")
#     verify_password = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/form/div[3]/input")
#     verify_password.send_keys("Password123")
# def select_recaptcha():
#     men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[1]/form/div[7]/div/div/div/iframe")))
#     men_menu.click()

# def transcribe():
#     print("Starting transcription!")
#     r = sr.Recognizer()
#     with sr.AudioFile(AUDIO_FILE) as source:
#         print("Starting!")
#         audio = r.record(source)  # read the entire audio file                  

#         data = r.recognize_google(audio)
#         print(data)
#         return data

# def get_to_sound():
#     print("Searching for sound button")
#     sound_butt_iframe = driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/iframe")
#     print("Step one complete")
#     driver.switch_to.frame(sound_butt_iframe)
#     print("Step two complete")
#     sound_butt = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button")     
#     print("Step 4 complete")
#     sound_butt.click()
#     print("Step 5 complete")
#     download_button = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[7]/a")))
#     download_button.click()
#     print("clicked on the download button")
#     audio_src = driver.find_element(By.CSS_SELECTOR, "#audio-source")
#     print("Audio Source: ", audio_src.get_attribute("src"))
#     doc = requests.get(audio_src.get_attribute("src"))
#     with open("myfile.wav", 'wb') as f:
#         f.write(doc.content)

#     driver.switch_to.default_content()


    

# ### set up driver to go to reddit page!
# driver, wait = initialize()
# driver.get('https://old.reddit.com/login')
# time.sleep(1)
# #### Fill in the information necessary! (username, password)
# input_info()
# time.sleep(1)

# print("Finding recaptcha")
# select_recaptcha()
# print("looking to see if successful!")
# try:
#     successful = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[5]")))
#     print("Call to API with sound file!")
#     try:
#         get_to_sound()
#         print("Downloaded sound!")
#         transcription = transcribe()
#         print(transcription)
#     except:
#         print("Failed to get to sound!")

# except:
#     print("No captcha!")

# time.sleep(10000)

