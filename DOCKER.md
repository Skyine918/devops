<h3>Best practices that I could find for Docker</h3>
<ul>
    <li>Use linter for Dockerfile (hadolint). The only output for my dockerfile is <i>.\Dockerfile:14 DL3042 warning: Avoid use of cache directory with pip. Use `pip install --no-cache-dir package</i></li>
    <li>Disable Python output buffering, to see all changes at once during development. set up envs PYTHONDONTWRITEBYTECODE/PYTHONUNBUFFERED in Docker compose </li>
    <li>Use python slim image instead of alpine, because alpine is slow as was discussed in telegram chat </li>
</ul>