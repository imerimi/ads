# Job Seeker App

The Job Seeker app is a Django application designed to display available jobs and provide useful visualizations to help users understand market demand. 

## Features

1. **Login/Logout/Register**: Users can register for an account, log in to access the application's features, and log out when done.
2. **Admin Panel**: Administrators have access to the admin panel to manage users and job listings efficiently.
3. **Load Data from CSV File**: The application supports loading job data from CSV files, providing flexibility in data management.
4. **Job List Page**: Users can view a list of available jobs with details such as job title, company, location, and date posted.
5. **Dashboard Page**: The dashboard page provides users with visualizations and insights into market demand, helping them understand trends and make informed decisions.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Data Scraping

The `jobscrape.ipynb` file contains the Python notebook used to scrape job data from Jobstreet. This notebook utilizes various web scraping techniques to extract job listings and relevant information from the Jobstreet website and store it into 'job.csv' file

## Future Enhancements

1. **Enhanced Job Data**: Add additional data such as job level, years of experience, and desired skills to provide users with more useful information.
2. **Salary Suggestion**: Utilize data on years of experience, desired skills, and location to suggest salary ranges for job listings, helping users negotiate salaries effectively.
3. **Recommendations**: Provide recommendations for high-salary locations and top skills to learn based on market demand and trends, helping users make strategic career decisions.


