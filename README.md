# Mtcars Flask API

This homework and README file was adapted from the one provided in stat418.

I am creating a predictive linear model using mpg as a response and cyl, disp, hp, drat, wt, qsec, vs, am, gear, carb as predictors using Python in a Docker container.

The local host address is 4000.

This repo contains the following files... 
    curl_test.sh
    docker-compose.yml
    Dockerfile
    mtcars.csv
    prediction.py
    README.md
    requirements.txt
    server.py

Here is how to stand up my API...

First, cd into the folder and run the following codes below

`docker compose up -d`

Open up a new terminal window and run the curl command to check its up

`curl http://localhost:4000/`

Then, I run a test 

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6","disp":"160","hp":"110","drat":"3.9","wt":"2.62","qsec":"16.46", "vs":"0","am":"1","gear":"4","carb":"4"}' "http://localhost:4000/predict_mpg"`

Now that we know it works locally, the next step is to create a repository on the docker hub to push our image.

Return to the terminal and into the folder and run the following code

`docker ps -a`

`docker images`

We need to change the tag of the image to match the docker hub repository we just created

`docker tag mtcars-flask-api-app:latest kpvo/mtcars-flask:latest`

Now push it

`docker push kpvo/mtcars-flask:latest`

Almost done! Now we create our container on Google Cloud Run. 

Once that is done, return to the terminal and run our curl command but with the url

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6","disp":"160","hp":"110","drat":"3.9","wt":"2.62","qsec":"16.46", "vs":"0","am":"1","gear":"4","carb":"4"}' "https://mtcars-flask-253216833082.us-central1.run.app/predict_mpg"`

The response you should get is...

`{
  "predict mpg": 22.59950576126238
}`
