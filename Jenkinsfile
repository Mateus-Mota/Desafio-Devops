pipeline {
    agent any
    stages {
        stage('Stage 1 main') {
            when {
                branch 'refs/remotes/origin/main'
            }
            steps {
                echo "${some_ip}"
            }
        }
        stage('Stage 1 main 2') {
            when {
                branch 'main'
            }
            steps {
                echo "${some_ip}"
            }
        }
    }
}
