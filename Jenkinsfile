pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') {
            steps {
                pytest 'app/test_main.py'
            }
        }

    }
}