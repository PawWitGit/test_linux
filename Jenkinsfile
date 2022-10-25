

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'poetry update'
            }
        stage('Test') {
            steps {
                sh 'python app/test_main.py'
            }
        }

    }
}