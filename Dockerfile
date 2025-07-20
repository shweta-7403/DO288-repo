# Base image
FROM nginx:alpine

# Copy your app into nginx default location
COPY . /usr/share/nginx/html

# Expose port 8080 instead of 80 (optional)
EXPOSE 8080

# Optional: Run nginx in foreground (but nginx base image already handles it)
CMD ["nginx", "-g", "daemon off;"]
