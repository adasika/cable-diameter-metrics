# cable-diameter-metrics
 Creating visual representation of cable diameter metrics

IMPORTANT!- How to Run the Code

Due to the nature of the assignment, I have decided to include a React Project within a Django Project. All the files/dependencies 
for React specifically are included in the compressed zip. However, I have left a requirements.txt to install all Django reqs.

Step 1: Make sure to pip install all Python dependecies(using venv) using the requirements.txt file located in 
	the cable-diameter-metrics folder.

Step 2: Make sure to have RabbitMQ installed. This is not a dependency for the Django project specifically, but our celery workers
	will not be functional without this.

Step 3: Make sure to have 4 different command-line windows open. As I used Windows for completing this assingment, most of my
	instructions will be specifically for Windows.
	  
	Before starting, make sure to create a venv and pip install -r requirements.txt.
	Now go into the venv in the first three terminals.
	- In the first terminal- 1. cd cable-diameter-metrics
				 2. cd metrics_api
				 3. python manage.py runserver
	- In the second terminal- 1. cd cable-diameter-metrics
				  2. cd metrics_api
				  3. celery -A metrics_api worker -l info --pool=solo
	- In the third terminal- 1. cd cable-diameter-metrics
				 2. cd metrics_api
				 3. celery -A metrics_api beat -l info

	Do not be in the venv for this last terminal
	-In the fourth terminal- 1. cd cable-diameter-metrics
				 2. cd metrics_api
				 3. cd metrics-ui
				 4. npm start

	Now go to http://localhost:3000/- and the code shoud be (hopefully) working! The graphs will be changing every 5 minutes.
	If there are any issues at all, please feel free to reach out to me at architdasika1@gmail.com

Solution Questions
1. This coding test took me about 3-4 hours to complete. If I had more time, I would improve the UI as well as the backend 
   functionality. I used majority of the time allotted for this test to setup asynchronous celery workers. I would love to further 
   improve the readability of the graphs and also allow for increased user interaction. From a development standpoint, the frontend 
   and backend code bases would be separate, and vital data would be stored in an .env file. Also, majority of the test, db, and 
   package files would be ignored and could possibly be stored in a docker container for deployment.

2. I used a variety of different libraries including but not limited to Django, React, and Celery along with Charts.JS for graphing
   purposes. Effectively, I used the backend I build to query the timeseries API data, so that the application doesn't become very
   heavy on the frontend. I used celery workers to asynchronously track data as it changes. While I set the current value to every
   5 minutes, this number could very easily be changed based on needs. I used React as well as Charts.JS for clean readability as 
   well as visibility for prospective users.

3. I used 3 different line graphs for the 3 different types of data points (min/max/avg). My reasoning behind using a line graph is
   due to the fact that a user wants to track information over a period of time. Detecting anomalies or trends in data is not much
   an issue to a user with the use of a line graph.

4. The timeseries API was definitely a bit difficult to work with due to having a large dataset along with the nesting of data 
   structures. I personally used a backend framework to query this data in an effective manner. This API could be directly called to
   our frontend as well, but adding some nesting logic felt a little bit too frontend heavy in my opinion. Maybe having one data
   structure(such as series), and using the endpoint to detect what information was being passed would be more convenient.

In all, I had a lot of fun working on this assignment. Any feedback is greatly appreciated!