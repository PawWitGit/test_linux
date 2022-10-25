pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            steps {
                sh 'make Jenkins/app/test_main.py'
            }
        }

    }
}