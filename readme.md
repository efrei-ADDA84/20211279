This code retrieves current weather data for a given latitude and longitude using the OpenWeatherMap API.

#__Requirements__ :
Python 3.6 or higher
requests module

#__Installation__ :
Clone the repository.
Install the requests module by running  : pip install requests.

#__Usage__:

* Obtain an API key from OpenWeatherMap.

* Edit the config.py file with your API key, latitude, and longitude values.

* Run the main.py script to retrieve the current weather data. by running  : python main.py


#__Configuration__:
The config.py file contains the following variables:

* API_KEY: Your OpenWeatherMap API key.
* LAT: The latitude of the location you want to retrieve weather data for.
* LONG: The longitude of the location you want to retrieve weather data for.
Example


#__Dockerfile__:
You can also buil a docker image by follow this step :

* install docker
* install git
* go to a terminal
* git clone https://github.com/efrei-ADDA84/20211279.git
* docker build -t 20211279 -f ./Dockerfile . 
* docker run --env LAT=\<Lat>--env LONG=\<long> --env API_KEY=\<yourapikey> 20211279

#__difficulty__ :  

We faced obstacles in obtaining an API key necessary for our project. This difficulty slowed down our progress and required additional research to find an adequate solution. Solution : Wait for the creation of the Apikey.

During the process of creating the Docker image, we encountered a minor blockage that delayed the project delivery. We had to investigate and resolve this technical problem to ensure the proper functioning of our application.

Bonus : 
* i use type Dockerfile | docker run --rm -i hadolint/hadolint insted of : docker run --rm -i hadolint/hadolint < Dockerfile because i work on windows
