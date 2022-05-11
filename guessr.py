from itertools import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Path to chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# Driver we will use
driver = webdriver.Chrome(PATH)

# Characters in English alphabet
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# All vowels and 'y', usually used as vowel
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

# List to save all the valid combinations
citys = []

# Type the possible city and sending it
def send(word):
  inp = driver.find_element_by_id("city-input")
  inp.send_keys(word, Keys.RETURN)

# Entry point
if __name__ == '__main__':

  for i in [3, 4, 5, 6 ,7]:

    # Cartesian product, every loop will create all the possible cartesian products with length i
    x = list(product(characters, repeat= i))

    # Deleting the words that don't have any vowels and appending them to the citys list
    for j in x:
      if any(char in vowels for char in j):
        citys.append(''.join(j))

  # Accesing the page
  driver.get("https://iafisher.com/projects/cities/world")

  # Sending all the 'worlds' generated
  for city in citys:
    send(city)
