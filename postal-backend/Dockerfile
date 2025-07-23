FROM ubi9-micro

USER 1001
WORKDIR /opt/app

# Copy static nginx from builder
COPY --from=builder sbin/nginx /nginx

# Copy static HTML
COPY html/ /nginx/html/

EXPOSE 8080

CMD ["/nginx/sbin/nginx", "-g", "daemon off;"]
