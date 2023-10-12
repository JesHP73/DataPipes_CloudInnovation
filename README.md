# Behind the Scenes: Data Pipelines and Cloud Innovation 

![Alt text](Images_folder/header.jpg)

## E-Scooter GANS - 📌Case Study, Data Engineer Role

✓ **Context**: Imagine, I have been "hired" by Gans, an e-scooter startup aspiring to operate in 5 of the major cities of Germany. 
The challenge faced by such companies isn't just sustainability but also ensuring scooters are available where users need them.

✓ **Problem**: Scooter movement isn't always symmetrical and while the eco-friendly narrative is a significant selling point, Gans identified 
a more pressing operational challenge: **ensuring scooters are conveniently available for users**. It's like setting up a coffee shop ☕️:
it's not just about brewing the best coffee but also about being where coffee lovers are. 
In an ideal world, for every user that takes a scooter **from point A to B**, another user brings it back. But real-world scenarios paint a
different picture:

- 🌍 In cities with hills, riders prefer scooters for uphill journeys and choose to walk downhill.
- 🚘 The Daily Commute: Mornings see a rush from residential areas to city centers.
- 🌦️ Weather: A sudden downpour can drastically reduce e-scooter usage.
- 💃🏽 Tourist Patterns: Tourists, especially the younger demographic, prefer scooters available near landmarks or downtown.

✓ **Solving the Puzzle: Beyond Predictive Modelling**

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

### Phase 1: The Local Pipeline

Imagine you're assembling a toy train set in your living room. Before setting it out in the vast outdoors, you'd first test it in a controlled environment
to ensure everything works smoothly. Similarly, before deploying a data pipeline in the expansive digital cloud, it's prudent to first set it up locally
on your computer.

#### 1.1 Web Scraping: The Treasure Hunt
Just as treasure hunters of with old maps and delved into unknown terrains, modern data engineers navigate the vast expanse of the internet (if the
information in legaly disclose). With **Python's beautifulsoup library**, extracting valuable data hidden within website codes. It's like uncovering
hidden gems embedded in the digital landscape. Some of the data I will need is going to be floating around the internet, as the content of websites,
this information by downloading and **extracting the HTML code of these sites**.

#### 1.2 APIs: or as I call them, the love language of the internet
Imagine knocking on the doors of various data houses and politely asking for information. APIs serve as these doorbells, allowing seamless interaction and
data exchange. With **Python's requests library**, interacting with these APIs becomes as easy as ringing a doorbell and acquire the specific data I need.
Assemblying a request with the right parameters is key! Each Api might have its own language or better, some of them are already in the programing
language of a data engineer dayly live. 

For this project, I used the following API's for the collection of data, that will allow GANS to solve the puzzel:

 - 🌍 **Cities table:** the main German cities they want to work with; I started doing web scraping on wikipedia to retrive information sunch as Latitud
   and Longitud, and population density, And to be honest, Wikipedia is land of no one, so web scraping became extremetly unreliable, thas when, I
   decided to use an API called 🔗 https://api.api-ninjas.com/v1/city for this table.
 - ☀️ **Weather table:** to gather the upto date information of the weather conditions in the cities I am gathering information, I used
🔗 https://openweathermap.org
 - 🛬 **Airports & Arrival flights table:** As part of GANS strategy to have e-scooters available also for tourist in this cities, I collected the
   airports Icao's ID that are the main ones for the cities of analysis, and that will help me to search for realtime information of arrival flights; I
   used 🔗 https://aerodatabox.com 


#### 1.3 Database Modeling: The Blueprint Creation
Before constructing a building, architects draft a blueprint. Similarly, before storing data, a logical structure or model for the database is essential.
It involves determining the tables, their relationships, and the best way to organize data. This foundational step ensures data is stored efficiently and
can be accessed swiftly by the Data Analyst, data stored as dictionaries or **Pandas DataFrames**. Python objects are great for local exploration and
analysis, ⚠️ but not the best format to make data quickly available. 

Here is where, **Relational databases** are the solution. Determining the logical structure of the database is an important first step when a company
wants to start storing data. Which tables will be need it? How will these tables be related to each other?, what 'datatypes' would I need the information
in? Only after answering these questions (and more), would be the moment to start actually creating!; I know I want to test and deploy my tables 1st
locally, and the best tool (for me) is MySQL, so for this step, before creating anything, I used 🔗 https://app.sqldbm.com/MySQL to be able to visualize
this reationship. 

![Alt text](Images_folder/1.3_Database_Modeling_TheBlueprintCreation.jpg)

#### 1.4 Local Storage: Testing the Waters
Once the blueprint is ready, it's time to test the waters. By setting up a **MySQL instance locally**, I would be able to ensure that the data from the
APIs and web scraping endeavors is stored correctly. It's a way to test-driving a car before hitting the main road. Once I havve created the **database
model**, testing that the connection **between Python and MySQL** works by setting up the database locally on my computer and storing the data I
collected from the APIs.

![Alt text](Images_folder/1.4_LocalStorage_TestingTheWaters.jpg)


### Phase 2: Cloud Pipeline

