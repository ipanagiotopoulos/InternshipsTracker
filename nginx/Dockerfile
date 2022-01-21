FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
ADD static /appinternships/static
COPY default.conf /etc/nginx/conf.d
