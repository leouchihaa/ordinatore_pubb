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
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r ./src/requirements.txt
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh '''
                        cd src
                        echo "Salsa" | sudo -S docker build -t myapp:latest .
                    '''
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    sh '''
                        # Stop and remove the Docker container if it exists
                        docker stop myapp_container || true
                        docker rm myapp_container || true
                        
                        # Run the Docker container
                        docker run -d -p 3333:3333 --name myapp_container myapp:latest
                    '''
                }
            }
        }
    }
}
