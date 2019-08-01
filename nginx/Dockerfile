FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf \
    && rm /etc/nginx/nginx.conf
    
COPY ["site_dev.conf", "/etc/nginx/conf.d/"]
COPY ["site_prod.conf", "/etc/nginx/conf.d/"]
COPY ["nginx.conf", "/etc/nginx/"]
