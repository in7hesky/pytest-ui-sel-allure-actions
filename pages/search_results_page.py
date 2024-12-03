from pages.abstract.base_page import BasePage


class SearchResultsPage(BasePage):
    
    PRODUCT_SELECTOR = ("class name", "product")
    PAGE_TITLE_SELECTOR = ("class name", "page-title")
    ADD_TO_CART_BUTTON_SELECTOR = ("class name", "add_to_cart_button")
    
    def get_page_title_string(self):
        return self.find_element(self.PAGE_TITLE_SELECTOR).text
    
    def get_product_by_index(self, index):
        return self.find_elements(self.PRODUCT_SELECTOR)[index]
    
    def add_product_by_index(self, index):
        return self.get_product_by_index(index) \
            .find_element(*self.ADD_TO_CART_BUTTON_SELECTOR).click()