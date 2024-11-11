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

## API Endpoints

- **Create a Poll**
  - Method: `POST`
  - Endpoint: `/polls`
  - Request Body:
    ```json
    {
      "question": "What is your favorite color?",
      "option1": "Red",
      "option2": "Blue",
      "option3": "Green",
      "option4": "Yellow"
    }
    ```
  - Response:
    ```json
    {
      "id": 1,
      "question": "What is your favorite color?",
      "option1": 0,
      "option2": 0,
      "option3": 0,
      "option4": 0
    }
    ```

- **Vote on a Poll**
  - Method: `POST`
  - Endpoint: `/polls/{id}/vote`
  - Request Body:
    ```json
    {
      "poll_id": 1,
      "option": 1
    }
    ```
  - Response: `204 No Content`

- **Get Poll Results**
  - Method: `GET`
  - Endpoint: `/polls/{id}`
  - Response:
    ```json
    {
      "id": 1,
      "question": "What is your favorite color?",
      "option1": 5,
      "option2": 3,
      "option3": 8,
      "option4": 2
    }
    ```

- **Get Leaderboard**
  - Method: `GET`
  - Endpoint: `/leaderboard`
  - Response:
    ```json
    {
      "leaderboard": [
        {"option": "Green", "count": 10},
        {"option": "Red", "count": 8},
        {"option": "Blue", "count": 6}
      ]
    }
    ```

## Real-Time Updates

Connect to the WebSocket endpoint using a WebSocket client (e.g., in JavaScript):

```javascript
const socket = new WebSocket('ws://localhost:8000/ws');

socket.onmessage = function(event) {
    console.log(JSON.parse(event.data));
};
```