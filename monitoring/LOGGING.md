<h3>Best practices that I could find for Logging</h3>
<ul>
    <li>Use JSON format to output logs.</li>
    <li>Collect logs from containers in docker.</li>
    <li>Output more information. Log level, ip addresses</li>
    <li>Use bounded values for labels. Like: level of logging, but not ip addresses of users</li>
</ul>

<h6>Grafana: http://142.93.48.168:3000/login </h4>
<ul>
    <li>Username: <i>admin</i></li>
    <li>Password: <i>admin</i></li>
</ul>
<h3>Loki Data source connected</h3>

![Grafana logs](imgs/datasource.png?raw=true "Data source connected")

<h3>Query example</h3>

![Grafana query](imgs/devops2.png?raw=true "Grafana query")

<h3>Logs example</h3>

![Grafana logs](imgs/grafana.png?raw=true "Grafana logs")

<h1>Lab 8.</h1>
<p>I have configured log rotation and memory limit inside server using logrotate</p>

```
/prometheus/query.log {
    daily
    rotate 7
    compress
    delaycompress
    postrotate
        killall -HUP prometheus
    endscript
}
```

I have configured all stack on separate server because I have Windows laptop.

<h3>Targets in prometheus</h3>

![Grafana logs](imgs/lab8_targets.png?raw=true "Grafana logs")

<h3>All dashboards</h3>

![Grafana logs](imgs/lab8_all_dashboards.png?raw=true "Grafana logs")

<h3>Prometheus dashboards</h3>

![Grafana logs](imgs/lab8_prom_dashboard.png?raw=true "Grafana logs")

<h3>Loki dashboards</h3>

![Grafana logs](imgs/lab8_loki_dashboard.png?raw=true "Grafana logs")