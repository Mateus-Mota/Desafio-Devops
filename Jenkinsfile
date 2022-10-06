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
                    def branchName = "${env.GIT_BRANCH}"
                    sh "echo ${GIT_BRANCH}"
                    if (branchName == 'origin/main') {
                        sh "echo ${GIT_BRANCH}"
                    }
                    if (branchName == 'origin/jenkins-tests') {
                        sh "echo ${GIT_BRANCH}"
                    }
                }
            }
        }
        
        stage ('Code Analysis') {
            steps {
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
