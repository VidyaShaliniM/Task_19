from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import requests


class Sauce_demo:
    username = "standard_user"
    password = "secret_sauce"

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            print("The title of webpage is: ",self.driver.title)
            print("The url of webpage is: ", self.driver.current_url)
            sleep(4)
            self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
            sleep(4)
            self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
            sleep(4)
            self.driver.find_element(by=By.ID, value="login-button").click()
            sleep(4)
        except NoSuchElementException as selenium_error:
            print("Element not found", selenium_error)
        finally:
            self.driver.quit()


    def contents_of_page(self):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                page_content = response.text
                file_name = "Webpage_task_11.txt"
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(page_content)
                print(f"Webpage content saved to {file_name}")
            else:
                print(f"Failed to get the contents of the webpage. Statuscode: {response.status_code}")
        except NoSuchElementException as selenium_error:
            print("Element not found", selenium_error)
        finally:
            self.driver.quit()


url = "https://www.saucedemo.com/"

demo = Sauce_demo(url)

demo.login()
demo.contents_of_page()



