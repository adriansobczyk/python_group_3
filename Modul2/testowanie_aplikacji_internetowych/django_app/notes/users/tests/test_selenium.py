from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Użycie webdriver_manager do automatycznego pobrania i konfiguracji ChromeDriver
        cls.service = Service(ChromeDriverManager().install())
        cls.browser = webdriver.Chrome(service=cls.service)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_navigation_to_login(self):
        # Przejdź do strony głównej
        self.browser.get(self.live_server_url)
        self.assertIn("Homepage", self.browser.title)

        # Znajdź i kliknij link do logowania (dostosuj selektor do faktycznego HTML)
        login_link = self.browser.find_element(By.LINK_TEXT, "Login")
        login_link.click()

        # Sprawdź, czy jesteśmy na stronie logowania
        self.assertIn("/users/login", self.browser.current_url)
        self.assertIn("Sample app", self.browser.title)
