pipeline {
    agent any 

    stages {
        stage('Build') {
            steps {
                echo 'Building..'

		sh 'docker build -t tomdai -f Dockerfile . '

            }
        }
        stage('Test') {
            steps {
	      script {
		docker.image('tomdai').inside("--entrypoint=''") {

                  echo 'Testing..'
	
		  sh 'flake8'
		}
	      }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
		sh 'docker run -p 5000:5000 -e PORT=5000 tomdai:latest'
		sh 'curl http://localhost:5000'
            }
        }
    }
}
