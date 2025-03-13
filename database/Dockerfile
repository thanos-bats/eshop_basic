FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY database/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the database init_db file
COPY database/init_db.py .

# Copy models file from eshop_api
COPY eshop_api/database/models.py ./models.py

# Command to run the initialization of the database
CMD ["python", "-u", "init_db.py"]