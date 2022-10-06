pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        sonarToken = credentials('SonarQubeToken')
        dockerHome = tool 'docker'
        scannerHome = tool 'SonarQubeScanner'
    }
    stages {
        stage('Checkout scm scripted') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        
        stage ('Code Analysis') {
            steps {
                scannerHome = tool 'SonarQubeScanner'
                withSonarQubeEnv('SonarQube') {
                    sh '${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=${sonarProjectName} \
                    -Dsonar.sources=./web \
                    -Dsonar.exclusions=.*,Dockerfile,*.md,*.yml,*.conf \
                    -Dsonar.host.url=https://0.0.0.0:3000 \
                    -Dsonar.login=${sonarToken}'
                }
            }
        }
        
        stage('Build scripted') {
            steps{
                script{
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    sh "docker --version && echo $USER"
                    sh "docker build -t desafio-devops-${env.BUILD_ID} --pull -f web/Dockerfile web"
                }
            }  
        }
    }
}
