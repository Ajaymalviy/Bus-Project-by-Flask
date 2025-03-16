version: '3.8'

services:
  # Flask Application
  app:
    container_name: bus-management-app
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=init.py
      - FLASK_ENV=development
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=root_password
      - MYSQL_DB=bus_management
    volumes:
      - .:/app
    depends_on:
      - db
    networks:
      - bms_network

  # MySQL Database
  db:
    container_name: bus-management-db
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: bus_management
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - bms_network

networks:
  bms_network:
    driver: bridge

volumes:
  mysql_data:
