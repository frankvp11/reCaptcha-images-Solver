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




class Solver():
    def __init__(self, url):
        self.url = url
        self.audio_file = "myfile.wav"
        self.options = Options()
        self.options.add_argument("--disable-dev-shm-usage")
        #self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = self.options)
        self.wait = WebDriverWait(self.driver, 1)
        self.recognizer = sr.Recognizer()
    def transcribe(self):
        with sr.AudioFile(self.audio_file) as source:
            audio = self.recognizer.record(source)  # read the entire audio file                  
            data = self.recognizer.recognize_google(audio)
            return data
    def click_recaptcha(self):
        print("Clicking recaptcha!")
        men_menu = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".g-recaptcha")))
        men_menu.click()
        print("Clicked!")

    def get_to_sound(self):
        sound_butt_iframe = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/iframe")
        self.driver.switch_to.frame(sound_butt_iframe)
        sound_butt = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button")     
        sound_butt.click()
        download_button = self.wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[7]/a")))
        download_button.click()
        audio_src = self.driver.find_element(By.CSS_SELECTOR, "#audio-source")
        print("Audio Source: ", audio_src.get_attribute("src"))
        doc = requests.get(audio_src.get_attribute("src"))
        with open("myfile.wav", 'wb') as f:
            f.write(doc.content)

        self.driver.switch_to.default_content()
    def complete(self):
        print(self.url)
        self.driver.get(self.url)
        self.click_recaptcha()
        try:
            successful = self.wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[5]")))
            try:
                self.get_to_sound()
                transcription = self.transcribe()
            except:
                print("Failed!")
                self.complete()
        except:
            print("No Captcha -> complete!")
        
        
        return self.driver.find_element(By.CSS_SELECTOR, "#g-recaptcha-response").get_property("value")


