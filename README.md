
## Requirements

- Python 3.12.6 or later

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

### Run The API Server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
.