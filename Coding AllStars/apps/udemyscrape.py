import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv



def printer():
    
    with open("./apps/result.csv", 'w') as result:
        fieldnames = ["Title", "Description", "Author", "Rating",
        "Reviews", "Total Hours", "Number of Lectures", "Difficulty",
        "Discounted Price", "Original Price", "Tags"]

        writer = csv.writer(result)

        writer.writerow(fieldnames)

        for i in range(len(title)):
            writer.writerow([title[i], descri[i], aut[i], rate[i],
            rev[i], tothour[i], lect[i], dif[i], price[i], orprice[i], tags[i]])

    print("Scraping Completed!")





def start():

    print("Scraping Starts Now...")

    for page in range(1,int(maxp)):

        driver.get(url + "?p=" + str(page))

        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located
            ((By.CLASS_NAME, "pagination--page--13HGb")))
            time.sleep(2)
        except TimeoutException:
            print("\n\nPage TimeOut, please check your Internet Connection.")
            driver.quit()


        soup = BeautifulSoup(driver.page_source, "html.parser")
        maincont = soup.find('div', class_="course-list--container--3zXPS") #getMainContainer
        res = maincont.find_all('div', class_="course-card--main-content--2XqiY")



        for i in res:
            unused = i.find('div', class_="ud-sr-only").text
            title.append(i.find('a').text.replace(unused,"")) #getTitle

            descri.append(i.find('p', class_="course-card--course-headline--2DAqq").text) #getdescription

            aut.append(i.find('div', class_="ud-text-xs").text.replace("Instructor:","").replace("Instructors:", "")) #getAuthor

            rate.append(i.find('span', class_="star-rating--rating-number--3l80q").text + " out of 5") #getRating

            rev.append(i.find('span', class_="course-card--reviews-text--1yloi").text.strip("()")) #getNumberOfReviews

            finspan2 = i.find_all('span', class_="course-card--row--29Y0w")
            tothour.append(finspan2[0].text) #getTotalHour
            lect.append(finspan2[1].text) #getNumberOfLectures
            dif.append(finspan2[2].text) #getDifficulty

            price.append(i.find('div', class_="course-card--discount-price--1bQ5Q").text.replace("Current price","")) #getCurrentPrice
            orprice.append(i.find('div', class_="price-text--original-price--1sDdx").text.replace("Original Price", "")) #getOriginalPrice

            try: #getTagsIfAvailable
                tags.append(i.find('div',class_="ud-badge").text)
            except:
                tags.append("None")
        

            if len(title) == 90:
                break
        
        if len(title) == 90:
            driver.quit()
            break
    printer()





title, descri, aut, rate, rev, tothour, lect, dif, price, orprice, tags = ([] for i in range(11))

driver = uc.Chrome()
url = "https://www.udemy.com/courses/development/web-development/"
driver.get(url)
driver.minimize_window()


try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located
    ((By.CLASS_NAME, "pagination--page--13HGb")))
    time.sleep(2)
except TimeoutException:
    print("\n\nPage TimeOut, please check your Internet Connection.")
    driver.quit()

time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
maxp = soup.find('span', class_="pagination--page--13HGb").text #getmaxpage


start()


