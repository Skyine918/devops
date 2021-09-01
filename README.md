![example workflow](https://github.com/Skyine918/devops/actions/workflows/django.yml/badge.svg)

<br />
<p align="center">
  <h3 align="center">Django Time application</h3>

  <p align="center">
    Using axios, django, world time api. Link to : <a href="https://github.com/Skyine918/devops">github repository</a>
    <br/>
    <br/>
  </p>
  
  <h3 align="center">Docker</h3>
  <ol>
    <li>Link to Docker Hub: <a href="https://hub.docker.com/repository/docker/skyline918/django-time-app">skyline918/django-time-app</a></li>
    <li>docker pull <a href="">skyline918/django-time-app</a></li>
    <li>docker run -p 8000:8000 skyline918/django-time-app</li>
    
  </ol>
  
  <h3 align="center">Linter</h3>
  <ol>
    <li>To run linter, use <i>pylint .\app_python</i></li>    
  </ol>
  
  <h3 align="center">Unit tests</h3>
  <ol>
    <li>I have implemented django test cases using internal django testing framework which allows to test endpoints. Also I have rewritten the date logic to use my endpoint instead of public world time API. I have 2 test cases in tests.py file. First checks that logic is correct (i.e usability test case). And second test case ensures validation of timezone query parameter in API</li>    
    <li>to run tests: <i>python manage.py test</i> while in app_python folder</li>    
  </ol>
  
  <h3 align="center">CI actions</h3>
  <ol>
    <li>I have configured CI pipeline as 1 job consisting of 10 steps. You can find it in workflows folder.</li>    
  </ol>
</p>

<br/><br/><br/>
