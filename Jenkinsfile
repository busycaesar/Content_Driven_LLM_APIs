pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        git(url: 'https://github.com/busycaesar/Content_Driven_LLM_APIs', branch: 'Jenkins')
      }
    }

    stage('build docker image') {
      steps {
        sh 'sudo docker build -t busycaesar/content_driven_llm_apis:jenkins .'
      }
    }

  }
}