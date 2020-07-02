from video_code.tests.acceptance.locators.home_page import HomePageLocators
from video_code.tests.acceptance.page_model.base_page import BasePage

# * Antes de uma variavel transforma uma tupla,lista em 2 objetos separados.
# Ex: (By.TAG_NAME,'id') transformaria em => By.TAG_NAME, 'id'

class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)