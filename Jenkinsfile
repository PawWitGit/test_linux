pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            steps {
                sh 'pytest app/test_main.py'
            }
        }

    }
}