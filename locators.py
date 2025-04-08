from selenium.webdriver.common.by import By

class Locators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка 'Войти в аккаунт' с главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка 'Войти в аккаунт'
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Окно входа с полями майл и пароль, ссылка "Зарегистрироваться"
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # Окно регистрации, поле 'Имя'
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']") # Поле 'Email'
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле 'Пароль'
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Окно регистрации, кнопка 'Зарегистрироваться'
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка 'Оформить заказ'
    ERROR_INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Ошибка 'Некорректный пароль'
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка 'Личный Кабинет'
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # Ссылка 'Войти' на странице регистрации
    PROFILE = (By.XPATH, "//a[text()='Профиль']") # Элемент 'Профиль' на странице личного кабинета
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") # Кнопка 'Конструктор'
    LOGO = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]") # Логотип Stellar Burgers
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text() = 'Соберите бургер']") # Заголовок 'Соберите бургер' на главно странице
    LOG_OUT = (By.XPATH, "//button[text()='Выход']") # Кнопка 'Выход'
    TUB_BUNS = (By.XPATH, "//span[text()='Булки']") # Раздел 'Булки'
    TUB_SAUCES = (By.XPATH, "//span[text()='Соусы']") # Раздел 'Соусы'
    TUB_FILLINGS = (By.XPATH, "//span[text()='Начинки']") # Раздел 'Начинки'
    CURRENT_TUB_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/child::span[text()='Булки']") # Выбранный раздел 'Булки'
    CURRENT_TUB_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/child::span[text()='Соусы']") # Выбранный раздел 'Соусы'
    CURRENT_TUB_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/child::span[text()='Начинки']") # Выбранный раздел 'Начинки'