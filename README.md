## Climate Analysis and Exploration

* Used climate_starter.ipynb and hawaii.sqlite(Resources/hawaii.sqlite) files to complete a climate analysis and data exploration.
* Used SQLAlchemy `create_engine` to connect to the sqlite database.
* Used SQLAlchemy `automap_base()` to reflect the tables into classes and save a reference to those classes called `Station` and `Measurement`.
* Linked Python to the database by creating an SQLAlchemy session.

### Precipitation Analysis

* Found the most recent date in the data set.
* Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
* Selected only the `date` and `prcp` values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by `date`.
* Plotted the results using the DataFrame `plot` method.
* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations in the dataset.
* Designed a query to find the most active stations
  * Listed the stations and observation counts in descending order.
  * Found which station id has the highest number of observations.
  * Used the most active station id, calculate the lowest, highest, and average temperature.

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
