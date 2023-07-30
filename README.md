# JobVantage - Recruitment Platform

JobVantage is a cutting-edge recruitment platform built using Django REST Framework that connects companies with top talent globally. This README provides a detailed overview of the functionalities implemented in the project, enabling you to understand and utilize the platform effectively.

## Features

### User Authentication

Companies can securely sign in to manage their accounts.

Password recovery and account deletion options are available for enhanced security.

### Job Posting and Management

Companies can create job listings with details such as role, requirements, and location.

Job postings can be easily edited or deleted as needed.

### Candidate Database and Search

The platform stores candidate profiles with relevant information like skills and experience.

Companies can search for candidates based on specific criteria.

### Internship Listing

Companies can also post internships, including descriptions, requirements, and duration.

Internship postings can be managed through the platform.

### Course Enrollment

Users can discover and enroll in various skill-enhancing courses.

Courses are listed with detailed descriptions and durations.

### Filtering and Search

Jobs and internships can be filtered based on location, job type, and more.

Search functionality allows finding specific opportunities by title.

### Discounts and Coupons

Courses support discount options, and companies can offer coupons for enrollment.

### Bookmark Feature

Users can bookmark jobs and internships for later reference.

## How to Use JobVantage
### Installation

Clone the repository from GitHub: git clone https://github.com/shrey1010/JobVantage.git

Navigate to the project directory: cd JobVantage

Install the required dependencies: pip install -r requirements.txt

Apply migrations: python manage.py makemigrations and python manage.py migrate

Create a superuser: python manage.py createsuperuser

Running the Server

Start the development server: python manage.py runserver

Access the platform locally at http://localhost:8000/

### API Endpoints

User Registration: /api/users/ (POST)

Job List and Create: /api/jobs/ (GET, POST)

Job Detail, Update, and Delete: /api/jobs/<job_id>/ (GET, PUT, DELETE)

Internship List and Create: /api/internships/ (GET, POST)

Internship Detail, Update, and Delete: /api/internships/<internship_id>/ (GET, PUT, DELETE)

Course List and Create: /api/courses/ (GET, POST)

Course Detail, Update, and Delete: /api/courses/<course_id>/ (GET, PUT, DELETE)

Coupon List and Create: /api/coupons/ (GET, POST)

Coupon Detail, Update, and Delete: /api/coupons/<coupon_id>/ (GET, PUT, DELETE)

Bookmark List and Create: /api/bookmarks/ (GET, POST)

Bookmark Detail and Delete: /api/bookmarks/<bookmark_id>/ (GET, DELETE)

## Contributing
We welcome contributions to JobVantage! If you find a bug or want to add new features, please feel free to fork the repository and submit a pull request.
