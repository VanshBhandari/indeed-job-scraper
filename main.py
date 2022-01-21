import requests
from bs4 import BeautifulSoup

user_input_keyword = input("enter the keyword for jobs that you want to search: ")
user_input_keyword = "+".join(user_input_keyword.split(" "))
user_input_location = input("enter the location: ")
user_input_location = "+".join(user_input_location.split(" "))
user_input_pages = int(input("how many pages do you want to search?: "))


def extract(page):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    url = f'https://ca.indeed.com/jobs?q={user_input_keyword}&l={user_input_location}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def data(soup):
    div = soup.find_all('div', class_='job_seen_beacon')
    for job in div:
        title = job.find('span').text.strip()
        company = job.find('span', class_='companyName').text.strip()
        location = job.find('div', class_='companyLocation').text.strip()
        try:
            salary = job.find('div', class_='salary-snippet').text.strip()
        except:
            salary = 'salary not given'

        summary = (
            f'job title: {title}\ncompany name: {company}\njob location: {location}\nsalary: {salary}\n'
        )
        print(summary)

    return

for i in range(0, user_input_pages):
  c = extract(0)
  data(c)
