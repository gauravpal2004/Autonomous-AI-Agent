import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to interact with OpenAI's GPT model (using the old method)
def generate_text(prompt):
  response = openai.Completion.create(
      engine="text-davinci-003",  # Adjust engine if needed (consider "text-babbage-001" for a similar model)
      prompt=prompt,
      max_tokens=150
  )
  return response.choices[0].text.strip()

# Initialize the WebDriaver
driver = webdriver.Chrome()

# Load the webpage with the form
driver.get('https://form.jotform.com/241617189501153')

# Wait for the page to load completely
time.sleep(3)

# Fill out the Full Name section
driver.find_element(By.XPATH, "//input[@id='first_11']").send_keys("Gaurav")
driver.find_element(By.XPATH, "//input[@id='middle_11']").send_keys("Pal")
driver.find_element(By.XPATH, "//input[@id='last_11']").send_keys("Pal")

time.sleep(5)

# Fill out the Current Address section
driver.find_element(By.XPATH, "//input[@id='input_16_addr_line1']").send_keys("A-100")
driver.find_element(By.XPATH, "//input[@id='input_16_addr_line2']").send_keys("ramphal chock")
driver.find_element(By.XPATH, "//input[@id='input_16_city']").send_keys("Dwarka")
driver.find_element(By.XPATH, "//input[@id='input_16_state']").send_keys("Delhi")
driver.find_element(By.XPATH, "//input[@id='input_16_postal']").send_keys("100011")

time.sleep(5)

# Fill out the other form fields
driver.find_element(By.XPATH, "//input[@id='input_12']").send_keys("palgaurav19067@gmail.com")
driver.find_element(By.XPATH, "//input[@id='input_13_full']").send_keys("7042512015")
driver.find_element(By.XPATH, "//input[@id='input_19']").send_keys("www.linkedin.com/in/gaurav-pal-b3a4b2222")

time.sleep(5)
# Generate and fill content for "Write something interesting about AI Agents/LLMs"
ai_agents_text = generate_text("Write something interesting about AI Agents/LLMs.")
ai_agents_field = driver.find_element(By.XPATH, "//textarea[@id='input_24']")
ai_agents_field.send_keys(ai_agents_text)


# Generate and fill content for "Write something interesting about Web Automation"
web_automation_text = generate_text("Write something interesting about Web Automation.")
web_automation_field = driver.find_element(By.XPATH, "//textarea[@id='input_25']")
web_automation_field.send_keys(web_automation_text)


# Generate and fill description for "Reverse a LinkedList"
reverse_linked_list_text = generate_text("Describe how to reverse a LinkedList in Python.")
reverse_linked_list_field = driver.find_element(By.XPATH, "//textarea[@id='input_23']")
reverse_linked_list_field.send_keys(reverse_linked_list_text)

time.sleep(5)

# Upload Resume - simulate the file upload
resume_upload_field = driver.find_element(By.XPATH, "//input[@type='file'][@id='input_17']")
resume_upload_field.send_keys(r"C:\Users\Hp\OneDrive\Desktop\Gaurav Pal Resume.pdf")


# Optionally, you can generate and fill a cover letter if there's a placeholder for it
cover_letter_text = generate_text("Write a cover letter for a LLM based job application.")
cover_letter_field = driver.find_element(By.XPATH, "//textarea[@id='input_22']")
cover_letter_field.send_keys(cover_letter_text)

time.sleep(5)



# Submit the form by clicking the apply button
apply_button = driver.find_element(By.XPATH, "//button[text()='Apply']")
apply_button.click()

# Optionally, wait to observe the results
time.sleep(115)

# Close the driver
# driver.quit()
