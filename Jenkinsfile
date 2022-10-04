pipeline {
    agent any
    
    options {
        skipDefaultCheckout(true)
    }
    environment {
        sonarToken = credentials('SonarQubeToken')
    }
    stages {
        stage('Stage 1 main scripted') {
            steps {
                script {
                    checkout scm
                    def branchName = "${env.BRANCH_NAME}"
                    if (branchName ==~ 'main') {
                        sh "echo ${GIT_BRANCH}"
                        sh "echo ${GIT_COMMITTER_NAME}" 
                        sh "echo ${branchName}"
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
    }
}
