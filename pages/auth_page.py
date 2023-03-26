from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=312322e5-94fa-41eb-880e-6e97327a1605&theme&auth_type'
        super().__init__(web_driver, url)

    phone = WebElement(id='username')

    email = WebElement(id='username')

    login = WebElement(id='username')

    pa = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(id='kc-login')

    recovery = WebElement(id='forgot_password')

    registration = WebElement(id='kc-register')

    code = WebElement(id='back_to_otp_btn')

    auth_code = WebElement(id='address')

    get_code = WebElement(id='otp_get_code')

    rt_code = WebElement(id='rt-code-0')

    captcha = WebElement(alt='Captcha')

    symbol = WebElement(id='captcha')

    contin = WebElement(id='reset')

    new_pass = WebElement(id='password-new')

    confirm = WebElement(id='confirmation')

    save = WebElement(id='t-btn-reset-pass')

    name = WebElement(name='firstName')

    lastname = WebElement(name='lastName')

    region = WebElement(autocomplete='new-password')

    email_or_phone = WebElement(id='address')

    confirmation = WebElement(id='password-confirm')

    register = WebElement(id='register')

