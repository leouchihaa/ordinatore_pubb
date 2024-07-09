pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                script {
                    // Clona il repository Git
                    git clone 'https://github.com/leouchihaa/ordinatore_pubb.git'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Crea e attiva l'ambiente virtuale Python
                    powershell '''
                        python -m venv venv
                        ./venv/Scripts/Activate.ps1
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    // Costruisci l'immagine Docker
                    powershell '''
                        docker build -t myapp:latest .
                    '''
                }
            }
        }

        stage('Run Docker container') {
            steps {
                script {
                    // Ferma e rimuove il contenitore Docker se esiste già
                    powershell '''
                        docker stop myapp_container
                        if (-not $?) {
                            return 0
                        }
                        docker rm myapp_container
                        if (-not $?) {
                            return 0
                        }
                    '''

                    // Avvia il contenitore Docker
                    powershell '''
                        docker run -d -p 5000:5000 --name myapp_container myapp:latest
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            script {
                // Ferma e rimuove il contenitore Docker alla fine della pipeline
                powershell '''
                    docker stop myapp_container
                    if (-not $?) {
                            return 0
                        }
                    docker rm myapp_container
                    if (-not $?) {
                            return 0
                        }
                '''
            }
        }
    }
}
