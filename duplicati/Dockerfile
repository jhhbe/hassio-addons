FROM lsiobase/mono:arm32v7-LTS

# set version label
ARG BUILD_DATE
ARG VERSION
ARG DUPLICATI_RELEASE
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"
LABEL maintainer="sparklyballs"

# environment settings
ENV HOME="/data"
ENV PUID=0
ENV PGID=0

RUN \
 echo "**** install jq ****" && \
 apt-get update && \
 apt-get install -y \
	jq && \
 echo "**** install duplicati ****" && \
 if [ -z ${DUPLICATI_RELEASE+x} ]; then \
	DUPLICATI_RELEASE=$(curl -sX GET "https://api.github.com/repos/duplicati/duplicati/releases" \
	| jq -r 'first(.[] | select(.tag_name | contains("beta"))) | .tag_name'); \
 fi && \
 mkdir -p \
	/app/duplicati && \
  duplicati_url=$(curl -s https://api.github.com/repos/duplicati/duplicati/releases/tags/"${DUPLICATI_RELEASE}" |jq -r '.assets[].browser_download_url' |grep zip |grep -v signatures) && \
 curl -o \
 /tmp/duplicati.zip -L \
	"${duplicati_url}" && \
 unzip -q /tmp/duplicati.zip -d /app/duplicati && \
 echo "**** cleanup ****" && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 8099
VOLUME /data

RUN apt-get update
RUN apt-get install -y python-pip
# install .py script dependency
RUN pip install inotify
# Copy data for add-on
COPY zbackup.py /
COPY run.sh /

RUN chmod a+x /run.sh
#
CMD [ "/run.sh" ]
