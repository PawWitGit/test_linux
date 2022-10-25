

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh """
                python -m venv .env
                source ./.env/bin/activate
                python -m pip install -r requirements.txt
                python -m pip install pytest pytest-cov coverage
                """
            }
        stage('Test') {
            steps {
                sh 'python app/test_main.py'
            }
        }

    }
}