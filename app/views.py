from flask import render_template
from app import app
import cgi, cgitb 
import os
from xml.etree import ElementTree
#initalize getting info from the HTML
form = cgi.FieldStorage() # instantiate only once!
#import XML file
file_name = 'testrecords.xml'
full_name = os.path.abspath(os.path.join('app/xml', file_name))
# get variables from html 

htmlName = 'lewis'# form.getfirst('name', 'empty')
htmlNumber = 1 #form.getvalue('searchcrit')

#htmlName = cgi.escape(htmlName)

# initialize variables
search = ['blank','name','activity','year','title']
searchnumber = ['1','2','3','4']

def searchingall (filename):
    doc = ElementTree.parse(filename)
    records = doc.findall('record')
    return (records)
def display (searchXML,htmlName,htmlNumber,search):
    displaycounter = -1
    name = ['None']
    activity = ['None']
    record = ['None']
    num = ['None']
    year = ['None']
    
    for x in searchXML:
        if htmlName == (x.find(search[int(htmlNumber)]).text):
            displaycounter = int(displaycounter) + 1
            name.append(displaycounter)
            activity.append(displaycounter)
            record.append(displaycounter)
            num.append(displaycounter)
            year.append(displaycounter)
            name[displaycounter] = x.find('name').text
            activity[displaycounter] = x.find('activity').text
            record[displaycounter] = x.find('title').text
            num[displaycounter] = x.find('numvalue').text
            year[displaycounter] = x.find('year').text
    displaycounter = displaycounter + 1
    name[displaycounter] = "Empty"
    return(name, activity, record, num, year)

searchXML = searchingall(full_name) #finds all xml entries
(name, activity, record, num, year) =  display(searchXML,htmlName,int(htmlNumber),search) 
#all vars coming out of the line above are arrays
x = 0
addedArrays = ["None"]
while name[x] != "Empty":
    addedArrays[x] = (str(name[x])+ "," + str(activity[x]) +","+ str(record[x]) +","+ str(num[x])+","+ str(year[x]))
    x = x + 1
    addedArrays.append(x)






@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': addedArrays}  
    return render_template('index.html',
                           title='Home',
                           user=user)
