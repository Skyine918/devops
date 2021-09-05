<h3>Best practices that I could find for Terraform</h3>
<ul>
    <li>Do not commit .tfstate files (<a href="https://stackoverflow.com/questions/38486335/should-i-commit-tfstate-files-to-git">security risks</a>)</li>
    <li>Do not commit .terraform folder as it is platform dependant (example: executable for windows/linux)</li>
    <li>Do commit `.terraform.lock.hcl` files (<a href="https://stackoverflow.com/questions/67963719/should-terraform-lock-hcl-be-included-in-the-gitignore-file">dependencies</a>)</li>
    <li>Use small resources (smallest droplet in D.O. in my case) </li>
    <li>Use checks like <i>terraform fmt</i> and <i>terraform validate</i></li>
    <li>Use variables for sensitive data like DO API key</li>
    <li>Save terraform planning for safety</li>
</ul>