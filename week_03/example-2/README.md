# Example-2

Example-2 from Chapter 4 of [Davis, A. 2024, Bootstrapping Microservices with Docker, Kubernetes, GitHub actions, and Terraform / Davis, Ashley, Manning Publications](https://library.deakin.edu.au/record=b5599390~S1).

## Steps

1. Open Terminal and Go to `example-2/` directory.
2. Run `pip install -r requirements.txt`
3. Run `docker-compose up -d --build`
4. Verify container is created or not by running `docker-compose ps` command.
5. Open your favorite browser and go to [http://localhost:8000/](http://localhost:8000/). If everything is correct then you will see the video in browser.
6. Stop container by running `docker-compose stop` command.
