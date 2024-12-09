
import time
from datetime import timedelta, datetime

import pytest
# from telnetlib import EC
# from openpyxl.chart import title
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from Basepage import Basepage

class Login(Basepage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.CSS_SELECTOR, '.oxd-button')
    click = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    direct = (By.LINK_TEXT, "My Info")
    #########################personal###########################
    personal = (By.CSS_SELECTOR,"input[placeholder='First Name']")
    time.sleep(2)
    ID = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    Nation = (By.XPATH,"//div[contains(text(),'Indian')]")
    radio = (By.XPATH,"//label[normalize-space()='Female']")
    time.sleep(4)
    save = (By.XPATH,"(// button[@ type='submit'][normalize-space() = 'Save'])")
    Logout = (By.LINK_TEXT, "Logout")
    ###########################contact#####################
    contact = (By.XPATH,"//a[normalize-space()='Contact Details']")

    city = (By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[3]//div[1]//div[2]//input[1]")
    time.sleep(6)
    mail = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[11]")
    save1 = (By.XPATH,"(//button[normalize-space()='Save'])[1]")
    time.sleep(6)
    add = (By.XPATH,"//button[normalize-space()='Add']")
    comment = (By.CSS_SELECTOR,"textarea[placeholder='Type comment here']")
    time.sleep(6)
    save2 = (By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[2]")
#################################################################
    Emeadd = (By.XPATH,"(//a[normalize-space()='Emergency Contacts'])[1]")
    add1 = (By.CSS_SELECTOR,"div[class='orangehrm-attachment'] button[type='button']")
    time.sleep(6)
    browse = (By.XPATH,"(//div[@class='oxd-file-button'])[1]")
    save3 = (By.XPATH,"(//button[normalize-space()='Save'])[1]")
    time.sleep(5)
# ########################################################
#     depend = (By.XPATH,"//a[normalize-space()='Dependents']")
#     add2 = (By.XPATH,"(//button[@type='button'][normalize-space()='Add'])[1]")
#     time.sleep(4)
#     name = (By.XPATH,"(//*[@class='oxd-input oxd-input--active'])[2]")
#     relation = (By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
#     time.sleep(4)
#     date = (By.CSS_SELECTOR,"input[placeholder='yyyy-dd-mm']")
#     save4 = (By.CSS_SELECTOR,"button[type='submit']")
#     time.sleep(5)
#     ##############################################################
#     # immigration =(By.CLASS_NAME,"orangehrm-tabs-item --active")
#     # delete = (By.XPATH,"(//button[@type='button'])[5]")
#     #time.sleep(6)
#     # edit = (By.XPATH,"//div[@class='orangehrm-attachment']//i[@class='oxd-icon bi-pencil-fill']")
#     # browse1 =(By.XPATH,"(//div[@class='oxd-file-button'])[1]")
#     #time.sleep(4)
#     # comment1 = (By.CSS_SELECTOR,"textarea[placeholder='Type comment here']")
#     # save5 = (By.CSS_SELECTOR,"button[type='submit']")
#     #time.sleep(4)
#     #############################################
#     # # qualification
#     # add3 = (By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[1]")
#     # company = (By.XPATH, "(//*[@class='oxd-input oxd-input--focus'])")
#     # job_title = (By.XPATH, "(//*[@class='oxd-input oxd-input--active oxd-input--error'])[2]")
#     # save6 = (By.XPATH, "//*[@type='submit']")
#     # ####################################################3
#     # # education
#     # # add4 = (By.XPATH, "(//*[@class = 'oxd-icon bi-plus oxd-button-icon'])[2]")
#     # level = (By.XPATH, "//*[@class = 'oxd-select-text-input']")
#     #time.sleep(5)
#     # institute = (By.XPATH, "(//*[@class = 'oxd-input oxd-input--active'])[2]")
#     # specialization = (By.XPATH, "(//input)[5]")
#     #time.sleep(5)
#     # year = (By.XPATH, "(//input)[6]")
#     #
#     # gpa = (By.XPATH, "(//input)[7]")
#     #time.sleep(4)
#     # save7 = (By.XPATH, "//button[@type='submit']")
#     # ############################
#     # # skills
#     # skill = (By.XPATH, "//div[@class='oxd-select-text-input']")
#     # yexp = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
#     # time.sleep(5)
#     # save8 = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
#     # ###############################
#     # # language
#     # la = (By.XPATH, "//*[@class = 'oxd-select-text-input']")
#     # competency = (By.XPATH, "(//*[@class = 'oxd-select-text-input'])[3]")
#     # time.sleep(4)
#     # ################################
#     # # membership
#     # memb = (By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
#     # currency = (By.XPATH, "(//*[@class = 'oxd-select-text-input'])[3]")
#     # time.sleep(4)
#
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, namevalue, pwdvalue):
        self.hrm_send_keys(self.username, namevalue)
        self.hrm_send_keys(self.password, pwdvalue)
        self.hrm_btn_click(self.submit)

        time.sleep(3)

    def login1(self):


        self.hrm_btn_click(self.direct)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.my_info))

        # self.driver.find_element(direct).click()
        # time.sleep(5)
        # print("clicked my info")
        # self.hrm_btn_click(self.personal)
        time.sleep(8)

    def login2(self, heyy):


        self.hrm_btn_click(self.personal)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        time.sleep(3)
        # a.clear()
        self.hrm_send_keys(self.personal,heyy)
        # WebDriverWait(self.driver,30).until(EC.title_is(title))


    def login3(self, a):
        self.hrm_btn_click(self.ID)
        time.sleep(4)

        # actions = ActionChains(self.driver)
        # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        # time.sleep(3)
        # a=87
        self.hrm_send_keys(self.ID,a)

    def login4(self):
        american = (By.XPATH, "//div[contains(text(),'American')]")
        indian = (By.XPATH, "(//span[normalize-space()='Indian'])[1]")
        time.sleep(5)
        # self.driver.find_element(*my_info).click()
        time.sleep(4)
        self.driver.find_element(*american).click()
        time.sleep(4)
        self.driver.find_element(*indian).click()
        time.sleep(4)
    #
    #     self.hrm_btn_click(self.Nation)
    #     # actions = ActionChains(self.driver)
    #     # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
    #     # time.sleep(3)
    #     # self.hrm_send_keys(self.Nation,Indian)
    #     time.sleep(3)
    #     # a=(By.XPATH,"//div[contains(text(),'Indian')]")
    #     # a.click()
    #     # time.sleep(2)
    #
    def login5(self):
        self.hrm_btn_click(self.radio)
        # a.clear()
        time.sleep(4)

    def login6(self):
        self.hrm_btn_click(self.save)
        # a.clear()
        time.sleep(4)
