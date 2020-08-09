# Group 10 Summary Paper

## 1. Group Members

- ### A. Nidhi Punja - [Email](npunja@uwaterloo.ca)
- ### B. Judith Roth - [Email](j5roth@uwaterloo.ca)
- ### C. Iman Dordizadeh Basirabad - [Email](idordiza@uwaterloo.ca)
- ### D. Daniel Adam Cebula - [Email](dacebula@uwaterloo.ca)
- ### E. Cynthia Fung - [Email](c27fung@uwaterloo.ca)
- ### F. Ben Klassen - [Email](b6klasse@uwaterloo.ca)
___
## 2. Data Sources

- ### A. Toronto Fire Services Basic Incident Details
  - #### Open Data Toronto - [link](https://open.toronto.ca/) - [webpage](https://open.toronto.ca/dataset/fire-services-basic-incident-details/) - [download link](https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/64038657-6437-4a97-b6f7-b4caf135249f)
    - ##### Description
    Dataset provides information similar to what is sent to the Ontario Fire Marshall relating to incidents to which Toronto Fire Services respond to.  The amount of information is trimmed and includes only Fire incidents as defined by Ontario Fire Marshall.  Covers the year range between 2011 - 2018.

    For privacy purposes personal information is not provided and exact addresses have been aggregated to the nearset major / minor intersection.  Incident exclusion have been made pursuant under Section 8 of Municipal Freedom of Information of Privacy Act (MFIPPA).

    - #### Features
    Data contains the reasons as to the existence of Toronto Fire Serivices (TFS).  Fire, medical and emergency related calls are all indicated here.  As well as the source of the call and other like metrics.  One can determine the main purpose of TFS calls and appropriate resource properly.


- ### B. Toronto Fire Services Station Locations
  - #### Open Data Toronto - [link](https://open.toronto.ca/) - [webpage](https://open.toronto.ca/dataset/fire-station-locations/) - [download link](https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/daf5e0ee-cff6-4661-b308-79f95c3881e9)
    - ##### Description
    The .shp file contains the location of all fire stations and station numbers within the City of Toronto by latitude and longitude (Decimal Degrees).

    - #### Features
    The location of the TFS Fire Stations is important to determine how many calls are taken by each station and if they should be proportioned fewer or more resources as a result.

- ### C. Government of Canada Toronto Historical Climate Weather
  - #### Government of Canada - [link](https://climate.weather.gc.ca/) - [documentation](ftp://client_climate@ftp.tor.ec.gc.ca/Pub/Get_More_Data_Plus_de_donnees/Readme.txt)
    - ##### Description
    Historical Weather, climate, data and related information for numerous locations across Canada.  3 weather stations were found for Toronto city that have climate weather observations from 2010 - 2020.

    The first is located near University of Toronto St. George Campus, the second is located on Toronto Centre Island in Billy Bishop Toronto City Airport and the third is located in North York near York University.

    The weather and climate readings have been aggregated from the 3 locations for the 10 year range.

    - #### Features
    The Toronto Weather and Climate is important to determine how the temperature, precipitation and heating / cooling energy use impacts TFS incidents and if resources should be proportioned in inclimate conditions.
___
## 3. Analysis - [GitHub Repository](https://github.com/cebulada/Data-Science-Group-10)

- ### A. Data Retrieval
  The data is retrieved in the `01-DATA-RETRIEVAL.ipynb` jupyter notebook.  Data is retrieved and stored in folders as multiple data types dynamically when the jupyter notebook cells are executed.

  Downloading and dealing with .csv and .shp files proved to be a challenge.  Data across multiple .csv files are concatenated and transformed into 1 .csv file for a given year range.
  
  Escpecially with the .shp file (geospatial files) some additional steps had to be undertaken.  A conda virtual environment had to be setup to install the geopandas python library due to issues with the Anaconda base environment.  Details of which can be found in `02-GEOPANDAS_AND_MANIPULATIONS.ipynb`.  The data was transformed from a .shp file to a .csv file for compatibility with pandas.

- ### B. Data Munging / Cleaning
  For TFS Fire Incident Data, cleaning done in `02-GEOPANDAS_AND_MANIPULATIONS.ipynb`, several steps were done to clean up the data.

  First, any fire incident data with latitude or longitude values of 0 are replaced with null values (~7% of the data).

  Second, the TFS incident number is set as the index and any duplicated TFS incident numbers were removed (`<0.0005%` of the dataset).  This means each row will have a unique TFS Incident Number.

  Third, there are missing Incident Station Areas (TFS Fire Stations) that was imputed by their distance to the Latitude and Logitude of the call.  The Haversine formula was instrumental in calculating the distance to each TFS Fire Station and returning the smallest distance as the TFS Fire Station Number.

  Fourth, Toronto Weather Climate data was aggregated across 3 weather stations.  Several columns were removed due to an overabundance of nulls, as seen in `01-DATA-RETRIEVAL.ipynb` jupyter notebook.

  Fifth, TFS Fire Locations had the number of the fire station extracted from the name and set as the index.

- ### C. Data Storage

  Due to GitHub file storage concerns, all .csv files were save as .csv.bz2 files using the bz2 compression algorithm available on pandas.  This compresses the size of the data enough to fit in a GitHub repository.

- ### D. Data Merging

  To further conserve space the data is present as 3 different files (`<30MB`) that need to be merged to form the final dataframe (`~200MB`).

- ### D. 
___
## 4. Conclusion

