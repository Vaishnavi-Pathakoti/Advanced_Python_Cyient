pipeline{
  agent any
  environment{
    APP_URL='http://127.0.0.1:5001'
  }
  stages{
    stage('Checkout'){
      strps{
        echo 'Fetching Projectt from GitHub'
        checkout scm
      }
    }
    stage('Install Dependencies'){
      steps{
        bat 'python -m pip install -r reqirement.txt
      }
    }
    stage('Start Flask Application'){
      steps{
          bat 'start "FlaskApp"  /B python app.py'
      }
    }
    stage('Execute API tests'){
      steps{
        bat 'python -m robot test_2.robot'
      }
    }
  }
