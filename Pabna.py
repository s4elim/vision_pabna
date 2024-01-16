import sys
import time
import requests
import pyautogui
import tkinter as tk
from io import BytesIO
from tkinter import messagebox
from selenium import webdriver
from PIL import Image, ImageTk
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Function to check if the GitHub repository exists
def check_github_repository_exists():
    url = "https://github.com/s4elim/Nill"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        return False

if not check_github_repository_exists():
    messagebox.showerror("Error", "Check your internet connetion or Creator close the program.")
    sys.exit()


  
# Create the main window
root = tk.Tk()
root.geometry("350x400+1000+200")
root.title("Create New User / Pabna")

# URL of the icon
icon_url = "https://sunplex.net/wp-content/uploads/2024/01/VISION.logo.ico"

# Download the icon image
try:
    response = requests.get(icon_url)
    response.raise_for_status()  # Raise an HTTPError for bad responses 
    icon_image = Image.open(BytesIO(response.content))
    
    # Convert the image to a Tkinter PhotoImage
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Set the icon
    root.tk.call('wm', 'iconphoto', root._w, icon_photo)
except Exception as e:
    print(f"Error setting icon: {e}")


root.configure(bg="#f0f0f0")

# Create a list representing one person's data

def write_data():
    # Save the current window size
    initial_size = root.geometry()
    # Change the window size for the loop
    root.geometry("150x0")
    root.update_idletasks()
    data = [name_entry.get(), address_entry.get(), phone_entry.get(), '','', f"Fiber-{fiber_entry.get()}M & Onu-{onu_entry.get()}"]
    time.sleep(3)
    for value in data:
        pyautogui.write(str(value))
        pyautogui.press('tab')
        time.sleep(0.1)

    pyautogui.press('enter')  # Move to the next row
    time.sleep(0.1)

    # Clear entry fields
    name_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    fiber_entry.delete(0, 'end')
    nid_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    username_entry.delete(0, 'end')
    onu_entry.delete(0, 'end')
    root.after(10000, lambda: root.geometry(initial_size))
    


def on_entry_enter(event):
    submit_button.focus_set()

def focus_on_name_entry():
    name_entry.focus_set()

def pin_window():
    root.attributes('-topmost', True)
    root.update_idletasks()
    root.after(500, pin_window)

# Create labels and entry fields
font = ("Arial", 12)

tk.Label(root, text="Name:", font=font, bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=10, pady=5)
name_entry = tk.Entry(root, font=font)
name_entry.grid(row=0, column=1, padx=10, pady=5)


tk.Label(root, text="Username:", font=font, bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=10, pady=5)
username_entry = tk.Entry(root, font=font)
username_entry.grid(row=1, column=1, padx=10, pady=5)


tk.Label(root, text="Password:", font=font, bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=10, pady=5)
password_entry = tk.Entry(root, font=font)
password_entry.grid(row=2, column=1, padx=10, pady=5)


tk.Label(root, text="Phone Number:", font=font, bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=10, pady=5)
phone_entry = tk.Entry(root, font=font)
phone_entry.grid(row=3, column=1, padx=10, pady=5)


tk.Label(root, text="NID:", font=font, bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=10, pady=5)
nid_entry = tk.Entry(root, font=font)
nid_entry.grid(row=4, column=1, padx=10, pady=5)


tk.Label(root, text="Address:", font=font, bg="#f0f0f0").grid(row=5, column=0, sticky="e", padx=10, pady=5)
address_entry = tk.Entry(root, font=font)
address_entry.grid(row=5, column=1, padx=10, pady=5)


tk.Label(root, text="Fiber:", font=font, bg="#f0f0f0").grid(row=6, column=0, sticky="e", padx=10, pady=5)
fiber_entry = tk.Entry(root, font=font)
fiber_entry.grid(row=6, column=1, padx=10, pady=5)


tk.Label(root, text="Onu Id:", font=font, bg="#f0f0f0").grid(row=7, column=0, sticky="e", padx=10, pady=5)
onu_entry = tk.Entry(root, font=font)
onu_entry.grid(row=7, column=1, padx=10, pady=5)




# Function to start Selenium actions
def start_selenium():

    name = name_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()
    nid = nid_entry.get()
    fiber = fiber_entry.get()
    onu = onu_entry.get()
    address = address_entry.get()
    remark = f"Fiber-{fiber}M & Onu-{onu}"
    # Replace with your actual username, password, and login URL
    selenium_username = 
    selenium_password = 
    login_url = 

    # Set up WebDriver for Chrome
    driver = webdriver.Chrome()

    def check_browser():
        if driver.window_handles:
            root.after(100, check_browser)  # Check again after 100 milliseconds
        else:
            # Browser is closed, close the Tkinter window
            root.destroy()

    # Navigate to the login page
    driver.get(login_url)





    # Wait for the username field to be present and clickable
    username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[3]/form/fieldset/div[1]/input"))
        )
    username_field.send_keys(selenium_username)

        
    password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="passw"]'''))
        )
    password_field.send_keys(selenium_password)

        
    login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div[3]/form/fieldset/button"))
        )
    login_button.click()

        # Optional: Wait for some time to allow the login to complete
    time.sleep(1)


    home = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="exampleAccordion"]/li[3]/a/span'''))
        )
    home.click()

        
    add_account = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="collapseInternetService"]/li[1]/a'''))
        )
    add_account.click()


    name_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="fname"]'))
            )
    name_element.send_keys(name)

    username_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="uname"]'))
        )
    username_element.send_keys(username)

    password_element1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pass1"]'))
        )
    password_element1.send_keys(password)

    password_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pass2"]'))
        )
    password_element.send_keys(password)

    mobile_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mobile1"]'))
        )
    mobile_element.send_keys(phone)

    usertype = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="group_id"]/option[2]'''))
        )
    usertype.click()


    gender = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="page-top"]/div/div/div/div/center/div/form/div/div/div[2]/div[8]/div/span[1]/input'''))
        )
    gender.click()
    
    nid_redio = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="page-top"]/div/div/div/div/center/div/form/div/div/div[2]/div[9]/div[3]/label[1]/input'''))
        )
    nid_redio.click()
    

    nid_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nid"]'))
        )
    nid_element.send_keys(nid)


    address_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="house_no"]'))
        )
    address_element.send_keys(address)
    

    select_pabna = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="district"]/option[50]'''))
        )
    select_pabna.click()
    

    select_thana = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '''//*[@id="cthana"]/option[9]'''))
        )
    select_thana.click()


    remarks = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="int_ref"]'))
        )
    remarks.send_keys(remark)
            


    # Start checking if the browser is closed
    check_browser()



# Create a button to start Selenium actions

submit_button = tk.Button(root, text="Submit", command=start_selenium, font=font, bg="#4CAF50", fg="white")
submit_button.grid(row=9, columnspan=2, pady=10)



past_button = tk.Button(root, text="Past", command=write_data , font=font, bg="#4CAF50", fg="white")
past_button.grid(row=9, column = 1, columnspan=2, pady=10)


#Pin window
pin_window()


# Automatically focus on the "Name" field
root.after(100,focus_on_name_entry)

root.mainloop()

