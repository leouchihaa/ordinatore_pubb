pipeline {
    agent any

    stages {
        
        stage('Clone repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/leouchihaa/ordinatore_pubb.git'
                }
            }
        }

        stage('Working directory & info') {
            steps {
                script {
                    sh '''
                        python3 --version
                    '''
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                        sudo python3 -m venv venv
                        sudo source venv/bin/activate
                        sudo pip install -r ./src/requirements.txt
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh '''
                        cd src
                        sudo docker build -t myapp:latest .
                    '''
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    sh '''
                        # Stop and remove the Docker container if it exists
                        sudo docker stop myapp_container || true
                        sudo docker rm myapp_container || true
                        
                        # Run the Docker container
                        sudo docker run -d -p 3333:3333 --name myapp_container myapp:latest
                    '''
                }
            }
        }
    }
}
