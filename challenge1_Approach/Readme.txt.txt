Approach To deploy 3 tier application on GCP

Requirements
================
1 Public Instance for webserver - create in a public subnet
1 private instance for appserver and - create in a private subnet
1 private instance for mysql database - create in a private subnet

Tools
==========
gitlab for CI & CD
Terraform for resource provisioning
& GCP


Process
==========
1. Pull and execute tf code using gitlab
2. tf will enable required apis & create resources such as service accounts, network, subnets, firewall, disks, 1 public instance, 2 private instances etc.
