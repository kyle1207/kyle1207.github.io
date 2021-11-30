# _*_coding: utf-8_*_
#
# @Project_Name:EXDUIAutoTest
# @File_name: __init__.py
# @author: kyle
# @date: 2021/10/9 10:47
from selenium.webdriver.common.by import By

""" vs_login_config """
vs_username = (By.CSS_SELECTOR, "[id='username']")
vs_password = (By.CSS_SELECTOR, "[id='password']")
vs_login_btn = (By.CSS_SELECTOR, ".btn-primary")
# vs_nickname = (By.XPATH, "//*[@id='app']/div[1]/div[2]/header/div/div[2]/div/div[2]/button/span[1]/span")
# vs_nickname = (By.XPATH, "//*[@id='app']/div[1]/div[2]/header/div/div[2]/div/div[2]/button/span[1]/span/text()[2]")
vs_nickname = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/header/div/div[2]/div/div[2]/button/span[1]/span")
vs_filesure = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[3]/div/button[1]/span[1]")

""" url """

# url_vs = "http://192.168.1.101:8080"
url_vs = "http://10.131.133.189/"
# url_vs = "http://192.168.1.101"
url_vs_fileupload = "http://10.131.133.189/app"

""" vs_file_upload.yaml """
vs_manage_btn = (By.XPATH, "//*[@id='sidebar']/div/a[6]/div/span")
vs_upload_btn = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[1]/div[1]/button/span[1]")
vs_choose_btn = (By.XPATH, "//*[@id='mainContent']/section/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[2]")
vs_assert_upload = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/section/div/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td[2]/div/span")
