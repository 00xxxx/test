pipeline {
    agent any
    tools {
        git 'Default' // Jenkins에서 설정한 Git 이름과 일치하도록 수정
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Git 레포지토리에서 코드 체크아웃
            }
        }
        stage('Build') {
            steps {
                echo 'Build Stage'
            }
        }
        // 추가적인 스테이지들...
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
