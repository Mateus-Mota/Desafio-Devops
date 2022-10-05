pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        sonarToken = credentials('SonarQubeToken')
        dockerHome = tool 'docker'
    }
    stages {
        stage('Stage 1 main scripted') {
            steps {
                script {
                    checkout scm
                    def branchName = "${env.BRANCH_NAME}"
                    sh "echo ${branchName}"
                    sh "echo ${env.BRANCH_NAME}"
                    if (branchName ==~ 'origin/main') {
                        sh "echo ${GIT_BRANCH}"
                        sh "echo ${GIT_COMMITTER_NAME}" 
                    }
                }
            }
        }
        
        stage('Stage 2 main declarative') {
            when {
                branch 'main'
            }
            steps {
                checkout scm
                echo "${env.BRANCH_NAME}"
            }
        }
        
        stage('Build scripted') {
            steps{
                script{
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    sh "docker --version"
                    sh "echo ${dockerHome}"
                    sh "docker build -t desafio-devops-${env.BUILD_ID} --pull -f web/Dockerfile web"
                }
            }  
        }
    }
}
