import requests
from bs4 import BeautifulSoup
import json

page = requests.get('https://coronavirus-dashboard.utah.gov/#outbreaks')
soup = BeautifulSoup(page.content, 'html.parser')

outbreaks_scriptdata = soup.find("script",attrs={"data-for":"htmlwidget-00c922b077adb863e8f8"}).contents
outbreaks_data = []
outbreaks_data.append(json.loads("".join(outbreaks_scriptdata[0])))
outbreaks_data = outbreaks_data[0]['x']['data']

# Total Outbreaks = 0 index
# Total Cases = 1 index
# Total Hospitalizations = 2 index
# Total Deaths = 3 index
# Male % / Female % = 4 index
# Median Age = 5 index

# Column 0 = Demographic
# Column 1 = Workplace
# Column 2 = Hospital / Clinic
# Column 3 = Group Living
# Column 4 = Detention Facility
# Column 5 = School
# Column 6 = Childcare
# Column 7 = Other Setting

print(outbreaks_data)
