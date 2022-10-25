pipeline {
  agent
  stages {
    stage('Initialise') {
      steps {
        stepInitialise()
        stepPythonConfigure()
      }
    }
    stage('Install Dependencies') {
      steps {
        sh """
          python -m venv .env
          source ./.env/bin/activate
          python -m pip install -r requirements.txt
          python -m pip install pytest pytest-cov coverage
          """
        }
      }
    }
 }