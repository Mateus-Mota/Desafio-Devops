pipeline {
    agent any
    stages {
        stage('Stage 1 main') {
            when {
                branch 'main'
            }
            steps {
                sh "echo ${GIT_BRANCH}"
                sh "${GIT_COMMITTER_NAME}" 
            }
        }
        stage('Stage 1 main 2') {
            when {
                branch 'jenkins_test'
            }
            steps {
                echo "${some_ip}"
            }
        }
    }
}
