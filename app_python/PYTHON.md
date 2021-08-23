<h3>Best practices that I could find</h3>
<ul>
    <li>Use server side to determine time. The browser or user PC can have invalid time configured</li>
    <li>Use separate files to store static, because it allows caching</li>
    <li>Use django cache backend to cache template file which is not changed at all. For speed up</li>
    <li>Use external library (axios) to send requests, to make project more maintainable</li>
</ul>