import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
app = Flask(__name__)

#################################################
# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start<br/>"
        "/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    """Return a list of 12 months of Precipitation"""
    # Query precipitation data
    results = session.query(measurement.station,measurement.date,measurement.prcp).filter(measurement.date>year_ago).all()

    session.close()

    # Create a dictionary from the row data and append to precipitation data
    all_prcp = []
    for station, date, prcp in results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["prcp"] = prcp
        prcp_dict["station"] = station
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of station names"""
    # Query stations
    station_results = session.query(measurement.station).distinct().all()

    session.close()

    # Convert list of tuples into normal list for all stations
    all_stations = list(np.ravel(station_results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    """Return a list of 12 months of Temperature for Most Active Station"""
    # Query precipitation data
    temps = session.query(measurement.station,measurement.date,measurement.tobs).filter(measurement.date>year_ago).filter(measurement.station=='USC00519281').all()

    session.close()
    # Create a dictionary from the row data and append to temp data
    all_temps = []
    for station, date, tobs in temps:
        temp_dict = {}
        temp_dict["Date"] = date
        temp_dict["tobs"] = tobs
        temp_dict["station"] = station
        all_temps.append(temp_dict)

    return jsonify(all_temps)

@app.route("/api/v1.0/<start>")
def summary(start):
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query temp data for min, max and avg for start date
    start_summary = session.query(measurement.station,func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date>=start).all()   
    session.close()
    
    return jsonify(temps = list(np.ravel(start_summary)))
     
@app.route("/api/v1.0/<start>/<end>")
def summary_range(start,end):
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query temp data for min, max and avg for start date to end date
    end_summary = session.query(measurement.station,func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date.between(start, end)).all()     
    session.close()
    
     # Create a dictionary for temp data for min, max and avg for start date to end date
    all_summary = []
    for station, min_tobs, max_tobs, avg_tobs in end_summary:
        sum_dict = {}
        sum_dict["Max Temp"] = max_tobs
        sum_dict["Min Temp"] = min_tobs
        sum_dict["Avg Temp"] = avg_tobs
        sum_dict["Station"] = station
        all_summary.append(sum_dict)

    return jsonify(all_summary)
        
if __name__ == "__main__":
    app.run(debug=True)
