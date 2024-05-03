# Project-API-Gateway

## Introduction
The `project-API-gateway` is designed to streamline the interactions between the front-end and various microservices in an e-commerce platform using KrakenD API Gateway. This setup helps in managing requests efficiently, providing a single entry point for all services, and improving the security and scalability of the application.

## Features
- **Single Entry Point**: Simplifies client-side communication by providing a single entry point for all backend services.
- **Load Balancing**: Distributes incoming API traffic across multiple backend services to improve responsiveness and availability.
- **Rate Limiting**: Prevents overuse of resources by limiting how often each user can call the API.
- **Caching**: Reduces the load on the API by caching common requests, improving the response time.
- **Security**: Implements standard security practices such as authentication and authorization to protect against unauthorized access.
However, in this project, I have demonstrated -
1. Single Entry Point
2. Rate Limiting
3. Security

## Technologies Used
- **KrakenD**: As the API Gateway to manage all the incoming requests to the system.
- **Docker**: For containerizing the application and ensuring consistency across various development and production environments.
- **Microservices Architecture**: Various backend services are split into smaller, independent services.

## Getting Started

### Prerequisites
- Docker
- Git
- Postman OR any other application that allows the testing of web APIs

### Installation
1. **Install GIT on your system**
2. **Clone the repository**
   ```bash
   git clone https://github.com/sumitandsumit/project-API-gateway.git
   cd project-API-gateway
3. **Install docker as per your system configuration**
4. **Install Postman OR any application to test APIs**
   
### Running the Application
1. **To start all containers**
   ```bash
    ./start.sh
2. **To stop all containers**
   ```bash
    ./stop.sh

### Usage
You can access these APIs using Postman
**URLs and supported methods**
1. **Product service**
   URL: http://localhost:8088/api/products
   Methods: GET, POST
2. **Order service**
   URL: http://localhost:8088/api/orders
   Methods: GET
3. **User service**
   URL: http://localhost:8088/api/users
   Methods: GET
4. **AUTH service**
   URL: http://localhost:8088/api/auth
   Methods: POST

