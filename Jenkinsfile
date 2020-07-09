pipeline {
    agent any 

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
