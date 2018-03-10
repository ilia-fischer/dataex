FROM centos:nodejs

ENV DATAEX_HOME="/opt/dataex" 

ADD dataex /opt/dataex
COPY start.sh /opt/dataex/

WORKDIR /opt/dataex
RUN npm install

EXPOSE 3001
ENTRYPOINT ["/opt/dataex/start.sh"]