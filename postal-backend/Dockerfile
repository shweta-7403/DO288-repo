# ---------- Stage 1: Build node_modules ----------
FROM registry.access.redhat.com/ubi9/nodejs-18 AS builder

# Use root to avoid EACCES during npm install
USER 0
WORKDIR /opt/app

COPY . .

# Install dependencies (no dev-deps)
RUN npm install --omit=dev

# ---------- Stage 2: Final image with UBI9-Micro ----------
FROM registry.access.redhat.com/ubi9/ubi-micro:9.3

# Set working dir
WORKDIR /opt/app

# Copy node binary from builder
COPY --from=builder /usr/bin/node /usr/bin/node
COPY --from=builder /usr/lib64 /usr/lib64
COPY --from=builder /lib64 /lib64

# Copy app and installed node_modules
COPY --from=builder /opt/app /opt/app

# Run as non-root (OpenShift-safe)
USER 1001

# Expose port
ENV PORT=8080
EXPOSE 8080

# Start app
CMD ["node", "app.js"]
