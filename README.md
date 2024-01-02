# FastAPI CRUD for Manage Football club

## Overview

This project is a FastAPI-based CRUD (Create, Read, Update, Delete) application for managing football players and teams. It provides API endpoints to perform operations such as creating players, reading data from the database, updating player information, and deleting players.

## Features

- **Create Player:** Add a new football player to the database.
- **Read Player:** Retrieve player information from the database.
- **Update Player:** Modify player details in the database.
- **Delete Player:** Remove a player from the database.

## Testing

- **E2E:** Testing the entire process from creating a player to deleting the player from the data
- **Create Player:** valid or not valid value , value with null(None) , max length String and int , or deviation of characters from what is defined
- **Update Player:** valid or not valid value , value with null(None) , max length String and int , or deviation of characters from what is defined

## Technologies Used

- FastAPI
- SQLAlchemy
- SQLite 

### Prerequisites

- Python 3.7 or higher
- Pipenv (optional but recommended)
- pytest (conftest,fixtures)
