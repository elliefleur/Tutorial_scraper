# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
#this imports the scraperwiki library of functions
import lxml.html
#this imports the lxml.html library of functions
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
#this uses the scrape function from the scraperwiki library on the url uk.soccerway...fortuna-sittard and turns it into a variable called html. Change url for a different website
#print html
#this prints the results of the scrape function on the soccerway url
root = lxml.html.fromstring(html)
#this performs the fromstring function from the lxml.html library on the variable html which is the results of the scrape function on the soccerway url and turns the varible called root into an object
tds = root.cssselect("td")
#uses the cssselect method on the root to grab "td" tags and put in variable called tds - change td to a different selector to grab something else on the page


# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
