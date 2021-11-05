## Scrapping in Python by using BeautifulSoup

## Objective of Project
- In this project, we are doing scrapping while using beautifulsoup library of python. We have get validated data from           https://www.goodreads.com/book/popular_by_date


## Setup Project

1. Clone the project using following command
```
git clone https://github.com/AMOIZ0866/scrapping.git
```

2. Make sure you have python 3 installed in your system

3. Make sure you have install these packages of python 
    -  pip3 install requests 
    -  pip3 install html5lib
    -  pip3 install bs4 
    -  pip3 install selenium 
    -  brew cask install chromedriver
          
    
## Procedure
   In the main we have to parts:
   - Getting Data
   - Analysis of data
   
 - In the Getting data there is function with name 'fetching_links_scrap()' this function will be used to fetch book data and write them in a json file(data.json)
   
   In the second part we have class of Analysis which function that perform differnt type of analysis by using panada dataframe:
   - "analysis.get_high_rating()" for making a small graph showing the top 10 highest rated books.
   - "analysis.get_author_with_most_books()" for list of authors who had the most number of books in the popular book
   - "analysis.get_genres_with_number_of_books()" for list all the genres in order of number of books.
   - "analysis.get_avg_rating_genres()" for calculating the average rating of books in a genre.

## Git Branching Structure
- Default latest branch is **Staging**
- Dev is child branch for development
- Every task branch finally merged in Staging upon completion/review.

## How to deploy new changes
- Create a new branch from **staging** branch
- Update the codebase according to the change-set required
- Create a **Pull Request** with **staging** branch
- Review & Merge that PR

