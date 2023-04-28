This code retrieves current weather data for a given latitude and longitude using the OpenWeatherMap API.

#__Requirements__ :
Python 3.6 or higher
requests module

#__Installation__ :
Clone the repository.
Install the requirements.txt

#__Usage__:

* Obtain an API key from OpenWeatherMap.

* Run the main.py script to retrieve the current weather data. by running  : python main.py
* Make request to the api

#__Configuration__:
The config.py file contains the following variables:

* API_KEY: Your OpenWeatherMap API key.


#__Dockerfile__:
You can also buil a docker image by follow this step :

* install docker
* install git
* go to a terminal
* git clone https://github.com/efrei-ADDA84/20211279.git
* docker build -t 20211279 -f ./Dockerfile . 
* docker run -p 8081:8081 --env API_KEY=*** 20211279
* go to another terminal
* curl "http://localhost:8081/?lat=5.902785&lon=102.754175"

#__difficulty__ :  

* I encountered errors while running the workflow, such as issues with Docker image building or publishing to Docker Hub. These errors could have been caused by a misconfiguration in the YAML file, syntax errors, or other issues.

* I also had authorization problems while trying to connect to Docker Hub or running certain Docker commands, possibly due to insufficient permissions.

* Additionally, I had difficulties adding my Docker username and password to the secrets or accessing them from the workflow.

* I had trouble with port forwarding when using the docker run command. Specifically, I encountered an issue while trying to use the command docker run --network host --env API_KEY=**** 20211279 because I was working on Windows. To resolve this issue, I used the command docker run -p 8081:8081 --env API_KEY=*** 20211279 instead. This allowed me to forward port 8081 on my local machine to port 8081 in the Docker container. As a result, I was able to access my Flask app running in the Docker container at http://localhost:8081.

* I encountered an issue while adding Hadolint to my GitHub workflow. After adding Hadolint, my workflow was broken due to an issue with my Dockerfile. To fix the problem, I changed my "RUN" command in the Dockerfile to be: "RUN pip install --no-cache-dir -r requirements.txt".