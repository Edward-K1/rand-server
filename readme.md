# Server Tracker - An Interview Challenge
[View On Heroku](https://rand-server.herokuapp.com/)

![Screenshot](https://github.com/Edward-K1/rand-server/blob/master/resources/images/new-shot.png?raw=true)

## Technologies:
- Python
- Flask
- Javascript

## Setup
- Clone the repo: `git clone https://github.com/Edward-K1/rand-server.git`
- CD into project
- Create python virtual environment: `python -m venv venv`
- Activate virtual environment: `source venv/bin/activate` or `venv\Scripts\activate`
- Install requirements with pip: `pip install -r requirement.txt`
- Create a `.env` file and add the variable `SECRET_KEY`. Checkout the [.env.example](https://github.com/Edward-K1/rand-server/blob/master/.env.example) file for reference
- run the project: `python api.py`
- Navigate to: [http://localhost:5000](http://localhost:5000)

## Additional Info
- Server time on heroku is in GMT / UTC. You'll need to add the respective hours for your timezone e.g 8:00AM GMT = 11:00AM EAT

