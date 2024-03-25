FROM gi-docker.docker.artifactory.viasat.com/viasat-centos7

# In user:password syntax
ARG ARTIFACTORY_CREDS
ARG ARTIFACTORY_URL=https://artifactory.viasat.com/artifactory
ARG ARTIFACTORY_REPO=nbn_nms-gen-dev

ARG GO_VERSION=go1.15.3
ARG GO_TARBALL=${GO_VERSION}.linux-amd64.tar.gz
ARG GO_URL=https://dl.google.com/go/${GO_TARBALL}
ENV GOROOT=/usr/local/go
ENV GOPATH=/root/go
ENV PATH="${GOPATH}/bin:${GOROOT}/bin:${PATH}"

RUN yum -y install rpm-build
RUN yum -y install rpm-sign
RUN yum -y install expect
RUN yum -y install git

# Install GO
RUN curl -L -o /tmp/${GO_TARBALL} ${GO_URL}
RUN stat /tmp/${GO_TARBALL}
RUN cd /tmp; tar -xzf ${GO_TARBALL}
RUN mv /tmp/go ${GOROOT}
RUN go version

# Install github-release using go
RUN go get github.com/github-release/github-release
RUN github-release --version

#CMD ["/bin/bash"]