Now, imagine wanting to share a toy train set with the world. You'd move it from your living room to a park, where everyone can see and appreciate it.
Similarly, once the local pipeline is set, it's time to move it to the cloud, making it accessible and scalable. If you use Google Drive or Apple’s
iCloud, your files are already on the cloud. **The cloud is a catch-all name for any technological resources or services accessed via the internet**. And
it has many advantages when it comes to building data pipelines: scalability, flexibility, automation, maintenance… where in the old days (Im not saying
its extint), I remember this room, full of computers and cables, that requaiers big initial investment and maintenance. One can choose its poison, I
choose the cloud. 

#### 2.1. Cloud Database conected to mySQL
Using **RDS from Amazon Web Services (AWS)**, the biggest public cloud provider, one can set up a **MySQL database in the cloud**. It's like moving your
treasured book collection from a local shelf to a grand library where many can access it. 

![Alt text](Images_folder/2.1_CloudDatabase_conectedTo_mySQL.jpg)

#### 2.2 Lambda: The Cloud's Command Center 🫡
Moving scripts to Lambda is like shifting from using personal diaries to collaborative online platforms. **AWS Lambda** allows code to run seamlessly in
the cloud, ensuring data collection happens and its actually been transfered to the created data base. I moved my data collection scripts from **Jupyter
Notebook** into a AWS Lambda functions by copying and pasting my local database scrip in an estructured way. 

![Alt text](Images_folder/2.2_LambdaTheCloud_Command_Center.jpg)


#### 2.3 Automation: The Digital Clockwork
Here is where the magic ⚡️ happens, one of the cloud's biggest perks is automation. Using **AWS's CloudWatch Events or EventBridge**, one can set rules,
much like setting alarms on a clock. When the conditions are met, the data collection scripts are triggered, ensuring timely, relevant and efficient data
gathering.

![Alt text](Images_folder/2.3_AutomationTheDigitalClockwork.jpg)

⚠️ Once completed, the pipeline should resemble the flowchart below, and everything should be ready for the Data Analysis department to take over 🤸🏽

#### Disclaimer ❗️
Data pipelines can get more complex than this. So, I want to make sure to level expectations:
•	I will not connect our data pipeline to a BI tool.
•	I will not be creating either a data warehouse or a data lake.
•	Iwill not work with big data, data streaming or parallel computing.
This is just a "newbi" start with a simple approach, before moving on to cool (but oftentimes, complicated) solutions.

## In a nutshell 💁🏽‍♀️

It might seem simple from the outside, I was just getting data from one place to another, but if you (the reader) have struggled to follow the whole process, you might understand by now,how complex data pipelines can become! and to summarized it all:

 - Collected data from the internet by writing a web scraping script using **Python’s library beautifulsoup.**
 - Collected **data from the internet through APIs**, either using a **Python wrapper such as spotipy or pyowm**, or assembling the call directly with the
   **requests library**.
 - Navigated **JSON files** and find the information I need it.
 - Cleaned data using either **Python’s string operations, str methods from the Pandas library or regex.**
 - Writed **for loops and list comprehensions** on Python to perform tasks iteratively.
 - Structured **Python code as functions**.
 - Setted up a **local MySQL database.**
 - Created an **SQL data model**, crafting the relationships between tables.
 - Created MySQL tables with the **appropriate data types, constraints and keys.**
 - Setted up an **RDS instance** on AWS and enable the connection between my computer and the cloud instance, both through a standard client such as
   MySQL Workbench and through Python, by using **MySQL-python-connector.** 🔌
 - **Populated your MySQL tables** with collected data through INSERT queries executed from a Python script.
 - Setted up **Lambda functions** to run my code in the cloud (using a serverless service).
 - Created **custom Layers** with ad-hoc dependencies for the Lambda functions.
 - Scheduled the Lambda functions **to run on a specified schedule.**


## But, you might wonder, Is that all?

And the answer is yes!, Data engineers work is, in my opinion, the backbone for data analisys. This project Meant, moving data pipelines from local to
the cloud!!!! Think of it as an astronomer extending their study from Earth to the vastness of space, if you will. My scripts, initially run on local
machines and now, founded a new home in AWS Lambda, ensuring relevant and up to date data collection. While developing this project, I realized that I had applyed **The Five Pillars of a Data Analyst too** that played a pivotal role:

 - **1▸ Curiosity:** The quest to understand e-scooter movements, much like a scientist's thirst for answers, drove this project.
 - **2▸ Understanding the Context:** Analyzing data without context is like reading a book in an unknown language. Recognizing patterns in scooter
   movements required a deep understanding of the urban landscape.
 - **3▸ Technical Mindset:** Breaking down the challenge into smaller, manageable tasks was crucial. It's the art of seeing the bigger picture
   and understanding the minute brushstrokes that create it.
 - **4▸ Data Design:** Imagine a librarian arranging books, ensuring that readers find what they're looking for without hassles.
 - **5▸ Data Strategy:** Managing the tools, processes, and the team inpputs need it, as if conducting an orchestra, ensuring each instrument
   plays its part.

# Conclusion
The Gans e-scooter project was not just about predicting scooter movements; it was a deep dive into the world of data engineering. It reaffirmed the
importance of understanding the data ecosystem, the need for robust pipelines, and the foundational analytical skills that guide such projects. As we
move ahead in this data-driven era, these lessons will be the lights to my path; As the very wise Data Scientist, Soner Yıldırım, wrote **"Data
Scientists Without Data Engineering Skills Will Face the Harsh Truth"** *(I really encourague to read his article on MEDIUM)*









































