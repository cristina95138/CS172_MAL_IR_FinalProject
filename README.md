# CS172_MAL_IR_FinalProject

## Part 1: Crawler

### Design:

#### (a) Architecture
<img src="1200px-WebCrawlerArchitecture.svg.png" alt="drawing" width="500"/>

#### (b) The Crawling or data collection strategy (do you handle duplicate URLs, is your crawler parallel, etc.)
- Grabs url content from MAL.
- Use BeautifulSoup to turn url content to lxml format.
- Search through BeautifulSoup lxml document for names, ratings, descriptions, ranks, and num_episodes.
- When crawling website wait 60 senconds for each request.
- Create dataframe with all information.
- Convert dataframe to csv file called output.csv.

#### (c) Data Structures employed
- Lists
- Dataframe

### Run Instructions:

1. python3 crawler.py

## Part 2: Indexer

### Design:

- Creates Elasticsearch index from csv created from the crawler
- Gets inputted searches from command line
- Employs es.search in order to search through creasted index for searches inputted on the command line
- Outputs the search results

### Run Instructions:

1. Run your Elasticsearch locally
2. python3 retrievalSystem.py
3. Input search items into search input

## Part 3: Extension

### Design:

### Run Instructions:
