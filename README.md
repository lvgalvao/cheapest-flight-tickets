# The cheapest flights tickets - Save up to 60% on airline  tickets.

As a summary, I built an ETL process to get information about flights and then generate user insights and alarms.

I used Spark to run the data modeling process, postgreSQL to orchestrate the custom data, a web application to design (file) and Airflow for table with final fluiph.js.

<p align="center">
<img src="https://github.com/lvgalvao/cheapest-flight-tickets/blob/main/docs/cheapest-flight-tickets.png?raw=true" alt="flowchart" width="80%">
<p>

## Functions

- Integrate with Google Sheet to personalize your search (e.g. to looking for cities that you want to go to)
- Use the Flight Search API to check for the cheapest flights integrating hundreds of airlines companies
- Send SMS with the best tickets using Twillio API
