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
		sh 'docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 127.0.0.1:8001:8080 -e PORT=8080 tomdai:latest'
            }
        }
	stage('API Test') {
	    steps {
	        echo "API Test"
		sh 'curl https://127.0.0.1:8001'
		//sh 'curl http://172.24.0.1:5000'
	    }
	}
    }
}
