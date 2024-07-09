# Django Blog Project

This project is a Django-based blog application designed to manage posts, categories, tags, user profiles, and authentication using JWT tokens.


## Project Overview

The project consists of several Django apps:

- **categories**: Manages blog post categories.
- **posts**: Handles blog posts, comments, and related functionalities.
- **profiles**: Manages user profiles.
- **tags**: Manages tags associated with blog posts.
- **users_auth**: Handles user authentication and registration.

Each app includes models, serializers, views, URLs, and tests to manage its functionalities.

## Features

- User authentication using JWT tokens.
- CRUD operations for blog posts, comments, categories, tags, and user profiles.
- RESTful API endpoints for interacting with blog content.
- Dockerized setup for deployment.
- CI/CD pipeline using GitHub Actions for automated testing and deployment.
- Swagger API Documentation.

## Setup Instructions

### Local Development Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <project_directory>

2. **Docker:**
    ```bash
    docker-compose up --build

## Deployment 
This project is deployed on aws ec2 instance containerized by docker and automated by 
github ci/cd pipeline

link: http://16.171.24.21/swagger/

Admin Auth:
Username: admin
password: admin
