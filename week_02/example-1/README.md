# Week 2

This week you will learn how to package and containerized microservice.

Once you have installed `Docker` follow the steps.

## Steps

1. Open Terminal and Go to `example-2` directory.
2. Run `docker build -t week-02-code .`
3. Verify image that is created or not by running `docker images`
4. Run `docker run -d -p 8000:8000 week-02-code`
5. Run `docker container ls` to check the container details.
6. Open your favorite browser and go to [http://localhost:8000/](http://localhost:8000/). If everything is correct then you will see the video in browser.
