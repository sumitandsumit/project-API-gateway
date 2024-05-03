FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install Flask flask_jwt_extended cryptography pyjwt
CMD ["python", "./auth_service.py"]