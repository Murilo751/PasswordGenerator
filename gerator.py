from bs4 import BeautifulSoup
import random
import string


def gerado(passwordBase, tamPass):
    return ''.join(
        random.SystemRandom().choices(
            passwordBase, k=tamPass
        )
    )


char = string.ascii_letters
specialChar = string.punctuation
numbers = string.digits
passwordBase = char + specialChar + numbers

def getpasswordBase():
    return passwordBase

def gettamPass():
    with open('templates/generator.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    input_element = soup.find('input', {'id': 'tamanho'})
    input_value = input_element['value'] if input_element else None

    span_element = soup.find('span', {'id': 'rangeValue'})
    span_text = span_element.text if span_element else None

    

    return tamPass

