jenkins: docker_sock
	#docker run -v /var/run/docker.sock:/var/run/docker.sock -v docker_mnt:/var/jenkins_home/ -p 8443:8443 -p 8080:8080 -p 50000:50000 0559cd841542
	docker-compose up --remove-orphans

docker_sock:
	sudo chmod 777 /var/run/docker.sock

end_session:
	docker-compose down

lint:
	flake8
