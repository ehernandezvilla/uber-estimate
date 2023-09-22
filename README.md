# Uber Price Estimation Project (Is possible than the API library is not longer working - deprecated)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [References](#references)

## Introduction
This project aims to estimate Uber prices using Uber's API and store the data in a MySQL database. The code fetches price estimates for a specific route and stores various metrics like distance, duration, low and high estimates, and more into a MySQL database.

## Installation

### Requirements
- Python 3.x
- MySQL
- Uber API Token

### Steps
1. Clone the repository
    ```bash
    git clone https://github.com/your-repo/uber-estimate.git
    ```
2. Install the required Python packages
    ```bash
    pip install -r requirements.txt
    ```
3. Set up MySQL database and replace the credentials in the code.

## Usage
Run the main script to start fetching and storing Uber price estimates.
```bash
python main.py
```

## Code Structure

- main.py: The main script that runs the price estimation and database storage.
- config.py: Contains configuration variables like MySQL credentials and Uber API token.

### Functions

- get_uber_estimate(): Fetches the Uber price estimates
- convert_to_dataframe(): Converts the JSON response to a Pandas DataFrame.
- calculate_metrics(): Calculates various metrics like average price, duration, etc.
- insert_into_db(): Inserts the calculated metrics into the MySQL database.

### References 

- Coordenadas GPS: https://www.coordenadas-gps.com/
- Uber API Documentation: https://developer.uber.com/docs/riders/ride-requests/tutorials/api/python
