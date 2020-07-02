from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from video_code.tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')

@step('I wait for the posts to load')
def step_impl(context):
    # WebDriverWait(context.driver, 10).until(
        # EC.presence_of_element_located(BlogPageLocators.POSTS_SECTION)
    # )
    time.sleep(10)
