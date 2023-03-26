import pytest
import random
from pages.auth_page import AuthPage
from settings import valid_email, valid_password, valid_login, valid_phone, valid_pa
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


def test_registration_email(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Марианна')

    page.lastname.send_keys('Ушакова')

    page.region.send_keys('Пермский край')

    page.email_or_phone.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_email)
    page.get_code.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_registration_phone(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Мария')

    page.lastname.send_keys('Ушакова')

    page.region.send_keys('Москва г')

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)
    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


@pytest.mark.parametrize
def test_registration_phone_negativ(web_browser):

    page = AuthPage(web_browser)

    page.registration.click()

    page.name.send_keys('Мария')

    page.lastname.send_keys('Ушакова')

    page.region.send_keys('Москва г')

    page.email_or_phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.confirmation.send_keys(valid_password)

    page.register.click()

    page.auth_code.send_keys(valid_phone)
    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorisation_login(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=312322e5-94fa-41eb-880e-6e97327a1605&client_id=account_b2c#/'


@pytest.mark.parametrize
def test_authorisation_login_negativ(web_browser):

    page = AuthPage(web_browser)

    page.login.send_keys(valid_login)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=312322e5-94fa-41eb-880e-6e97327a1605&client_id=account_b2c#/'


def test_authorisation_email(web_browser):

    page = AuthPage(web_browser)

    page.email.send_keys(valid_email)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=312322e5-94fa-41eb-880e-6e97327a1605&client_id=account_b2c#/'


def test_authorisation_phone(web_browser):

    page = AuthPage(web_browser)

    page.phone.send_keys(valid_phone)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=312322e5-94fa-41eb-880e-6e97327a1605&client_id=account_b2c#/'


def test_authorisation_check(web_browser):

    page = AuthPage(web_browser)

    page.pa.send_keys(valid_pa)

    page.password.send_keys(valid_password)

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=312322e5-94fa-41eb-880e-6e97327a1605&client_id=account_b2c#/'


def test_authorisation_code_email(web_browser):

    page = AuthPage(web_browser)

    page.code.click()

    page.auth_code.send_keys(valid_email)

    page.get_code.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код авторизации в личном кабинете')
    )

    page2.element.click()

    element2 = driver.find_element(By.TAG_NAME, 'div > p')

    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()

    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorisation_code_phone(web_browser):

    page = AuthPage(web_browser)

    page.code.click()

    page.auth_code.send_keys(valid_phone)

    page.get_code.click()

    page.rt_code.send_keys()

    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_pass_recovery_phone(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.phone.send_keys(valid_phone)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page.rt_code.send_keys()

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'


def test_pass_recovery_email(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'


@pytest.mark.parametrize
def test_pass_recovery_email_negativ(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.email.send_keys(valid_email)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'


def test_pass_recovery_check(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.pa.send_keys(valid_pa)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'


def test_pass_recovery_login(web_browser):

    page = AuthPage(web_browser)

    page.recovery.click()

    page.login.send_keys(valid_login)

    symbols = page.captcha.get_text()

    page.symbol.send_keys(symbols)

    page.contin.click()

    page2 = pytest.driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    element = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(By.TAG_NAME, 'div > span', 'Код подтверждения')
    )
    page2.element.click()
    element2 = driver.find_element(By.TAG_NAME, 'div > p')
    for i in element2:
        numb = i.text.split(' ')
        number = numb[2]
        my_code = number.get_text()
    page = AuthPage(web_browser)

    page.rt_code.send_keys(my_code)

    new_pass = random

    page.new_pass.send_keys(new_pass)

    page.confirm.send_keys(new_pass)

    page.save.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light'
