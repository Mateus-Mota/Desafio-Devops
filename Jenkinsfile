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
                cleanWs()
                checkout scm
            }
        }
        
        stage ('Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '${scannerHome}/bin/sonar-scanner \
                    -Dsonar.projectKey=${sonarProjectName} \
                    -Dsonar.sources=./web \
                    -Dsonar.exclusions=.*,Dockerfile,*.md,*.yml,*.conf \
                    -Dsonar.host.url=http://172.17.128.1:9000 \
                    -Dsonar.login=${sonarToken}'
                    println "${env.SONAR_HOST_URL}"
                    println "${env.SONAR_CONFIG_NAME}"
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
