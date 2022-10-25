pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            steps {
                sh 'python -m pytest app/test_main.py'
            }
        }

    }
}