################################################################
    def login7(self):
        self.hrm_btn_click(self.contact)
        time.sleep(3)

    # @pytest.mark.skip(reason="Known bug: Issue #12345")
    def login8(self, cbe):
        self.hrm_btn_click(self.city)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        #     # time.sleep(3)
        time.sleep(3)
        self.hrm_send_keys(self.city,cbe)
        # assert False, "This test will be skipped due to a known bug."

    def login9(self, a):
        self.hrm_btn_click(self.mail)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        time.sleep(7)
        a = "madu@gmail.com"
        self.hrm_send_keys(self.mail,a)
        time.sleep(5)

    def login10(self):
        self.hrm_btn_click(self.save1)
        time.sleep(4)

    def login11(self):
        self.hrm_btn_click(self.add)
        time.sleep(3)

    def login12(self, a):
        self.hrm_btn_click(self.comment)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        time.sleep(7)
        a = "u look beautiful"
        self.hrm_send_keys(self.comment,a)
        time.sleep(5)

    def login13(self):
        self.hrm_btn_click(self.save2)
        time.sleep(4)
########################################################################3

#
#     def login14(self):
#         self.hrm_btn_click(self.Emeadd)
#         time.sleep(3)
#
#     def login15(self):
#         self.hrm_btn_click(self.add1)
#         time.sleep(4)
#
#     def login16(self, pic):
#         self.hrm_btn_click(self.browse)
#         pic = r"C:\Users\bindu.madhavi\Downloads\chill.jpg"
#         # driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(pic)
#         self.hrm_send_keys(self.browse,pic)
#         time.sleep(5)
#
#     def login17(self):
#         self.hrm_btn_click(self.save3)
# ###################################################################################
#     def login18(self):
#         self.hrm_btn_click(self.depend)
#         time.sleep(3)
#
#     def login19(self):
#         self.hrm_btn_click(self.add2)
#         time.sleep(3)
#
#     def login20(self, Heyy):
#         self.hrm_btn_click(self.name)
#         time.sleep(3)
#         self.hrm_send_keys(self.name,Heyy)
#
#     def login21(self, c):
#         self.hrm_btn_click(self.relation)
#         self.hrm_send_keys(self.relation,c)
#         time.sleep(4)
#         a = (By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
#         self.hrm_btn_click(self,a)
#         time.sleep(4)
#
#     def login22(self, a):
#         self.hrm_btn_click(self.date)
#         current_date = datetime.now()
#         next_date = current_date + timedelta(days=1)
#         formatted_date = next_date.strftime("%Y-%d-%m")
#         a=(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
#         # Keys.TAB clicks the tab key
#         self.hrm_btn_click(self.date,a)
#
#     def login23(self):
#         self.hrm_btn_click(self.save4)
#
#     #################################################################################
#     # def login24(self):
#     #     self.hrm_btn_click(self.immigration)
#     #     time.sleep(3)
#     #
#     # def login25(self):
#     #     self.hrm_btn_click(self.delete)
#     #     time.sleep(4)
#     #
#     # def login26(self):
#     #     self.hrm_btn_click(self.edit)
#     #     time.sleep(4)
#     #
#     # def login27(self):
#     #     self.hrm_btn_click(self.browse1)
#     #     pic = r"C:\Users\bindu.madhavi\Downloads\chill.jpg"
#     #     # driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(pic)
#     #     self.hrm_send_keys(self.browse, pic)
#     #     time.sleep(3)
#     #
#     # def login28(self,lovemyself):
#     #     self.hrm_btn_click(self.comment1)
#     #     time.sleep(4)
#     #     actions = ActionChains(self.driver)
#     #     actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
#     #     time.sleep(3)
#     #     self.hrm_send_keys(self.comment1,lovemyself)
#     #
#     # def login29(self):
#     #     self.hrm_btn_click(self.save5)
#     #     time.sleep(5)
#
# #############################################
#     # def key1(self):
#     #     self.hrm_btn_click(self.add3)
#     #     time.sleep(5)
#     #
#     # def key2(self, CTS):
#     #     self.hrm_send_keys(self.company, CTS)
#     #     time.sleep(5)
#     #
#     # def key3(self, DataAnalyst):
#     #     self.hrm_send_keys(self.job_title, DataAnalyst)
#     #     time.sleep(5)
#     #
#     # def key4(self):
#     #     self.hrm_btn_click(self.save6)
#     #     time.sleep(5)
#     #
#     # def key5(self):
#     #     self.hrm_btn_click(self.level)
#     #     a = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     time.sleep(3)
#     #     for i in a:
#     #         if i.text == 'College Undergraduate':
#     #             i.click()
#     #         break
#     #     time.sleep(4)
#     #
#     # def key6(self, Crescent):
#     #     self.hrm_send_keys(self.institute, Crescent)
#     #     time.sleep(5)
#     #
#     # def key7(self, computerscience):
#     #     self.hrm_send_keys(self.specialization, computerscience)
#     #     time.sleep(5)
#     #
#     # def key8(self, a):
#     #     # a = 2024
#     #     self.hrm_send_keys(self.year, a)
#     #     time.sleep(5)
#     #
#     # def key9(self, b):
#     #     # a = 9.2
#     #     self.hrm_send_keys(self.gpa, b)
#     #     time.sleep(5)
#     #
#     # def key10(self):
#     #     self.hrm_btn_click(self.save7)
#     #     time.sleep(5)
#     #
#     # def key11(self):
#     #     self.hrm_btn_click(self.skill)
#     #     skill1 = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     for i in skill1:
#     #         if i.text == 'Python':
#     #             i.click()
#     #         break
#     #     time.sleep(4)
#     #
#     # def key12(self, z):
#     #     # z=12
#     #     self.hrm_send_keys(self.yexp, z)
#     #     time.sleep(5)
#     #
#     # def key13(self):
#     #     self.hrm_btn_click(self.la)
#     #     lang = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     time.sleep(3)
#     #     for i in lang:
#     #         if i.text == 'French':
#     #             i.click()
#     #             break
#     #     time.sleep(5)
#     #
#     # def key14(self):
#     #     self.hrm_btn_click(self.competency)
#     #     com = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     time.sleep(3)
#     #     for i in com:
#     #         if i.text == 'Good':
#     #             i.click()
#     #         break
#     #     time.sleep(5)
#     #
#     # def key15(self):
#     #     self.hrm_btn_click(self.memb)
#     #     mem = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     for i in mem:
#     #         if i.text == 'British Computer Society (BCS)':
#     #             i.click()
#     #             break
#     #     time.sleep(3)
#     #
#     # def key16(self):
#     #     self.hrm_btn_click(self.currency)
#     #     cur = (By.CSS_SELECTOR, ".oxd-select-option span")
#     #     for i in cur:
#     #         if i.text == 'Indian Rupee':
#     #             i.click()
#     #             break
#     #     time.sleep(3)
#
    def logout(self):
        self.hrm_btn_click(self.click)
        self.hrm_btn_click(self.Logout)
        time.sleep(3)

#     def get_title(self, title):
#         self.hrm_get_title(title)


