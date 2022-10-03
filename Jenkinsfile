pipeline {
    agent any
    
    stages {
        stage('Stage 1 main scripted') {
            steps {
                script {
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
                echo "${env.BRANCH_NAME}"
            }
        }
    }
}
