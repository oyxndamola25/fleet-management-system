# Fleet Management System

By Oyindamola Bade-Ojo  
CSCE 3444 – Software Engineering

This is a solo project to build a basic fleet management system. It tracks vehicle usage, stores the data, and will eventually send maintenance alerts.

## Tech Stack

- RabbitMQ (for message queue)
- Spring Boot (for backend APIs)
- PostgreSQL (for database)
- HTML/CSS with Bootstrap (for dashboard UI)

## Folder Structure

- `backend/` – backend Spring Boot files
- `consumer/` – RabbitMQ listener script
- `frontend/` – basic dashboard UI
- `screenshots/` – UI mockups or preview images

## How to Run

1. Make sure RabbitMQ is running locally
2. Run the consumer script with `python consumer.py`
3. Open `frontend/dashboard.html` in your browser
4. Backend connects to PostgreSQL (you’ll need to configure DB settings in application.properties)

## Sprint Breakdown

**Sprint 1**  
- Set up backend repo and RabbitMQ queue  
- Built the consumer to listen for vehicle usage messages  

**Sprint 2**  
- Connected the consumer to the PostgreSQL database  
- Built REST API endpoints using Spring Boot  
- Created a basic HTML/CSS dashboard template  

**What’s next**  
- Finish the frontend  
- Add logic to trigger maintenance alerts based on data  
