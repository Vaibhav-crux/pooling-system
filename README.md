# Polling System Backend

This project provides a backend system for a polling application that supports high-concurrency polling features using Kafka and Zookeeper. The system allows multiple users to interact with polls simultaneously, ensures resilience in case of failures, and includes real-time poll updates using WebSockets along with a leaderboard feature.

## Technologies Used
- **Backend Framework**: FastAPI
- **Message Broker**: Kafka (with Zookeeper)
- **Database**: PostgreSQL
- **Real-Time Updates**: WebSockets
- **Containerization**: Docker

## Getting Started

### Prerequisites
- Python 3.7 or later
- `pip`
- Database server (PostgreSQL)
- Kafka and Zookeeper servers

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vaibhav-crux/pooling-system.git
   cd polling-system
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate # On Mac use `venv\bin\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   Create a `.env` file and set the required environment variables:
   ```plaintext
   DATABASE_URL=postgresql://user:password@localhost/dbname
   KAFKA_BROKERS=localhost:9092
   KAFKA_TOPIC=polls
   ```

### Database Setup

1. **Create Database**
   Ensure your PostgreSQL database is running and create a new database.

2. **Initialize Database Tables**
   Run the following commands to create the necessary tables:
   ```bash
   alembic upgrade head
   ```

### Kafka and Zookeeper Setup

Ensure you have a Kafka and Zookeeper cluster up and running. You can use Docker for quick setup:

`docker-compose.yml`

### Running the Application

To run the application, execute:

```bash
uvicorn app.main:app --reload
```