<h3>Best practices that I could find</h3>
<ul>
    <li>Use server side to determine time. The browser or user PC can have invalid time</li>
    <li>Use external service API to determine time (world time API), because it is ready solution</li>
    <li>Use separate static files (JS/CSS), i.e not inside HTML template, because it allows browser caching</li>
    <li>Use django cache backend to cache template file which is not changed at all. For speed up</li>
    <li>Use external library (axios) to send HTTP requests on frontend, to make project more maintainable</li>
    <li>Use python3 typing hints to make the code better. Like: <i>def main_page(request: HttpRequest) -> HttpResponse:</i></li>
    <li>Configure settings to use Environment variables, to be able easily change it on production environment (ALLOWED_HOSTS/DEBUG mode in settings.py)</li>
    <li>Use python linter PyLint, to make code maintainable and standardised</li>
    <li>Freeze requirements in <i>requirements.txt</i> file, to use it later in Docker/production server for example</li>
    <li>Add <i>.gitignore</i> file, add there .idea/, __pycache__/, .sqlite3, etc. To keep repository clean</li>
</ul>
<h4>Lab 3 (Tests)</h4>
<ul>
    <li>I have written django internal test framework unit tests, because I have django project.</li>
    <li>I have written TestCase name, use-case, preconditions, steps to execute and expected results in python docstring</li>
    <li>I have performed all statements coverage testing</li>
</ul>