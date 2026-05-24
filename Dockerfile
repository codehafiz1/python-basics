FROM python:3.10-slim

# Install the system library that is missing (libffi)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "codehafiz1_bot.py"]
