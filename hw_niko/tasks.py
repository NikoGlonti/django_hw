from datetime import datetime

from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Quote


def send_message():
    send_mail(
        subject='Parsing',
        message='Quotes are over',
        from_email="test@mail.com",
        recipient_list=['admin.parsing@mail.com'],
    )


@shared_task
def parser():
    url = 'https://quotes.toscrape.com'
    quotes_num = 5
    page_num = 1

    while quotes_num > 0:
        req = requests.get(f'{url}/page/{str(page_num)}/')
        soup = BeautifulSoup(req.content, features='lxml')
        quotes = soup.findAll('div', class_='quote')

        for el in quotes:
            text_quota = el.find('span', class_='text').text

            if not Quote.objects.filter(text_quota=text_quota).exists():

                url_ends = el.find('small', class_='author').find_next_sibling('a').get('href')
                auth_url = f'{url}/{url_ends}'
                auth_r = requests.get(auth_url)
                auth_soup = BeautifulSoup(auth_r.content)
                author_block = auth_soup.find('div', class_='author-details')

                name = author_block.find('h3', class_='author-title').text

                if not Author.objects.filter(name=name).exists():
                    date_of_birth = datetime.strptime(auth_soup.find(
                                              'span', {'class': 'author-born-date'}).text, '%B %d, %Y').date()
                    biography = author_block.find('div', class_='author-description').text
                    author = Author.objects.create(name=name, date_of_birth=date_of_birth,  biography=biography)

                else:
                    author = Author.objects.get(name=name)

                quote = Quote.objects.create(text_quota=text_quota, author=author)
                quote.save()
                quotes_num -= 1

            if quotes_num != 0 and el == quotes[-1] and not soup.find('li', class_='next'):
                send_message()
                break
        page_num += 1
