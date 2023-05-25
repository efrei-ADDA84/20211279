FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV API_KEY=c3d9e313fd2a407b8c67a810ce2eee46

COPY . .

EXPOSE 8081


CMD ["python", "main.py"]
