terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# 65d7bfa61d631c4cfded7de89294dbd991c927ef5c2045620bbde78dcbf784b5

# I will set that variable using -var="do_token=..." in CLI
variable "digital_ocean_token" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.digital_ocean_token
}

resource "digitalocean_droplet" "web" {
  image  = "ubuntu-18-04-x64"
  name   = "web-1"
  region = "NYC1" # invalid in documentation (nyc2 is not valid option)
  size   = "s-1vcpu-1gb"
}