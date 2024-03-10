# Importing required libraries
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigating to the eBay homepage
    driver.get("https://www.ebay.ca/")

    # Scroll and click on the sneakers link
    sneakers_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/ul/li[6]"))
    )
    time.sleep(1)
    sneakers_link.click()
    time.sleep(2)

    # Scroll and click on the Nike button
    nike_btn_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/nav/div[1]/div/div/div/section[1]/ul/li[3]/a"))
    )
    time.sleep(1)
    nike_btn_link.click()
    time.sleep(2)

    # Scroll and click on the Air Force image link
    airForce_img_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[3]/div[3]/section[1]/div[2]/div/div/ul/li[2]/a/div/img"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", airForce_img_link)
    time.sleep(1)
    airForce_img_link.click()
    time.sleep(2)

    # Scroll and click on the view gallery button
    view_gallery = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[3]/div[3]/section[1]/div[1]/div[1]/div[2]/div[2]/span/button"))
    )
    time.sleep(1)
    view_gallery.click()
    time.sleep(2)

    # Scroll and click on the view grid button
    view_grid = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[3]/div[3]/section[1]/div[1]/div[1]/div[2]/div[2]/span/span"))
    )
    time.sleep(1)
    view_grid.click()
    time.sleep(2)

    # store current window handle
    main_Window_Handle = driver.current_window_handle

    # Scroll and click on the review button
    item_Text_Btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "#s0-28-9-0-1\\[0\\]-0-0 > ul > li:nth-child(1) > div.s-item__wrapper.clearfix > div.s-item__info.clearfix > a"))
    )
    time.sleep(1)
    item_Text_Btn.click()
    time.sleep(3)

    # Switch to the pop-up window
    for handle in driver.window_handles:
        if handle != main_Window_Handle:
            driver.switch_to.window(handle)
            break

    driver.close()
    # Switch back to the main window
    driver.switch_to.window(main_Window_Handle)

    view_Auction = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[3]/div[3]/section[1]/div[1]/div[1]/div[1]/div/ul/li[2]/a"))
    )
    time.sleep(2)
    view_Auction.click()
    time.sleep(3)

    heart_favourites = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[3]/div[3]/div[3]/section[1]/ul/li[1]/span/a"))
    )
    time.sleep(2)
    heart_favourites.click()
    time.sleep(3)

finally:
    # Ensure the driver is closed properly
    driver.close()
