FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the eshop folder
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["python", "-u", "app.py"] 