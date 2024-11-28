import time
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Initialize WebDriverWait
def initialize_wait_drive_feed(driver):
    return WebDriverWait(driver, 300)

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

# Headless set up
options = Options()
options.add_argument('--headless')

# Set up the driver
driver = webdriver.Chrome(options=options)
wait_driver = initialize_wait_drive_feed(driver)  # Pass the driver to the wait function

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScGuzmmOU0BjpZv9AVblmmOVnBCQz5WqMracmAhdOQkZVHqlg/viewform")
driver.maximize_window()

import random

def generate_grades():
    # Generate three random float numbers between 1.0 and 2.8
    randGrades = [round(random.uniform(1.0, 2.8), 1) for _ in range(3)]
    # Join them into a space-separated string
    return " ".join(map(str, randGrades))

# Use explicit waits for each interaction
try:
    try:
        time.sleep(0.5)
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[1]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)
    # Year
    year_xpaths = [
        "//div[@id='i9']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i12']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i15']//div[@class='AB7Lab Id5V1']"
    ]

    try:
        # Randomly select an XPath
        selected_xpath = random.choice(year_xpaths)
        print(f"Selected XPath: {selected_xpath}")  # Debugging to see which XPath was chosen

        # Locate the element
        locator = (By.XPATH, selected_xpath)
        year = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, year)
        year.click()
    except TimeoutException as e:
        print("Host Create form did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    department_xpaths = [
        "//div[@id='i26']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i29']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i35']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i38']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i41']//div[@class='AB7Lab Id5V1']"
    ]
    # Department selection
    try:
        # Randomly select an XPath
        selected_xpath = random.choice(department_xpaths)
        print(f"Selected XPath: {selected_xpath}")  # Debugging to see which XPath was chosen

        # Locate the element
        locator = (By.XPATH, selected_xpath)
        department = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, department)
        department.click()
    except TimeoutException as e:
        print("Host Create form did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    gender_xpaths = [
        "//div[@id='i58']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i61']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i64']//div[@class='AB7Lab Id5V1']"
    ]
    # Gender
    try:
        # Randomly select an XPath
        selected_xpath = random.choice(gender_xpaths)
        print(f"Selected XPath: {selected_xpath}")  # Debugging to show the chosen XPath

        # Locate the element
        locator = (By.XPATH, selected_xpath)
        gender = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, gender)
        gender.click()
    except TimeoutException as e:
        print("Host Create form did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    # next button
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    # mother employment
    try:
        # yes
        locator = (By.XPATH, "(//div[@class='AB7Lab Id5V1'])[1]")
        mWork = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, mWork)
        mWork.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    # father employment
    try:
        # yes
        locator = (By.XPATH, "(//div[@class='AB7Lab Id5V1'])[3]")
        fWork = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, fWork)
        fWork.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    status_xpaths = [
        "//div[@id='i31']//div[@class='AB7Lab Id5V1']",
        "//div[@id='i37']//div[@class='AB7Lab Id5V1']"
    ]
    # Marital Status selection
    try:
        # Randomly select an XPath
        selected_xpath = random.choice(status_xpaths)
        print(f"Selected XPath: {selected_xpath}")  # Debugging to show the chosen XPath

        # Locate the element
        locator = (By.XPATH, selected_xpath)
        status = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, status)
        status.click()
    except TimeoutException as e:
        print("Host Create form did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    # next
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)

    # Clicks the dropdown
    try:
        locator = (By.XPATH, "(//div[@role='option'])[1]")
        economicStatus = wait_driver.until(EC.visibility_of_element_located(locator))
        economicStatus.click()

        # Lower Class
        locator = (By.XPATH, "(//div[@role='option'])[2]")
        classStatus = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, classStatus)
        classStatus.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)

    # Family Support
    try:
        # Clicks the family radio button
        locator = (By.XPATH, "(//span[normalize-space()='Family'])[1]")
        support = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, support)
        support.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    # Next button
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    # Motivation
    time.sleep(5)
    try:
        # This selects all except others
        # locator = (By.XPATH, "(//span[normalize-space()='Future goals'])[1]")
        # goals = wait_driver.until(EC.visibility_of_element_located(locator))
        # goals.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='Family'])[1]")
        fam = wait_driver.until(EC.visibility_of_element_located(locator))
        fam.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='Improve financial circumstances'])[1]")
        financial = wait_driver.until(EC.visibility_of_element_located(locator))
        financial.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='Romantic Relationships'])[1]")
        rel = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, rel)
        rel.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='Personal Development'])[1]")
        personal = wait_driver.until(EC.visibility_of_element_located(locator))
        personal.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)
    # Preferred learning style
    try:
        # Selects all except others
        locator = (By.XPATH, "(//div[@class='uHMk6b fsHoPb'])[7]")
        visual = wait_driver.until(EC.visibility_of_element_located(locator))
        visual.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//div[@class='uHMk6b fsHoPb'])[8]")
        auditory = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, auditory)
        auditory.click()

        time.sleep(0.5)

        # locator = (By.XPATH, "(//div[@class='uHMk6b fsHoPb'])[9]")
        # kinesthetic = wait_driver.until(EC.visibility_of_element_located(locator))
        # kinesthetic.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)
    try:
        # grades
        locator = (By.XPATH, "(//input[@class='whsOnd zHQkBf'])[1]")
        grades = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, grades)
        grades_string = generate_grades()
        grades.send_keys(grades_string)
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)
    try:
        # pass
        locator = (By.XPATH, "(//div[@role='option'])[1]")
        status = wait_driver.until(EC.visibility_of_element_located(locator))
        status.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//div[@role='option'])[2]")
        passed = wait_driver.until(EC.visibility_of_element_located(locator))
        passed.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)
    try:
        # pass
        locator = (By.XPATH, "(//div[@role='option'])[4]")
        status = wait_driver.until(EC.visibility_of_element_located(locator))
        status.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//div[@role='option'])[5]")
        passed = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, passed)
        passed.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    try:
        # pass
        locator = (By.XPATH, "(//div[@role='option'])[7]")
        status = wait_driver.until(EC.visibility_of_element_located(locator))
        status.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//div[@role='option'])[8]")
        passed = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, passed)
        passed.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)
    # academic success
    try:
        # yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[1]")
        yes = wait_driver.until(EC.visibility_of_element_located(locator))
        yes.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)
    # understanding lesson
    try:
        # no
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='No'])[2]")
        no = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, no)
        no.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)
    # Time Studying
    try:
        # yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[3]")
        yes = wait_driver.until(EC.visibility_of_element_located(locator))
        yes.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(5)
    # next button
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # Internet
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[1]")
        internet = wait_driver.until(EC.visibility_of_element_located(locator))
        internet.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # understanding topic
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[2]")
        topic = wait_driver.until(EC.visibility_of_element_located(locator))
        topic.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(0.5)
    # aid or tools
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[3]")
        aid = wait_driver.until(EC.visibility_of_element_located(locator))
        aid.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # recommendations can help me perform better
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[4]")
        reco = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, reco)
        reco.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # suggestions to improve my performance based on predictions
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[5]")
        improve = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, improve)
        improve.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # reduce my academic stress
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[6]")
        system = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, system)
        system.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # Using AI to assist me academically
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[7]")
        assist = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, assist)
        assist.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # Academic guidance
    try:
        # Yes
        locator = (By.XPATH, "(//span[@class='aDTYNe snByac OvPDhc OIC90c'][normalize-space()='Yes'])[8]")
        guidance = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, guidance)
        guidance.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # tools resources used
    try:
        locator = (By.XPATH, "(//span[normalize-space()='YouTube'])[1]")
        yt = wait_driver.until(EC.visibility_of_element_located(locator))
        yt.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='ChatGPT or other AI assistants'])[1]")
        gpt = wait_driver.until(EC.visibility_of_element_located(locator))
        gpt.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[normalize-space()='Learning Management Systems (LMS)'])[1]")
        lms = wait_driver.until(EC.visibility_of_element_located(locator))
        lms.click()

        time.sleep(0.5)

        locator = (By.XPATH, "(//span[contains(text(),'Note-taking Applications (e.g: Evernote, OneNote, ')])[1]")
        note = wait_driver.until(EC.visibility_of_element_located(locator))
        note.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    time.sleep(4)
    # Next
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        next = wait_driver.until(EC.visibility_of_element_located(locator))
        scroll_to_element(driver, next)
        next.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

    # time.sleep(4)
    # Submit
    try:
        locator = (By.XPATH, "(//span[@class='l4V7wb Fxmcue'])[2]")
        submit = wait_driver.until(EC.visibility_of_element_located(locator))
        submit.click()
    except TimeoutException as e:
        print("Host Create from did not show on time", e)
    except ElementClickInterceptedException as e:
        print("Can't click on Host elements", e)

except TimeoutException as e:
    print("Host Create from did not show on time", e)
except ElementClickInterceptedException as e:
    print("Can't click on Host elements", e)

time.sleep(0.5)
driver.quit()