&nbsp;&nbsp;&nbsp;&nbsp; The initial assumption regarding one of the largest organizations providing fire services in Canada, was that majority of calls must be for fires. Surprisingly, the majority of calls to Toronto Fire Services are not for fires. Group 10’s analysis has disproved this initial assumption and revealed other meaningful insights concerning the Toronto Fire Services. As a well-rounded organization providing services for all hazardous emergencies, the majority of their calls are for other medical reasons in which these calls are primarily made by ambulances.

&nbsp;&nbsp;&nbsp;&nbsp; The number of total calls expected in the current month can be predicted using the number of total calls in previous months, allowing the organization to prepare and make better more effective decisions. The analysis concluded that attributes such as time and weather did not impact the calls as believed. Regardless of what time of the year, day of the week, rain, or shine, hot or cold, the Toronto Fire Services get the same amount of calls 365 days a year.
___
## 5. Data Column Details

- ### A. Toronto Fire Services Basic Incident Data Column Details

|    | Column                      | Description                                                                                                                                                                   | Data Source                                                                                            |
|---:|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
|  0 | Incident Number             | TFS incident number                                                                                                                                                           | TFS RMS System                                                                                         |
|  1 | Initial CAD Event Type      | First event type in CAD system of this incident.                                                                                                                              | TFS RMS System                                                                                         |
|    |                             | In situations where the initial CAD event type is medical OR the final incident type is medical, the field is set to medical                                                  |                                                                                                        |
|  2 | Initial CAD Event Call Type | First call type in CAD system of this incident.  Call type is a group of event types.                                                                                         | TFS RMS System                                                                                         |
|    |                             | In situations where the initial CAD event type is medical OR the final incident type is medical, the field is set to medical                                                  |                                                                                                        |
|  3 | Final Incident Type         | Final incident type.                                                                                                                                                          | TFS RMS System                                                                                         |
|    |                             | In situations where the initial CAD event type is medical OR the final incident type is medical, the field is set to medical                                                  |                                                                                                        |
|  4 | Event Alarm Level           | Alarm level of the event                                                                                                                                                      | TFS RMS System                                                                                         |
|  5 | Call Source                 | Source of the call to TFS (e.g., 911 call, Alarm, referal agency, etc.)                                                                                                       | TFS RMS System                                                                                         |
|  6 | Incident Station Area       | TFS Station area where the incident occurred                                                                                                                                  | TFS CAD System                                                                                         |
|  7 | Incident Ward               | Ward where the incident occurred, when available                                                                                                                              | TFS CAD System                                                                                         |
|  8 | LATITUDE                    | Latitude of nearest major or minor intersection in the ward of the incident.                                                                                                  | City Of Toronto Open Data, Intersection File                                                           |
|    |                             | For medical calls this data is not provided.                                                                                                                                  |                                                                                                        |
|  9 | LONGITUDE                   | Longitude of nearest major or minor intersection in the ward of the incident.                                                                                                 | City Of Toronto Open Data, Intersection File                                                           |
|    |                             | In situations where the initial CAD event type is medical OR the final incident type is medical, the field is set to the Forward Sortation Area (FSA) where the event occured |                                                                                                        |
| 10 | Intersection                | Nearest major or minor intersection in the ward where the incident occurred                                                                                                   | City Of Toronto Open Data, Intersection File or Forward Sortation Area Boundary File, Census year 2016 |
| 11 | TFS Alarm Time              | Timestamp of when TFS was notified of the incident                                                                                                                            | TFS RMS System                                                                                         |
| 12 | TFS Arrival Time            | Timestamp of first arriving unit to incident                                                                                                                                  | TFS RMS System                                                                                         |
| 13 | Last TFS Unit Clear Time    | Timestamp of last unit cleared from incident                                                                                                                                  | TFS RMS System                                                                                         |
| 14 | Persons Rescued             | Number of persons rescued                                                                                                                                                     | TFS RMS System                                                                                         |

- ### B. Toronto Fire Services Station Locations Data Column Details

| Column    |                                           Description |
|-----------|------------------------------------------------------:|
| INDEX     |      Toronto Fire Services (TFS) Fire Station Number. |
| NAME      |                                TFS Fire Station Name. |
| ADDRESS   |                             TFS Fire Station Address. |
| LATITUDE  |          TFS Fire Station Latitude (Decimal Degrees). |
| LONGITUDE |         TFS Fire Station Longitude (Decimal Degrees). |
| WARD_NAME | Municipal Ward which the TFS Fire Station belongs to. |
| MUN_NAME  | Municipal Name which the TFS Fire Station belongs to. |

- ### C. Government of Canada Toronto Historical Climate Weather Data Column Details

| Column    |                                                                                                           Description |
|-----------|----------------------------------------------------------------------------------------------------------------------:|
| DATE      |                                                       Date of Toronto Climate Weather Reading (format is YYYY-MM-DD). |
| MAX_TEMP  |                                                               Maximum Temperature recorded for a given day (Celsius). |
| MIN_TEMP  |                                                               Minimum Temperature recorded for a given day (Celsius). |
| MEAN_TEMP |                                                               Average Temperature recorded for a given day (Celsius). |
| HDD       | Heating degree day (HDD) is a measurement used to quantify the demand for energy needed to heat a building (Celsius). |
| CDD       | Cooling degree day (CDD) is a measurement used to quantify the demand for energy needed to cool a building (Celsius). |
| RAIN_MM   |                             Quantity used to measure rainfall where 1 mm indicates 1 Litre of water per square metre. |
| PRECIP_MM |       Quantity used to measure deposition of water in Toronto where 1 mm indicated 1 Litre of water per square metre. |
| SNOW_CM   |                                                             Quantity of snow on the ground in Toronto (Centimetres).  |
___