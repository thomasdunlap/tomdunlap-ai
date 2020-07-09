pipeline {
    agent { 
	docker { 
	  image 'python:3.7.3'
	  args '-p 3000:3000' 
	} 
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'docker build -t test -f Dockerfile.build .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
	
		sh 'flake8'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
