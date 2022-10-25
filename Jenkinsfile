pipeline {
    agent any
    stages {

        stage('Deploy') {
            steps {
                sh """
                   python -m venv .venv
                   source ./.env/bin/activate
                   python -m pip install -r requirements.txt
                   python -m pip install pytest pytest-cov coverage
                   """
            }
        }
    }
}