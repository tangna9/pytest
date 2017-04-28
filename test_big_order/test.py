# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
import paramiko

paramiko.

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = '11d42ea0'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_name("8").click()
driver.find_element_by_id('digit7').click()
driver.find_element_by_id('plus').click()
driver.find_element_by_id('digit3').click()
driver.find_element_by_id('equal').click()
sleep(3)
driver.find_element_by_id('clear').click()
driver.quit()