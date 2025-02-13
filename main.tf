terraform {
  required_providers {
    ise = {
      source = "CiscoDevNet/ise"
    }
  }
}

provider "ise" {
  username = "username"
  password = "password"
  url      = "https://ise.url"
}

module "ise" {
  source  = "netascode/nac-ise/ise"
  version = ">= 0.1.2"

  yaml_directories = ["data/"]
}