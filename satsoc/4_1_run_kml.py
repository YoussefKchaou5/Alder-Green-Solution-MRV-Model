import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to your KML files
kml_folder = r'C:\Users\Youss\satsoc\kml'  # Replace with your KML files directory
kml_files = [os.path.join(kml_folder, f) for f in os.listdir(kml_folder) if f.endswith('.kml')]

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and in your PATH

try:
    # Open the Copernicus Data Space Browser
    driver.get('https://browser.dataspace.copernicus.eu/?zoom=4&lat=38.47939&lng=-99.09668&demSource3D="MAPZEN"&cloudCoverage=30&dateMode=SINGLE')

    # Allow time for the page to load
    time.sleep(5)

    # Iterate through each KML file
    for kml_file in kml_files:
        # Locate the KML upload element (you may need to inspect the webpage to find the correct element)
        upload_element = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')  # Adjust this selector as needed

        # Send KML file path to the upload input
        upload_element.send_keys(kml_file)
        
        # Allow time for the file to be processed (you may need to adjust this)
        time.sleep(10)  # Wait for the file to upload and polygons to be drawn

        # If there are any buttons to confirm or additional steps after upload, automate those as well
        # For example, clicking a button to confirm upload:
        # confirm_button = driver.find_element(By.ID, 'confirm-upload-button')  # Adjust selector
        # confirm_button.click()
        
        # Wait for the polygons to render
        time.sleep(5)

finally:
    # Close the browser when done
    driver.quit()
