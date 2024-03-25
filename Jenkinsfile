library identifier: 'jenkins_shared_libs@master', retriever: modernSCM(
  [$class: 'GitSCMSource',
   remote: 'https://git.viasat.com/NBNNMS/jenkins_shared_libs.git',
   credentialsId: 'NBNBuildNMSGHPersonalAccessToken'])

pipeline {
    // Agent is defined below because we cannot pass credentials to top-level agent 
  agent none
  parameters {
    booleanParam(name: 'IS_RELEASE', defaultValue: false, description: 'If checked, will push release to github and production artifactory RPM repository')
    booleanParam(name: 'SKIP_BUILD', defaultValue: false, description: 'If checked, will skip build process and will immediately do the test stage')
  }
  environment {
    ARTIFACTORY_CRED_ID = 'NBNBuildNMS_Artifactory_API_key'
    ARTIFACTORY_CREDS = credentials("${ARTIFACTORY_CRED_ID}")
    ARTIFACTORY_PATH = 'artifactory.viasat.com/artifactory'
    ARTIFACTORY_URL = "https://${ARTIFACTORY_PATH}"
    ARTIFACTORY_RPM_REPO_DEV = 'nbn-nms-rpm-dev'
    ARTIFACTORY_RPM_REPO_PROD = 'nbn-nms-rpm-prod'
    RPM_KEY_CRED_ID = 'NBN_NMS_RPM_SIGN_KEY'
    RPM_KEY = credentials("${RPM_KEY_CRED_ID}")
    GITHUB_CREDS = credentials('NBNBuildNMSGHPersonalAccessToken')
    GITHUB_TOKEN = "${GITHUB_CREDS_PSW}"
    GITHUB_API = 'https://git.viasat.com/api/v3'
    GITHUB_REPO = 'nms-omnibus'
    GITHUB_ORG = 'NBNNMS'
    GITHUB_REPO_URL = "git.viasat.com/${GITHUB_ORG}/${GITHUB_REPO}.git"
    BUILD_JOB_NAME = "${GITHUB_ORG}::${GITHUB_REPO}"
    RPM_VERSION = '5.0.0.5'
    SPEC_FILE = "docker_build/nms-omnibus.spec"
    RPMSIGN_EXPECT = "docker_build/rpmsign.expect"
    RPM_VERSION_BUILD = "${env.RPM_VERSION}-${env.BUILD_NUMBER}"
    RPMBUILD_DEFINES = '--define "placeholder value"'
    RPM_NAME = 'nms-omnibus'
    RPM_FULL_NAME = "${env.RPM_NAME}-${RPM_VERSION_BUILD}"
  }
  stages {
    stage('Build with docker image') {
      when { expression { !params.SKIP_BUILD } }
      agent {
        dockerfile {
          dir "docker_build"
          additionalBuildArgs "--build-arg ARTIFACTORY_CREDS=${ARTIFACTORY_CREDS}"
          args '-u root -v /home/jenkins/.gnupg:/root/.gnupg:z'
        }
      }
      stages {
        stage('Build') { 
          steps {
            script {
              nmsRpmAndSign()
            }
          }
        }
      }
      post {
        success {
          nmsArchiveArtifacts()
          cleanWs()
        }
      }
    }
    stage('Deploy in GMTL') {
      matrix {
        agent { label 'nms-dev.openstack-build-agents.viasat.io' }
        axes {
          axis {
            name 'GMTL_HOST'
            values 'nmsfms04', 'nmsfms06', 'nmsfmscol02', 'nmstools01'
          }
        }
        stages {
          stage('Deploy') {
            steps {
              sshagent (credentials: ['nmsjenkins']) {
                sh """ssh -o StrictHostKeyChecking=no -J nmsjenkins@d01-jumpdclin01.gtb.viasat.com nmsjenkins@${GMTL_HOST}.gmtl.viasat.com \
                        "sudo yum makecache; \
                         sudo yum install -y --rpmverbosity=debug nms-omnibus-${env.RPM_VERSION_BUILD}" """
              }
            }
          }
        }
      }
    }
  }
  options {
    // Artifacts here are large, so only keep up to 5
    buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
  }
  post {
    always {
      nmsNotifications()
    }
  }
}
