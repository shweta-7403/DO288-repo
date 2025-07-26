FROM ubi9:micro

WORKDIR /opt/app

# Copy node binary from build image
COPY --from=my-node-builder /usr/bin/node /usr/bin/node
COPY --from=my-node-builder /usr/lib64 /usr/lib64
COPY --from=my-node-builder /lib64 /lib64

# Copy app source + node_modules
COPY --from=my-node-builder /opt/app /opt/app

USER 1001

ENV PORT=8080
EXPOSE 8080

CMD ["node", "app.js"]
