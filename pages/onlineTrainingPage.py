from selenium.webdriver.common.by import By
import time

class OnlineTraining:
    def __init__(self, driver):
        self.driver = driver

    
    # locators
    Title = (By.XPATH, "//h1[normalize-space()='SDET-QA']")  
    DESCRIPTION = (By.XPATH, "//p[@class='description']")
    IMAGE = (By.XPATH, "//img[@width='640']") 
    HEADER_SECTION = (By.CSS_SELECTOR, "div[id='PageList1'] div[class='widget-content']")
    P = (By.TAG_NAME, "p")
    REGISTER_LINK = (By.XPATH, "//a[normalize-space()='Register Here']")
    SELENIUM_COURSE_LINK = (By.XPATH, "//a[normalize-space()='Selenium with Python Course Contents']")
    PAYNOW_FORM = (By.XPATH, "//form[@action='https://www.paypal.com/cgi-bin/webscr']")
    YOUTUBE_LINK = (By.XPATH, "//a[@href='https://www.pavanonlinetrainings.com/p/selenium-with-python-course-contents.html']")
    SOCIAL_MEDIA_SECTION = (By.CLASS_NAME, "post-share-buttons")
    SOCIAL_MEDIA_LINKS = (By.TAG_NAME, "a")
    PROFILE_IMAGE = (By.XPATH, "//img[@border='0'][@height='360']")
    LOAD_MORE_BUTTON = (By.XPATH, "//button[normalize-space()='Load more reviews']")
    EMBED_LINK = (By.XPATH, "//a[normalize-space()='Embed Google Reviews on your Blogger website']")
    ATOM_LINK = (By.XPATH, "//a[normalize-space()='Posts (Atom)']")
    FOOTER_SECTION = (By.CLASS_NAME, "widget-content")
    FOOTER_LINKS = (By.TAG_NAME, "a")

     
    # Title
    def title(self):
        print("---- Online Training Page ----")
        title = self.driver.find_element(*self.Title)
        print("Title is: ",title.text)
        time.sleep(2)

    # Description
    def description(self):
        description = self.driver.find_element(*self.DESCRIPTION)
        print("description is: ",description.text)
        time.sleep(2)
        print("")

    # Background Image
    def image(self):
        image = self.driver.find_element(*self.IMAGE) 
        print("image is: ",image.get_attribute("src"))
        time.sleep(2)
        print("")

    
    # Header links
    def heading(self):
        print("---- Header links ----")
        header = self.driver.find_element(*self.HEADER_SECTION)
        header_links = header.find_elements(By.TAG_NAME, "ul")
        for link in header_links:
            print(link.text)
            print("\n")
        print("")
    
    
    # Parahraphs 
    def parahraph(self):
        print("---- Body texts ----")
        p = self.driver.find_elements(*self.P)
        for p in p:
            print(p.text)
            print("")
        print("")


    # Other links
    def links(self):
        print("---- Other Links ----")
    
        # Register Here link 
        self.driver.find_element(*self.REGISTER_LINK)
        print("Register Here link clicked")
        time.sleep(2)

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)


        # Login Here link
        self.driver.find_element(*self.SELENIUM_COURSE_LINK)
        print("Login Here link clicked")
        time.sleep(2)

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)


        # Pay Now link 
        Paynow = self.driver.find_element(*self.PAYNOW_FORM)
        Paynow.click()
        print("Pay Now link clicked")
        time.sleep(2)

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)


        # Youtube link
        youtube = self.driver.find_element(*self.YOUTUBE_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", youtube)
        self.driver.execute_script("arguments[0].click();", youtube)
        print("Youtube link clicked")
        time.sleep(2)

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)
        print("")


    # Social media links
    def socialmedia(self):
        print("---- Social Media links ----")
        socialmedia = self.driver.find_element(*self.SOCIAL_MEDIA_SECTION)
        socialmedia_links = socialmedia.find_elements(By.TAG_NAME, "a")
        for link in socialmedia_links:
            print(link.get_attribute("href"))
            print("")
        print("")


    # Profile and Subscribe links and buttons
    def profile(self):
        print("---- Profile and Subscribe links ----")
        profile = self.driver.find_element(*self.PROFILE_IMAGE)
        profile.click()
        print("Profile link clicked")

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)
        print("")

    
    
    # Load more button
    def loadmore(self):
        print("---- Load More button ----")
        loadmore = self.driver.find_element(*self.LOAD_MORE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", loadmore)
        self.driver.execute_script("arguments[0].click();", loadmore)
        print("Load More link clicked")
        print("")

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)


    # Embed Link
    def embed(self):
        print("---- Embed link ----")
        embed = self.driver.find_element(*self.EMBED_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", embed)
        self.driver.execute_script("arguments[0].click();", embed)
        print("Embed link clicked")
        time.sleep(2)
        print("")

        self.driver.back()


    # Footer Links
    def footer(self):
        print("---- Footer links ----")
        footer = self.driver.find_element(*self.FOOTER_SECTION)
        footer_links = footer.find_elements(*self.FOOTER_LINKS)
        for link in footer_links:
            print(link.text)
        print("")
                
