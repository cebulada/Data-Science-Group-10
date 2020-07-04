# Hello group

## Here are some interesting Datasets that I have found that are pretty granular with little to no aggregation

## These datasets I have found contain as little as 100,000 records to up to 2.5 million records
- I would have to say that none of this is aggregated whatsoever and they are very raw

## I have downloaded most of the datasets and placed them in the data folde and their own subfolders

## Please look at this jupyter notebook for a preliminary look at the data - [link](./preliminary.ipynb)

1. New York City CitiBike - [link](https://www.citibikenyc.com/system-data)
- I downloaded the sample data into the 01/ folder
- Here are the columns in the data set

<ul><li>Trip Duration (seconds)</li><li>Start Time and Date</li><li>Stop Time and Date</li><li>Start Station Name</li><li>End Station Name</li><li>Station ID</li><li>Station Lat/Long</li><li>Bike ID</li><li>User Type (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member)</li><li>Gender (Zero=unknown; 1=male; 2=female)</li><li>Year of Birth</li></ul>

2. Ontario Lake Water Quality at Drinking Water Stations - [link](https://data.ontario.ca/dataset/lake-water-quality-at-drinking-water-intakes)
- there are 4 great lakes and lake simcoe and several drinking water stations for each lake
- I downloaded the sample data into the 02/ folder
- its in long form so we will need to convert it

3. Ontario Great Lake Sediment Chemistry = [link](https://data.ontario.ca/dataset/sediment-chemistry-great-lakes-nearshore-areas)
- sediment data
- I downloaded the sample data into the 03/ folder
- its in long form so we will need to convert it

4. Bike Share Toronto Ridership Data - [link](https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/)
- toronto bikeshare data
- very few columns
- I downloaded the sample data into the 04/ folder

5. Toronto Daily Homeless Shelter Occupance - [link](https://open.toronto.ca/dataset/daily-shelter-occupancy/)
- occupancy of homeless shelters in Toronto
- I downloaded sample data into the 05/ folder

6. Toronto Fire Incidents - [link](https://open.toronto.ca/dataset/fire-incidents/)
- a lot of columns with statistics
- I downloaded sample data into the 06/ folder

7. Toronto Parking Data - [link](https://open.toronto.ca/dataset/parking-tickets/)
- not a lot of columns
- data is in long form
- I downloaded sample data into the 07/ folder

8. Amazon Reviews Dataset - [link](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)
- I have chosen to download automotive reviews - [link](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Automotive_v1_00.tsv.gz)
- the file is > 500 MB in size
- ~2.5 million reviews is nothing to discount...
