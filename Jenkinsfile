pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello, Jenkins!'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // GitHub 리포지토리에서 코드 가져오기
                checkout scm
            }
        }

        stage('Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '--scan .',
                                odcInstallation: 'Default' // Jenkins에 구성된 Dependency-Check 설치 이름
            }
        }

        stage('Results') {
            steps {
                // Dependency-Check 결과 보기 (보고서를 콘솔에 출력하거나 파일로 확인)
                echo 'Dependency-Check analysis complete. Review the results for potential vulnerabilities.'
            }
        }
    }
}
