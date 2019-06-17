ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG C.UTF-8

RUN apk add --no-cache python3
RUN pip3 install requests
 
# Copy data for add-on
COPY addon_monitor.py /
COPY run.sh /

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
