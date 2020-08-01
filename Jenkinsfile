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
		sh 'docker run -d -p 8001:8080 -e PORT=8080 tomdai:latest'
            }
        }
	stage('API Test') {
	    steps {
	        echo "API Test"
		sh 'docker exec tomdai:latest curl https://0.0.0.0:8001'
		//sh 'curl http://172.24.0.1:5000'
	    }
	}
    }
}
