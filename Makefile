jenkins:
	docker run -v /var/run/docker.sock:/var/run/docker.sock -v docker_mnt:/var/jenkins_home/ -p 8443:8443 -p 8080:8080 -p 50000:50000 0559cd841542
