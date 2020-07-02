from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from video_code.tests.acceptance.page_model.blog_page import BlogPage
from video_code.tests.acceptance.page_model.home_page import HomePage
from video_code.tests.acceptance.page_model.new_post_page import NewPostPage

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

use_step_matcher('re')

@given('Start chromedriver')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)

@given('I am on the homepage')
def step_impl(context):
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url