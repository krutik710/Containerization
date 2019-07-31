FROM ubuntu
RUN apt-get update \
    && apt-get install nginx -y \
    && echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx
ADD index.html /usr/share/nginx/html/
ADD default /etc/nginx/sites-available/
EXPOSE 80
CMD rm -rf /usr/share/nginx/html/index1.html && echo "<html><h1>$HOSTNAME</h1></html>" >> /usr/share/nginx/html/index1.html && service nginx start
