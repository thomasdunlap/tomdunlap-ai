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
	      script {
		docker.image('tomdai').inside("--entrypoint=''") {

                  echo 'Testing..'
	
		  sh 'flake8 --version'
		}
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
