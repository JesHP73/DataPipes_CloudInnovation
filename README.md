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
Just as treasure hunters of old scoured maps and delved into unknown terrains, modern data engineers navigate the vast expanse of the internet. Armed with Python's beautifulsoup library, they extract valuable data hidden within website codes. It's like uncovering hidden gems embedded in the vast digital landscape. Some of the data you will need is going to be floating around the internet, as the content of websites. You will have to learn how to access this information by downloading and extracting the HTML code of these sites, mostly using Python’s most popular web scraping library: beautifulsoup.


