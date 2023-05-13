# Vacation planner

an AI-powered vacation planner

# Quick start

clone the repo:

```
git clone https://github.com/shaomaiguanguan/vacation_planner.git
```

install the dependencies

```
cd backend
pip install -r requirements.txt
cd ../frontend
npm install
```

input your OpenAI API key in `backend/app.py`

```
API_KEY = ""
```

start the frontend:

```
cd frontend
npm run dev
```

start the backend:

```
cd backend
flask run --port 5001 --debug
```

enjoy your vacation!
