# RIPL Project

My idea was to build a way to visualize the provided BLS salary data. View the highest paying job in each state by hovering over each one. Click on a state to see detailed salary stats.

## Pre-requisites
- `npm` 
- `pipenv`
- postgresql 14
- python >= 3.10
- node >= 20 or newer

## Setup 
- Clone this repository

**Backend Setup**

- `cd` into this repo and run `pipenv install` 
- Copy the `.env.sample` file into a file called `.env`. Replace the values with ones that work on your system, especially the database name, user, and password.
- Run `pipenv shell` to activate the virtual environment
- Run `python3 app/pandas_input.py` to populate the database 
- Run `fastapi dev app/main.py` to launch the backend, which runs on http://localhost:8000
- View the interactive API docs at http://localhost:8000/docs

**Frontend Setup**

- `cd` into `client` and run `npm install`
- Run `npx vite dev` to launch the frontend.
- Frontend should run on http://localhost:5173


## Todo
- Clean the data in a more realistic way, so we don't end up with duplicate salaries per job title per state
- Think about what other data could be shown on map, in detail or overview
- Add close button for detail view
- Use schema validation for state_abbr path parameter