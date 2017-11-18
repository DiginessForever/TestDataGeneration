import os, urllib, time, sys, requests, random
from PIL import Image
from selenium import webdriver
 
chromedriverpath = "C:\\Users\\jacob.johnson\\code\\randomEmployeeFileGenerator\\chromedriver"
browser = webdriver.Chrome(chromedriverpath)
 
url = "http://www.fakenamegenerator.com/gen-random-ar-gr.php"
 
iterations = 5000
 
for x in range(iterations):
    browser.get(url)

    #Auto diversity:
    randomOption = random.randrange(1,37) #There are 37 possible nameset types - they go by region/nationality
    print("Name set culture: " + str(randomOption))
    browser.find_element_by_xpath('//*[@id="n"]/option[' + str(randomOption) + ']').click()  #set the nameset selectbox to a random option.
                                                                    
    #Randomize country
    randomCountry = random.randrange(1,31) #It has 31 possible countries the fake employees can be from.
    browser.find_element_by_xpath('//*[@id="c"]/option[' + str(randomCountry) + ']').click()
    print("Country set to: " + str(randomCountry))

    name = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/h3')
    print("Name: " + name.text)
    output = "Name: " + name.text + '\n'

    gender = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[1]/div/div[1]/img').get_attribute('alt')
    print("Gender: " + gender)
    output += "Gender: " + gender + '\n'

    mothersMaiden = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[1]')
    print("Mother's maiden: " + mothersMaiden.text)
    output += "Mother's maiden: " + mothersMaiden.text + '\n'

    height = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[18]/dd')
    print("Height: " + height.text)
    output += "Height: " + height.text + '\n'

    weight = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[19]/dd')
    print("Weight: " + weight.text)
    output += "Weight: " + weight.text + '\n'

    bloodType = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[20]/dd')
    print("Blood Type: " + bloodType.text)
    output += "Blood Type: " + bloodType.text + '\n'

    phone = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[3]')
    print(phone.text)
    output += phone.text + '\n'

    address = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[1]/div')
    print("Address: " + address.text)
    output += "Address: " + address.text + '\n'

    countryCode = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd')
    print("Country Code: " + countryCode.text)
    output += "Country Code: " + countryCode.text + '\n'

    geoCoordinates = browser.find_element_by_xpath('//*[@id="geo"]')
    print("Geo Lat/Long: " + geoCoordinates.text)
    output += "Geo Lat/Long: " + geoCoordinates.text + '\n'

    birthday = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[5]/dd')
    print("Birthday: " + birthday.text)
    output += "Birthday: " + birthday.text + '\n'

    age = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[6]/dd')
    print(age.text)
    output += age.text + '\n'

    email = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[8]/dd')
    print("Email: " + email.text)
    output += "Email: " + email.text + '\n'

    #spoofEmailAddress = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[8]/dd/div/a').get_attribute('href')
    #print("Send email from above: " + spoofEmailAddress)
    #output += "Send email from above: " + spoofEmailAddress + '\n'

    username = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd')
    print("Username: " + username.text)
    output += "Username: " + username.text + '\n'

    password = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[10]/dd')
    print("Password: " + password.text)
    output += "Password: " + password.text + '\n'

    website = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[11]/dd')
    print("Website: " + website.text)
    output += "Website: " + website.text + '\n'

    browserUserAgent = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[12]/dd')
    print("Browser's User Agent: " + browserUserAgent.text)
    output += "Browser's User Agent: " + browserUserAgent.text + '\n'

    print("Financial Details:")
    creditCardType = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[13]/dt')
    creditCardNumber = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[13]/dd')
    creditCardExpiration = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[14]/dd')
    creditCardCV2 = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[15]/dd')
    print("Credit Card: " + creditCardType.text + ", " + creditCardNumber.text + ", Expires: " + creditCardExpiration.text + ", CV2: " + creditCardCV2.text)
    output += "Credit Card: " + creditCardType.text + ", " + creditCardNumber.text + ", Expires: " + creditCardExpiration.text + ", CV2: " + creditCardCV2.text + '\n'

    employer = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[16]/dd')
    print("Employer: " + employer.text)
    output += "Employer: " + employer.text + '\n'

    occupation = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[17]/dd')
    print("Occupation: " + occupation.text)
    output += "Occupation: " + occupation.text + '\n'

    personalVehicle = browser.find_element_by_xpath('//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[25]/dd')
    print("Vehicle: " + personalVehicle.text)
    output += "Vehicle: " + personalVehicle.text

    #Write out to a file - need to have built a string to write.
    savePath = "C:\\ManagedShare\\" + name.text + '.txt'
    myFile = ''
    if not os.path.exists(savePath):
        print('File path does not exist')
        myFile = open(savePath, 'w')
        myFile.write(output)
        myFile.close()
        #time.sleep(2.0)