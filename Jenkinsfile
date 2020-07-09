pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'docker build -t tomdai -f Dockerfile.build . '
            }
        }
        stage('Test') {
            steps {
		docker.image('tomdai:latest').inside("--entrypoint=''") {

                  echo 'Testing..'
	
		  sh 'flake8'
		}
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
