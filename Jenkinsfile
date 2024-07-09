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

        stage('working directory & info') {
            steps {
                script {
                    powershell '''
                        python --version
                        whoami
                    '''
                }
            }
        }
        
        stage('Install dependencies') {
            steps {
                script {
                    powershell '''
                        python -m venv venv
                        ./venv/Scripts/Activate.ps1
                        pip install -r ./src/requirements.txt
                    '''
                }
            }
        }

//        stage('Build Docker image') {
//            steps {
//                script {
//                    // Costruisci l'immagine Docker
//                    powershell '''
//                        cd src
//                        docker build -t myapp:latest .
//                    '''
//                }
//            }
//        }

        stage('Run Docker container') {
            steps {
                script {
                    // Ferma e rimuove il contenitore Docker se esiste già
                    powershell '''
                        try {
                            docker stop myapp_container
                            docker rm myapp_container
                        } catch {
                            # Non eseguire alcuna azione
                        }
                    '''

                    // Avvia il contenitore Docker
                    powershell '''
                        echo daje
                        docker run -d -p 3000:3000 --name myapp_container myapp:latest
                        echo dajedaje
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
                    docker stop myapp_container -ErrorAction SilentlyContinue
                    docker rm myapp_container -ErrorAction SilentlyContinue
                '''
            }
        }
    }
}
