

pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage("test PythonEnv") {

            withPythonEnv('python3') {
            sh 'pip install pytest'
            sh 'pytest mytest.py'
        }
    }
}



