# Yoga_scraper
web crawler that scrapes yoga studio info from an online directory

This app scrapes Name and Address information from a directory of yoga studios and places them into a CSV.  I responded to a craigslist post requesting data entry for someone to fill out a spreadsheet by hand, and I thought: "I could just build a scraper that could automate this!"  To some degree, it's my first project after code school where I really felt empowered by coding to do something that someone needed.  Very cool!

The program begins with yoga_scraper (verify), which uses Selenium to click through the web elements on the site and pull the Name and Addres information, which is stored in a .csv file.

Then, That .csv is parsed to differentiate the name, address, city, and state.  This is where the data was cleaned and normalized.

Finally, to find the phone numbers for search results, I built a second crawler that does a google search for "NAME CITY 'phone number'" and appends those results to the scraped list.
