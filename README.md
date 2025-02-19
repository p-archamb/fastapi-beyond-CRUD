**FastAPI Beyond CRUD**

This repository extends the original FastAPI CRUD example with CI/CD features including conventional commits enforcement, nightly builds, and automated notifications.

**Features**

Original Features:

-Complete CRUD operations with FastAPI  
-SQLAlchemy integration with PostgreSQL  
-Redis for task queuing and caching  
-Celery for background tasks  
-Email notifications using Ethereal Email  

**Added CI/CD Features**

-Conventional Commits enforcement on PRs  
-Nightly builds with container publishing  
-Automated email notifications for CI/CD events  
-Docker containerization  
-GitHub Container Registry integration  

**Prerequisites**

-Docker and Docker Compose  
-GitHub account with Actions enabled  
-Ethereal Email account for notifications  
-Python 3.11+  
-PostgreSQL  
-Redis  
# sjlie
**Setup Instructions**

1. Clone:

`git clone https://github.com/p-archamb/fastapi-beyond-CRUD` 

`cd fastapi-beyond-crud`

2. Create .env file:

`cp .env.example .env`

3. Run the Application:

`docker compose up`

**CI/CD Workflows**
Conventional Commits

All commits must follow the format: type: description  
Allowed types: feat, fix, docs, style, refactor, perf, test, build, ci, chore  
PRs with non-compliant commits will be automatically closed  
Email notifications sent on failures

Nightly Builds

-Runs daily at 0:00 AM Pacific Time  
-Executes all tests  
-Builds Docker container  
-Pushes to GitHub Container Registry  
-Sends notifications on failures  

**API Documentation**

Swagger UI: http://localhost:8000/api/v1/docs
ReDoc: http://localhost:8000/api/v1/redoc


**Making Contributions**

-Create a new branch  
-Make changes  
-Commit using conventional format:  
-git commit -m "type: description"  
-Create Pull Request  
-Wait for automated checks  
