<h3>Best practices that I could find for CI</h3>
<ul>
    <li>Use docker layer caching</li>
    <li>Use one job and multiple steps for performance</li>
    <li>Automate as much as possible</li>
    <li>Include unit test in CI pipeline in order to protect production from errors</li>
    <li>Include linters in CI pipelines</li>
    <li>Keep pip up to date</li>
    <li>Use slim linter instead of common one because my project do not contains languages like Rust</li>
    <li>Keep secrets like dockerhub credentials as repository secrets</li>
</ul>

<h3>Best practices that I could find for Jenkins</h3>
<ul>
    <li>Use linter</li>
    <li>Use tests</li>
</ul>