pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'pip3 install -r requirements.txt'
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
