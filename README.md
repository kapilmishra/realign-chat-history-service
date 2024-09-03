FastAPI Clean Architecture Example
This project is an example of how to structure a FastAPI application following the principles of Clean Architecture (also known as Hexagonal Architecture). The goal is to keep the codebase maintainable, testable, and scala# Project Name

## Description

This project is a FastAPI application implementing a messaging system using Clean Architecture principles. It allows for the creation, updating, deletion, and retrieval of messages and conversations, as well as appending messages to conversations. The application uses an in-memory data repository for simplicity.

## Clean Architecture Principles

The project follows [Clean Architecture principles](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) to ensure that the application is scalable, maintainable, and testable. The architecture is organized into several layers:

- **Entities**: Contains the core business logic and domain models, such as `Message` and `Conversation`.
- **Use Cases**: Defines the application's business rules and logic. This layer includes use cases such as creating, updating, and reading messages and conversations.
- **Repositories**: Interfaces for data storage, including in-memory implementations for the purpose of this project.
- **Interfaces (API)**: Contains the FastAPI routers and endpoint definitions, mapping HTTP requests to use cases.

## Folder Structure

- **/src**: The root source directory containing all application code.
  - **/app**: Main application folder.
    - **/application**: Contains use cases that implement business logic.
    - **/domain**: Includes domain models and repositories.
    - **/infrastructure**: Contains implementations of repositories and other infrastructure concerns.
    - **/interfaces**: Contains API routers and endpoint definitions.
    - **main.py**: The entry point for the FastAPI application.

## Running the Application

To run the application using Docker Compose, follow these steps:

1. **Ensure Docker and Docker Compose are installed** on your machine.

2. **Build and run the application** using Docker Compose:

    ```sh
    docker-compose up
    ```

3. **Access the FastAPI application** at `http://localhost:8000`.

4. **View the Swagger UI** for API documentation and testing at `http://localhost:8000/docs`.

## Docker Configuration

The Docker setup is configured to build the application and run it in a container. It includes a `Dockerfile` and a `docker-compose.yml` file:

- **Dockerfile**: Defines the application image, including the base Python image, dependencies, and the command to run the application.
- **docker-compose.yml**: Configures the Docker service, specifying build context, environment variables, and port mappings.

## Dependencies

The project uses Poetry for dependency management. Dependencies are defined in `pyproject.toml` and can be installed by running:

```sh
poetry install
