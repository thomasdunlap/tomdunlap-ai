pipeline {
    agent {
	docker { image 'python:3.7.2'}
	}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'python --version'
		sh 'pip3 install -r requiremtents'
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
