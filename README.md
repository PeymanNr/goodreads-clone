
# BookReview API

This project is a backend API designed for a simple book review website, similar to a simplified version of GoodReads. Users can rate and review books they've read, and bookmark books they want to read later.

## Features

- **User Management:**
  - Users can register and log in using their email and password.
- **Admin Capabilities:**
  - Admin users can create, edit, and delete books.
- **Book Management:**
  - Users can view a list of available books.
  - Users can view detailed information about each book.
  - Users can bookmark books they are interested in reading.
  - Users can rate and review books they have read.
  
## API Endpoints

### User Registration/Login
- **POST /api/authenticate**
  - Allows users to register or log in using their email and password.

### Get List of Books
- **GET /api/books**
  - Returns a list of books with the following details:
    - Book ID or link to the book details API
    - Book title
    - Number of users who have bookmarked the book
    - Bookmark status (if the user is logged in)

### Get Book Details
- **GET /api/books/{id}**
  - Returns detailed information about a specific book, including:
    - Title
    - Summary
    - Number of reviews
    - Number of ratings
    - Average user rating
    - Breakdown of user ratings (e.g., how many users rated it 1, 2, etc.)
    - List of reviews and ratings submitted by users

### Bookmark a Book
- **POST /api/books/{id}/bookmark**
  - Allows a user to bookmark or unbookmark a book. Users can only bookmark books they haven't rated or reviewed yet.

### Submit a Rating/Review
- **POST /api/books/{id}/rate**
  - Allows users to submit a rating and/or review for a book. If the user has previously submitted a rating or review, it will be updated.

### Admin: Create/Update/Delete Books
- **POST /api/admin/books**
  - Allows admins to create new books.
- **PUT /api/admin/books/{id}**
  - Allows admins to update book information.
- **DELETE /api/admin/books/{id}**
  - Allows admins to delete books.

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/PeymanNr/goodreads-clone
   cd bookreview-api
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Set up environment variables:
   \`\`\`bash
   cp .env.example .env
   \`\`\`
   Update the `.env` file with your environment-specific variables.

4. Apply database migrations:
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. Run the development server:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Running with Docker

If you prefer to run the project using Docker, follow these steps:

1. Build the Docker image:
   \`\`\`bash
   docker build -t bookreview-api .
   \`\`\`

2. Run the Docker container:
   \`\`\`bash
   docker run -p 8000:8000 bookreview-api
   \`\`\`

## Testing

To run tests, use the following command:

\`\`\`bash
python manage.py test
\`\`\`

## API Documentation

API documentation can be accessed via Postman or by viewing the Swagger/OpenAPI output.

## Additional Notes

- This project includes fixtures for initial data setup.
- The code is designed with clean and readable standards.
- The project structure is Dockerized for easy deployment.
