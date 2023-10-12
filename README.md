# Behind the Scenes: Data Pipelines and Cloud Innovation 

-- INTRODUCTION AND MY THOUGHTS GOES HERE --

## E-Scooter GANS - Case Study, Data Engineer Role

**Context**:I have been hired by Gans, an e-scooter-sharing startup aspiring to operate in 5 of the major cities of Germany. The challenge faced by such
companies isn't just sustainability but also ensuring scooters are available where users need them.

**Problem**: Scooter movement isn't always symmetrical due to various reasons like terrain, weather, and user demographics. While the eco-friendly
narrative is a significant selling point, Gans identified a more pressing operational challenge: **ensuring scooters are conveniently available for
users**. It's like setting up a coffee shop: it's not just about brewing the best coffee but also about being where coffee lovers are.In an ideal world,
for every user that takes a scooter **from point A to B**, another user brings it back. But real-world scenarios paint a different picture:

1. The Terrain Factor: In cities with hills, riders prefer scooters for uphill journeys and choose to walk downhill.
2. The Daily Commute: Mornings see a rush from residential areas to city centers.
3. Weather Woes: A sudden downpour can drastically reduce e-scooter usage.
4. Tourist Patterns: Tourists, especially the younger demographic, prefer scooters available near landmarks or downtown.

**Solving the Puzzle: Beyond Predictive Modelling**

While predictive modeling is the end goal 🏃🏽‍♀️, the first step is data collection, transformation, and storage. the immediate solution lies in:

1. Physical Rearrangement: Deploying trucks to move scooters to high-demand areas.
2. Economic Incentives: Encouraging users to pick or drop scooters at specific locations through financial perks.

⚠️ **However**, to implement these strategies effectively, a critical ingredient is needed: **data, data, data**.

**So, my Role consist in**: Collecting data from external sources that can help Gans predict e-scooter movement and assemble and automate a data pipeline
in the cloud. This involves:

1. **Data Collection:** Using tools like web scraping and APIs to gather data.
2. **Data Cleaning:** Ensuring the data is relevant and error-free.
3. **Data Storage:** Organizing the data in a manner that's easily accessible and usable.
4. **Data authomatization:** a cloud database with real time updates.
5. **Data ready for:** the data analyst department to work with!

## The Process: Breaking Down the Data Pipeline
Creating a data pipeline is like setting up a sophisticated railway system. Trains (data) must run smoothly, arrive on time, and ensure passengers (users)
are satisfied. 

Here's a step-by-step breakdown:

#### Phase 1: The Local Pipeline

Imagine you're assembling a toy train set in your living room. Before setting it out in the vast outdoors, you'd first test it in a controlled environment
to ensure everything works smoothly. Similarly, before deploying a data pipeline in the expansive digital cloud, it's prudent to first set it up locally
on your computer.

**1.1 Web Scraping: The Treasure Hunt**
Just as treasure hunters of with old maps and delved into unknown terrains, modern data engineers navigate the vast expanse of the internet (if the
information in legaly disclose). With **Python's beautifulsoup library**, extracting valuable data hidden within website codes. It's like uncovering
hidden gems embedded in the digital landscape. Some of the data I will need is going to be floating around the internet, as the content of websites,
this information by downloading and **extracting the HTML code of these sites**.

**1.2 APIs: or as I call them, the love language of the internet**
Imagine knocking on the doors of various data houses and politely asking for information. APIs serve as these doorbells, allowing seamless interaction and
data exchange. With **Python's requests library**, interacting with these APIs becomes as easy as ringing a doorbell and acquire the specific data I need.
Assemblying a request with the right parameters is key! Each Api might have its own language or better, some of them are already in the programing
language of a data engineer dayly live. 

For this project, I used the following API's for the collection of data, that will allow GANS to solve the puzzel:

 - **Cities table:** the main German cities they want to work with; I started doing web scraping on wikipedia to retrive information sunch as Latitud and
Longitud, and population density, And to be honest, Wikipedia is land of no one, so web scraping became extremetly unreliable, thas when, I decided to
use an API called 🔗 https://api.api-ninjas.com/v1/city for this table.
 - **Weather table:** to gather the upto date information of the weather conditions in the cities I am gathering information, I used
🔗 https://openweathermap.org
 - **Airports & Arrival flights table:** As part of GANS strategy to have e-scooters available also for tourist in this cities, I collected the airports
Icao's ID that are the main ones for the cities of analysis, and that will help me to search for realtime information of arrival flights; I used
🔗 https://aerodatabox.com 


**1.3 Database Modeling: The Blueprint Creation**

Before constructing a building, architects draft a blueprint. Similarly, before storing data, a logical structure or model for the database is essential.
It involves determining the tables, their relationships, and the best way to organize data. This foundational step ensures data is stored efficiently and
can be accessed swiftly by the Data Analyst, data stored as dictionaries or **Pandas DataFrames**. Python objects are great for local exploration and analysis, ⚠️ but not the best format to make data quickly available. 

Here is where, **Relational databases** are the solution. Determining the logical structure of the database is an important first step when a company
wants to start storing data. Which tables will be need it? How will these tables be related to each other?, what 'datatypes' would I need the information
in? Only after answering these questions (and more), would be the moment to start actually creating!; I know I want to test and deploy my tables 1st locally, and the best tool (for me) is MySQL, so for this step, before creating anything, I used 🔗 https://app.sqldbm.com/MySQL to be able to visualize this reationship. 

-- INSERT HERE SCREENSHOOT OF THE DESIGNED TABLES --

**1.4 Local Storage: Testing the Waters**

Once the blueprint is ready, it's time to test the waters. By setting up a **MySQL instance locally**, I would be able to ensure that the data from the
APIs and web scraping endeavors is stored correctly. It's a way to test-driving a car before hitting the main road. Once I havve created the **database
model**, testing that the connection **between Python and MySQL** works by setting up the database locally on my computer and storing the data I
collected from the APIs.


































