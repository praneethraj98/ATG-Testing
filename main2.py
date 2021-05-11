import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "platformName": "Android",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appWaitDuration": "5000",
    "appExecTimeout": "5000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "appPackage": "com.ATG.World",
    "deviceName": "your device",
    "driver": "http://localhost:4723/wd/hub",
    "app ": "D:\\Programming\\Appium-APKs",
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)


def test_LoginWithRightCredential():

    driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
    driver.find_element_by_id("com.ATG.World:id/login_email").click()
    email = driver.find_element_by_id("com.ATG.World:id/email")
    email.send_keys("wiz_saurabh@rediffmail.com")
    password = driver.find_element_by_id("com.ATG.World:id/password")
    password.send_keys("Pass@123")
    signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
    signin.click()
    print("test_LoginWithRightCredential passed")


test_LoginWithRightCredential()
time.sleep(3)
TouchAction(driver).tap(None, 221, 1122).perform()
time.sleep(3)
TouchAction(driver).tap(None, 228, 1303).perform()
time.sleep(3)
TouchAction(driver).tap(None, 716, 2185).perform()
time.sleep(3)
TouchAction(driver).tap(None, 944, 966).perform()
time.sleep(3)
driver.find_element_by_id(
    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
).click()
time.sleep(3)
driver.find_element_by_id(
    "com.android.permissioncontroller:id/permission_allow_button"
).click()
Btn = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]"
)

TouchAction(driver).tap(None, 626, 1277).perform()
time.sleep(3)
TouchAction(driver).tap(None, 300, 561).perform()
time.sleep(3)
TouchAction(driver).tap(None, 300, 561).perform()
time.sleep(3)
TouchAction(driver).tap(None, 181, 597).perform()
time.sleep(3)
TouchAction(driver).tap(None, 1284, 224).perform()
time.sleep(3)
caption = driver.find_element_by_id("com.ATG.World:id/postCaption")
caption.send_keys("test").click()
driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()
print("Image succesffuly posted to ATG world!")
