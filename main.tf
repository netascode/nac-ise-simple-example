terraform {
  required_providers {
    ise = {
      source  = "CiscoDevNet/ise"
      version = "0.2.14"
    }
  }
}

provider "ise" {
  username = "username"
  password = "password"
  url      = "https://ise.url"
}

module "ise" {
  source = "git::https://github.com/netascode/terraform-ise-nac-ise.git?ref=dev"

  yaml_directories = ["data/"]
}