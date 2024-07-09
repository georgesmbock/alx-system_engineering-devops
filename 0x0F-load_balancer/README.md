# Learning Objectives and Tasks
You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.


| Tasks                                   | Files                                   | Requirements                                                                                                                                      |
|-----------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0. Double the number of webservers      | 0-custom_http_response_header           | The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works.      |
| 1. Install your load balancer           | 1-install_load_balancer                 | Install and configure HAproxy on your lb-01 server.                                                                                               |
| 2. Add a custom HTTP header with Puppet | 2-puppet_custom_http_response_header.pp | Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.                                | 
