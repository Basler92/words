from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def count_words_on_page(url):
    # Inicjalizacja przeglądarki
    driver = webdriver.Chrome()  # Tutaj możesz użyć innej przeglądarki, jeśli preferujesz

    try:
        # Otwarcie strony
        driver.get(url)
        time.sleep(2)  # Poczekaj chwilę na załadowanie strony

        # Pobierz tekst ze strony
        page_text = driver.find_element_by_tag_name('body').text

        # Podziel tekst na słowa i policz ich ilość
        word_count = len(page_text.split())

        # Wyświetl wynik
        print(f'Ilość słów na stronie {url}: {word_count}')

    except Exception as e:
        print(f'Wystąpił błąd: {e}')

    finally:
        # Zamknij przeglądarkę
        driver.quit()

# Przykładowe użycie
url_to_test = 'https://www.example.com'
count_words_on_page(url_to_test)
