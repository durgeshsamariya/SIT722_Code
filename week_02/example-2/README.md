# Task 2.3C

As we already discussed about docker. In this Task, we want you to write docker file by your own and dockerize microservice. It is very basic microservice which will return your details such as `student_id`, `name`, `unit_code`, and `campus`.

## Steps

1. Open Terminal and Go to `example-2` directory.
2. Check `main.py` file and change `about_me` information accordingly.
3. Open `Dockerfile` and details/instruction for docker.
4. Run `docker build ...` command.
5. Verify image that is created or not by running `docker images`
6. Run `docker run ...` command.
7. Run `docker container ls` to check the container details.
8. Open your favorite browser and go to [http://localhost:8000/](http://localhost:8000/). If everything is correct then you will see the details.
