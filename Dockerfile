# specifies the Parent Image from which you are building.
FROM python:3.9

# specify the working directory for the image
WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

# Copy application code
COPY ./app /code/app

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]