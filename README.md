# vulnPingApp
Simple Vulnerable Ping Application

## Setup

To run the Vulnerable Ping Application you will first need to have Docker and Docker Compose installed. You can find instructions how to do this (here)[https://docs.docker.com/compose/gettingstarted/]

After you have Docker and Docker Compose installed you will need to clone this repository, then cd to the vulnPingApp directory.
```bash

┌──(logan)-[/tmp]
└─$ git clone https://github.com/1mckenna/vulnPingApp.git
Cloning into 'vulnPingApp'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
                                                                                                                               
┌──(logan)-[/tmp]
└─$ cd vulnPingApp 

┌──(logan)-[/tmp/vulnPingApp]
└─$ 

```

Next, we need to build the containers before we can launch them

```bash
┌──(logan)-[/tmp/vulnPingApp]
└─$ docker compose build
[+] Building 0.0s (0/1)
[+] Building 0.2s (2/3)
 => [internal] load build definition from attacker.Dockerfile
 => => transferring dockerfile: 163B
 => [internal] load .dockerignore
 => => transferring context: 2B
[+] Building 0.6s (4/11)
 => [internal] load .dockerignore
 => => transferring context: 2B
[+] Building 0.6s (7/7) FINISHED
 => [internal] load build definition from attacker.Dockerfile
 => => transferring dockerfile: 163B
 => [internal] load .dockerignore
[+] Building 0.6s (12/12) FINISHED
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load build definition from pingApp.Dockerfile
 => => transferring dockerfile: 292B
 => [internal] load metadata for docker.io/library/python:3.12.0a5-alpine3.17
 => [1/7] FROM docker.io/library/python:3.12.0a5-alpine3.17@sha256:b6b917050cdf2ef4555d8af7a941f3b9a1b22771d37b0432fada14850e5fbb0d
 => [internal] load build context
 => => transferring context: 1.67kB
 => CACHED [2/7] WORKDIR /srv
 => CACHED [3/7] RUN apk update && apk add nmap-ncat bash
 => CACHED [4/7] RUN pip install --upgrade pip
 => CACHED [5/7] RUN pip install flask
 => CACHED [6/7] ADD  templates/ /srv/templates/
 => CACHED [7/7] COPY ping.py /srv
 => exporting to image 
 => => exporting layers
 => => writing image sha256:94d1d231ea234c2e642cc4263987f1b85cb426f283ee6037fb4b5faed7fee7c6
 => => naming to docker.io/library/vulnpingapp-web

```

## Running The App

Now that everything has been built you can launch the web server and the attacker machine by running
```bash
┌──(logan)-[/tmp/vulnPingApp]
└─$ docker compose up
[+] Running 2/2
 ⠿ Container vulnpingapp-attacker-1  Created
 ⠿ Container vulnpingapp-web-1       Recreated
Attaching to vulnpingapp-attacker-1, vulnpingapp-web-1
vulnpingapp-web-1       |  * Serving Flask app 'ping'
vulnpingapp-web-1       |  * Debug mode: on
vulnpingapp-web-1       | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
vulnpingapp-web-1       |  * Running on all addresses (0.0.0.0)
vulnpingapp-web-1       |  * Running on http://127.0.0.1:5000
vulnpingapp-web-1       |  * Running on http://172.22.0.2:5000
vulnpingapp-web-1       | Press CTRL+C to quit
vulnpingapp-web-1       |  * Restarting with stat
vulnpingapp-web-1       |  * Debugger is active!
vulnpingapp-web-1       |  * Debugger PIN: 105-215-620

```

You can connect to the attacker machine by running the following command
```bash

┌──(logan)-[/tmp/vulnPingApp]
└─$ docker exec -it vulnpingapp-attacker-1 bash
attacker:/tmp#

```