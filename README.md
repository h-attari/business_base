# Business Base

The *Business Base* application is based in Python and Fast-API web-framework and uses SQlite for the database.

The Python version used for the application is Python 3.9.16

## To Run the application -
Create a virtual environment in Python with the name `env` or any other desired name.
```shell
python3 -m venv env
```

Activate the created virtual environment.
```shell
source env/bin/activate
```

Navigate to the project root diractory if not yet in the root directory and install the dependencies specified in the `requirements.txt` file.
```shell
pip install -r requirements.txt
```

Once the requirements are successfully installed, the project can be served using the the uvicorn command,
```shell
uvicorn app.main:app
```
or can run on the desired the host and port using
```shell
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The application API docs will be accessible at
```url
http://127.0.0.1:8000/docs
```


## Application Tests -
The test cases for the application are implemented in pytest, to run the test cases run the following command.
```shell
pytest
```

The code coverage percentage can also be seen while running the test cases using the  `--cov` flag.
```shell
pytest --cov
```

To view the test code coverage report as HTML run the command.
```shell
coverage html

open htmlcov/index.html
```


## Containerizing the application -
The application is containerized using docker and can be build as a docker image and deployed.

To build the docker image with the name `business_base` (any desired name can be used), run the command.
```shell
docker build -t business_base .
```
This will build a docker image with the specified name.

The pre-built docker image then can be executed using `docker run` command and exposing the port to access the application from the browser on the docker host (or any browser if deployed on a web server) with container name as `business_base_app`.
```shell
docker run --name business_base_app -p 80:80 business_base
```

The application API docs will now be availabe at:
```url
http://127.0.0.1/docs
```
or
```url
http://<machine-IP-address>/docs
```
from the docker host browser.

To stop the application hit
```keymap
Ctrl + C
```

The container can also be executed in a detached mode by
```shell
docker run -d --name business_base_app -p 80:80 business_base
```
and it can be killed with the command
```shell
docker stop <container-id>
```


> **_NOTE ->_** Multiple docker conatiners (stopped/running) with same name can not be created.