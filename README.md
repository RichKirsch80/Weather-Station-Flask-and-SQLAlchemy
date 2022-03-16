Goals - Weather Station Analysis answers the question, when is the best time to vacation in Hawaii with optimal weather. Observes weather station data for precipitation, date, minimum temperature, maximum temperature and average temperature.  


## Climate Analysis and Exploration

* Used climate_starter.ipynb and hawaii.sqlite(Resources/hawaii.sqlite) files to complete a climate analysis and data exploration.
* Used SQLAlchemy `create_engine` to connect to the sqlite database.
* Used SQLAlchemy `automap_base()` to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Linked Python to the database by creating an SQLAlchemy session.

![image](https://user-images.githubusercontent.com/85321602/158704088-a7f27bac-4469-4bb0-903b-64dcfa8913a7.png)

### Precipitation Analysis

* Found the most recent date in the data set.
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
* Selected only the `date` and `prcp` values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by `date`.

![image](https://user-images.githubusercontent.com/85321602/158704382-183dfdd0-83cc-4250-9e22-9e7ba06fde48.png)

* Plotted the results using the DataFrame `plot` method.
* Used Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/85321602/158704713-98d93b5d-72db-4608-bf9f-6fe3344fbbf7.png)

### Station Analysis

* Designed a query to calculate the total number of stations in the dataset.

![image](https://user-images.githubusercontent.com/85321602/158704909-19239095-4670-42b1-a67e-17aa9393fc9d.png)


* Designed a query to find the most active stations
* Listed the stations and observation counts in descending order.
* 
![image](https://user-images.githubusercontent.com/85321602/158704961-1ff2461f-803d-42e0-a54a-1b82c5ea373e.png)

  
* Found which station id has the highest number of observations.
* Used the most active station id, calculate the lowest, highest, and average temperature.
  
![image](https://user-images.githubusercontent.com/85321602/158704976-dcfa317c-3551-4136-9f5f-0ac9930cb68f.png)

  

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filtered by the station with the highest number of observations.
  * Queried the last 12 months of temperature observation data for this station.
  * Plotted the results as a histogram with `bins=12`.

## Step 2 - Climate App

Designed a Flask API based on the queries that were just developed.
* Use Flask to create routes.

### Routes

* `/`
  * Home page.
  * Listed all routes that are available.

* `/api/v1.0/precipitation`
  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Returned the JSON representation of your dictionary.

* `/api/v1.0/stations`
  * Returned a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queried the dates and temperature observations of the most active station for the last year of data.
  * Returned a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
