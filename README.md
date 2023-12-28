# Reddit Scraper

## Overview

A simple Python script for scraping post information and comments from a specified subreddit using the Reddit API. This script utilizes the PRAW (Python Reddit API Wrapper) library to interact with the Reddit API and fetch data in a structured manner.

## Features

- Fetches post details such as title, author, score, and URL.
- Retrieves comments for each post, including author and comment body.
- Handles posts with zero comments gracefully.
- Writes scraped data to a text file for easy reference.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/coder-es/reddit-post-scraper.git
    ```

2. Install the required dependencies:

    ```bash
    pip install praw
    ```

3. Set up your Reddit API credentials in the script (`client_id`, `client_secret`, `user_agent`).

4. Run the script:

    ```bash
    py bot.py
    ```

5. View the scraped data in the generated text file.

## Configuration

Modify the following variables
