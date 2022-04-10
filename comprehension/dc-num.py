version: "3.8"
services:
  num_app:
    build:
      context: .
      dockerfile: Dockerfile-num
    #stdin_open: true
    tty: true
    volumes:
      - .:/test-python
