pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        dockerHome = tool 'docker'
    }
    stages {
        stage('Checkout scm scripted') {
            steps {
                script {
                    checkout scm
                    def branchName = "${env.GIT_BRANCH}"
                    if (branchName ==~ 'origin/main') {
                        sh "echo ${GIT_BRANCH}"
                    if (branchName ==~ 'origin/jenkins-tests') {
                        sh "echo ${GIT_BRANCH}"
                    }
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
