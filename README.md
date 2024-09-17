Political Stars Scraper: A Dive into Celebrities in Indian Politics

1. Project Overview

This project is all about uncovering the fascinating world of Indian actors turned politicians. Using web scraping techniques, we extract a list of well-known Bollywood stars who have made the leap into politics and provide details about their political journeys. Our scraper pulls this data from a Times of India article that highlights prominent actors who have entered the 2024 Indian Lok Sabha elections.

2. Why This Website?

We chose this specific page from Times of India because it offers a rich and timely dataset that isn’t readily available through any public API. In India, celebrity influence in politics is significant—actors like Amitabh Bachchan and Sunny Deol have immense public followings, and their political affiliations could sway elections. This list brings together some of the biggest names in Bollywood who have embraced political life. The page organizes these actors in a way that’s perfect for scraping, with their names in h2 tags and descriptions in p tags.

Plus, the idea of merging two big Indian obsessions—movies and politics—makes this data feature especially intriguing. Who wouldn’t want to know more about their favorite actor’s political career?

3. The Data Feature

This scraper does more than just grab names. It helps you quickly access key details about the actors’ political roles and backgrounds. It’s like a mini celebrity dossier for those keeping track of the upcoming elections, providing instant access to essential info without the need to manually sift through articles.

Who might use this?

1-Journalists covering the 2024 elections and looking for quick insights into celebrity candidates.
2-Researchers studying the impact of celebrities in Indian politics.
3-Curious fans who want to know which stars are on the ballot.

4. Running the Scraper: Step-by-Step Guide

Step 1: Clone the Repository
Start by downloading the code from the repository:

git clone <repository-url>
cd <repository-directory>

Step 2: Set Up the Virtual Environment

To avoid conflicts with your system’s Python packages, create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  

Step 3: Install the Required Libraries

All the dependencies for this project are listed in the requirements.txt file. Install them with:

pip install -r requirements.txt

Step 4: Run the Script

Once you’ve set everything up, you can run the scraper and start interacting with the data:

python main.py

The script will print out a list of actors who have joined politics. You can then select an actor by entering their corresponding number, and the scraper will provide details about their political career.

5. Project Structure

The project is organized into several key files:


PoliticalStarsScraper/

  main.py               
  requirements.txt       
  README.md              
  ETHICS.md              
  .gitignore             

main.py: This is where all the magic happens. It contains the code for fetching and parsing the actor data from the Times of India article.

requirements.txt: This file includes the libraries you’ll need to install (requests, beautifulsoup4).

README.md: The documentation that explains the project and how to run it.

ETHICS.md: A document that lays out the ethical considerations behind the scraping process.

.gitignore: Ensures files like the virtual environment don’t get committed to Git.