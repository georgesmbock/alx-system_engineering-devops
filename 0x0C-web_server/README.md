# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

| Task                                    | File                                 | Requirement                                                                                             |
|-----------------------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------|
| 0. Transfer a file to your server       | 0-transfer_file                      | Write a Bash script that transfers a file from our client to a server                                   |
| 1. Install nginx web server             | 1-install_nginx_web_server           | Web servers are the piece of software generating and serving HTML pages, let’s install one!             |
| 2. Setup a domain name                  | 2-setup_a_domain_name                | Provide the domain name in your answer file                                                             |
| 3. Redirection                          | 3-redirection                        | Configure your Nginx server so that /redirect_me is redirecting to another page                         |
| 4. Not found page 404                   | 4-not_found_page_404                 | Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page  |
| 5. Install Nginx web server (w/ Puppet) | 7-puppet_install_nginx_web_server.pp | Install and configure an Nginx server using Puppet instead of Bash                                      |
