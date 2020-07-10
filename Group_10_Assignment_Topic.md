# Group 10 Assignment Topic

## Group Members

### 1. Nidhi, Punja, npunja - [email](npunja@uwaterloo.ca)
### 2. Judith, Roth, j5roth - [email](j5roth@uwaterloo.ca)
### 3. Iman, Dordizadeh Basirabad, idordiza - [email](idordiza@uwaterloo.ca)
### 4. Daniel Adam, Cebula, dacebula - [email](dacebula@uwaterloo.ca)
### 5. Cynthia, Fung, c27fung - [email](c27fung@uwaterloo.ca)
### 6. Ben, Klassen, b6klasse - [email](b6klasse@uwaterloo.ca)
___

## Topic:

Our group would like to determine all the reasons that Toronto Fire Services ([link](https://www.toronto.ca/fire-services)) are called / utlized for emergencies / operations for the year range of 2011 - 2018.  Potential avenues for data exploration are:
- Reasons for the call
    - Fire, Medical, etc.
- The source of the emergency call
    - ambulances, 911 phone calls, etc.
- GPS Coordinates of the call
    - map out neighbourhoods in which fire services are being overused compared to others

Our group has found a Fire Services Basic Incident Detail dataset that is a slice of a larger dataset for the years of 2011 - 2018.  

Per the Open Data Toronto website description:

<hr>
<quote>
    <em>
    This dataset provides information similar to what is sent to the Ontario Fire Marshal relating to all Incidents to which Toronto Fire responds. This dataset also includes response time intervals (dispatch, enroute, arrive and clear) and responding units. For privacy purposes personal information is not provided on all incidents and for medical incidents some information has been altered. If data is related to medical incidents the Forward Sortation Area (FSA) is provided in place of the Major Street and Cross Street fields.
    </em>
</quote>
<hr>

We will merge 2 seperate datasets to the fire incident data as well.
- 1. Historical Toronto Weather dataset aggregated for each day, for each month and each year that encompasses fire incident data in question
    - Weather may play a role in Toronto Fire Services Operations
        - Temperature, Rain, Snow, Precipitation, etc.
- 2. The GPS Decimal Latitude and Longitude Location of each Toronto Fire Services Station
    - The relative distance of each Toronto Fire Services Station to each call may impact operations
    - one can infer if fire stations should be allocated more or less resources

The combination of these 3 datasets will provide us with great insights into the Toronto Fire Services operations and any potential areas of concern / improvement.

## Data Sources:

### A. OPEN DATA TORONTO - [link]()

#### 1. Toronto Fire Services Basic Incident Details - [link](https://open.toronto.ca/dataset/fire-services-basic-incident-details/)
- **DOWNLOAD**:
    - [link](https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/64038657-6437-4a97-b6f7-b4caf135249f)
- **CONTENTS**:
    - 8 (2011 - 2018) dataset .csv files
    - 1 Data_Dictionary metadata .xlsx file
- **NOTE**:
    - this dataset is a slice of a more comprehensive Fire Services Incident Data dataset ([link](https://open.toronto.ca/dataset/fire-services-incident-data/)) however this is now deprecated.

#### 2. Toronto Fire Services Station Locations - [link](https://open.toronto.ca/dataset/fire-station-locations/)
- **DOWNLOAD**:
    - [link](https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/daf5e0ee-cff6-4661-b308-79f95c3881e9)
- **CONTENTS**:
    - WGS84 compatible files
- **NOTE**:
    - [geopandas](https://geopandas.readthedocs.io/en/latest/index.html) Python library will be used to read it in as a DataFrame

### B. Government of Canada - Historical Climate Data - [link](https://climate.weather.gc.ca/)

#### 3. Toronto Weather Stations Historical Weather
- **DOCUMENTATION**:
    - documentation to access data can be found [here](ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt)
    - more resources for data access is found in this `ftp://` [folder](ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/)
    - one can download daily weather data using `wget` module for the years 2010 - 2020
    ```bash
    for year in `seq 2010 2020`;do for month in `seq 1 1`;do wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${STATION_ID}&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ;done;done
    ```
    - STATION_ID can be found in the following [download](ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv)
        - we will be using ```[31688, 48549, 26953]``` STATION_ID's which correspond to:
            - Toronto City Weather Station
            - Toronto City Centre Weather Station
            - Toronto North York Weather Station

## Example DataFrames

<details>
<summary><strong>Click the arrow to see some sample DataFrames</summary></strong>

### 5 rows from the 2011 Toronto Fire Incidents Data (shape=(975175, 15))

|    | Incident Number   | Initial CAD Event Type            | Initial CAD Event Call Type   | Final Incident Type                                                                     |   Event Alarm Level | Call Source                           |   Incident Station Area |   Incident Ward |   LATITUDE |   Longitude | Intersection                       | TFS Alarm Time      | TFS Arrival Time    | Last TFS Unit Clear Time   |   Persons Rescued |
|---:|:------------------|:----------------------------------|:------------------------------|:----------------------------------------------------------------------------------------|--------------------:|:--------------------------------------|------------------------:|----------------:|-----------:|------------:|:-----------------------------------|:--------------------|:--------------------|:---------------------------|------------------:|
|  0 | F11000010         | Medical                           | Medical                       | 89 - Other Medical                                                                      |                   1 | 03 - From Ambulance                   |                     342 |               9 |    43.6791 |    -79.4618 | Silverthorn Ave / Turnberry Ave    | 2011-01-01 00:03:43 | 2011-01-01 00:10:02 | 2011-01-01 00:31:18        |                 0 |
|  1 | F11000011         | Medical                           | Carbon Monoxide               | 89 - Other Medical                                                                      |                   1 | 01 - 911                              |                     131 |              15 |    43.7263 |    -79.3964 | Lawrence Ave E / Mount Pleasant Rd | 2011-01-01 00:03:55 | 2011-01-01 00:09:02 | 2011-01-01 00:15:13        |                 0 |
|  2 | F11000012         | Medical                           | Medical                       | 89 - Other Medical                                                                      |                   1 | 03 - From Ambulance                   |                     324 |              14 |    43.6685 |    -79.3353 | Endean Ave / Jones Ave             | 2011-01-01 00:05:03 | 2011-01-01 00:09:34 | 2011-01-01 00:27:11        |                 0 |
|  3 | F11000013         | FIG - Fire - Grass/Rubbish        | Emergency Fire                | 03 - NO LOSS OUTDOOR fire (exc: Sus.arson,vandal,child playing,recycling or dump fires) |                   1 | 01 - 911                              |                     345 |               9 |    43.6571 |    -79.4343 | Dufferin St / Dufferin Park Ave    | 2011-01-01 00:04:46 | 2011-01-01 00:10:46 | 2011-01-01 00:20:39        |                 0 |
|  4 | F11000014         | FAHR - Alarm Highrise Residential | Emergency Fire                | 33 - Human - Malicious intent, prank                                                    |                   1 | 05 - Telephone from Monitoring Agency |                     142 |               7 |    43.7598 |    -79.5162 | Driftwood Ave / Wilmont Dr         | 2011-01-01 00:06:07 | 2011-01-01 00:11:03 | 2011-01-01 00:21:11        |                 0 |

### 5 rows from Toronto Fire Services Station Locations (shape=(84, 10))

|    | NAME             | ADDRESS             |      X |           Y |   LATITUDE |   LONGITUDE | WARD_NAME                  | MUN_NAME    |    OBJECTID | geometry                                    |
|---:|:-----------------|:--------------------|-------:|------------:|-----------:|------------:|:---------------------------|:------------|------------:|:--------------------------------------------|
|  0 | FIRE STATION 214 | 745 MEADOWVALE RD   | 331856 | 4.8503e+06  |    43.7942 |    -79.1636 | Scarborough East (44)      | Scarborough | 1.56757e+06 | POINT (-79.1636047829337 43.7942193852174)  |
|  1 | FIRE STATION 215 | 5318 LAWRENCE AVE E | 333114 | 4.84844e+06 |    43.7774 |    -79.1481 | Scarborough East (44)      | Scarborough | 2.25000e+06 | POINT (-79.1480690620369 43.777400552994)   |
|  2 | FIRE STATION 221 | 2575 EGLINTON AVE E | 324515 | 4.84368e+06 |    43.7348 |    -79.2551 | Scarborough Southwest (35) | Scarborough | 2.04886e+06 | POINT (-79.25506590336811 43.7347987485643) |
|  3 | FIRE STATION 222 | 755 WARDEN AVE      | 322181 | 4.84207e+06 |    43.7204 |    -79.2841 | Scarborough Southwest (35) | Scarborough | 2.44959e+06 | POINT (-79.28409383366279 43.7204080292081) |
|  4 | FIRE STATION 223 | 116 DORSET RD       | 326275 | 4.84248e+06 |    43.724  |    -79.2333 | Scarborough Southwest (36) | Scarborough | 2.17286e+06 | POINT (-79.2332642694298 43.7239653632118)  |

### 5 rows from Historical Toronto Weather Data (shape=(4018, 11))

|    |   Year |   Month |   Day |   Max Temp (°C) |   Min Temp (°C) |   Mean Temp (°C) |   Heat Deg Days (°C) |   Cool Deg Days (°C) |   Total Rain (mm) |   Total Precip (mm) |   Snow on Grnd (cm) |
|---:|-------:|--------:|------:|----------------:|----------------:|-----------------:|---------------------:|---------------------:|------------------:|--------------------:|--------------------:|
|  0 |   2010 |       1 |     1 |             1.9 |            -9.9 |             -4   |                 22   |                    0 |                 0 |                 1.3 |                   0 |
|  1 |   2010 |       1 |     2 |            -9.7 |           -16.5 |            -13.1 |                 31.1 |                    0 |                 0 |                 0   |                   0 |
|  2 |   2010 |       1 |     3 |            -9.3 |           -14.7 |            -12   |                 30   |                    0 |                 0 |                 2.3 |                   0 |
|  3 |   2010 |       1 |     4 |            -6.7 |           -12   |             -9.4 |                 27.4 |                    0 |                 0 |                 0   |                   0 |
|  4 |   2010 |       1 |     5 |            -3.6 |           -10.4 |             -7   |                 25   |                    0 |                 0 |                 2.9 |                   0 |

</details>