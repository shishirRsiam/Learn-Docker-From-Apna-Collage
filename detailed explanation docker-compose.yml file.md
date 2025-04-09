Here's a detailed explanation of the key directives and commands you can use in a `docker-compose.yml` file to configure and manage Docker containers.

### 1. **version**
Defines the version of Docker Compose being used. This version should be compatible with your Docker installation.

- **Example**:
  ```yaml
  version: '3'
  ```

- **Purpose**: Specifies which Docker Compose file format to use. Different versions support different features.

### 2. **services**
Defines the services (containers) that will be part of your application. Each service runs a separate container.

- **Example**:
  ```yaml
  services:
    web:
      image: nginx
      ports:
        - "8080:80"
  ```

- **Purpose**: Groups multiple containers into a service. Each service can be configured with its own image, build context, ports, volumes, etc.

### 3. **image**
Specifies the Docker image to use for the container. It can be a pre-built image from Docker Hub or a custom image you’ve built.

- **Example**:
  ```yaml
  image: node:14
  ```

- **Purpose**: If you’re using an image from Docker Hub or a custom registry, use this option to specify which image to use for the service. You can also specify the version or tag of the image.

### 4. **build**
Defines how to build the Docker image from a directory. It can be used instead of the `image` directive when you need to build the image from your local context (e.g., Dockerfile).

- **Example**:
  ```yaml
  build:
    context: .
    dockerfile: Dockerfile
  ```

- **Purpose**: Tells Docker Compose to build the image from the given directory (`context`) and optionally a specific Dockerfile.

### 5. **container_name**
Sets a custom name for the container. By default, Docker generates a random name.

- **Example**:
  ```yaml
  container_name: myapp_container
  ```

- **Purpose**: This allows you to explicitly name the container, which can make it easier to reference or manage.

### 6. **ports**
Maps the container’s internal ports to the host machine’s ports. It allows external traffic to reach your containerized app.

- **Example**:
  ```yaml
  ports:
    - "8080:80"
  ```

- **Purpose**: Exposes container ports to the host. The format is `host_port:container_port`. This means traffic on `host_port` is forwarded to `container_port` inside the container.

### 7. **volumes**
Defines shared directories between the host machine and the container or between containers themselves.

- **Example**:
  ```yaml
  volumes:
    - .:/usr/src/app
  ```

- **Purpose**: Allows you to persist data or synchronize files between the host and the container. Useful for development when you want changes made on the host to be reflected in the container instantly.

### 8. **environment**
Defines environment variables for the service, which are available inside the container.

- **Example**:
  ```yaml
  environment:
    - NODE_ENV=production
    - DB_HOST=db.example.com
  ```

- **Purpose**: Passes environment variables to the container. This is helpful for setting configuration options like API keys or environment-specific settings.

### 9. **command**
Overrides the default command that is executed when the container starts.

- **Example**:
  ```yaml
  command: bash -c "npm install && node server.js"
  ```

- **Purpose**: Runs a custom command when the container starts, overriding the default entrypoint.

### 10. **depends_on**
Defines dependencies between services. It ensures that one service starts before another.

- **Example**:
  ```yaml
  depends_on:
    - db
  ```

- **Purpose**: This ensures that the specified service (like a database) is started before the dependent service.

### 11. **networks**
Specifies which networks the container should be connected to. This allows you to control how different containers communicate with each other.

- **Example**:
  ```yaml
  networks:
    - my-network
  ```

- **Purpose**: This is useful for defining isolated networks that services can connect to, and it helps in controlling service communication.

### 12. **restart**
Specifies the restart policy for the container in case it crashes or stops.

- **Example**:
  ```yaml
  restart: always
  ```

- **Purpose**: Defines the restart behavior for the container. Common values are:
  - `no` (default): Don’t restart the container if it stops.
  - `always`: Restart the container if it stops.
  - `on-failure`: Restart the container only if it exits with a non-zero status.
  - `unless-stopped`: Always restart unless the container is manually stopped.

### 13. **build context (context, dockerfile)**
These are used in conjunction with the `build` directive. The `context` refers to the directory used as the build context, and `dockerfile` specifies the path to the Dockerfile if it’s different from the default.

- **Example**:
  ```yaml
  build:
    context: .
    dockerfile: Dockerfile.dev
  ```

- **Purpose**: Defines the path to the build context and Dockerfile for building an image.

### 14. **secrets**
Defines secrets for sensitive data such as passwords or API keys.

- **Example**:
  ```yaml
  secrets:
    - my_secret_key
  ```

- **Purpose**: Used for securely passing sensitive data to the container. Docker stores secrets in a secure, encrypted way.

### 15. **healthcheck**
Defines a command to check if the container is healthy (e.g., checking if an app is still responding).

- **Example**:
  ```yaml
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:80"]
    interval: 30s
    retries: 3
    start_period: 10s
    timeout: 5s
  ```

- **Purpose**: Allows you to define a health check for the container. If the health check fails, Docker can automatically restart the container or notify you.

### 16. **user**
Defines the user the container should run as. This can help ensure that the container runs with the appropriate permissions.

- **Example**:
  ```yaml
  user: "1000:1000"
  ```

- **Purpose**: Specifies the user ID (UID) and group ID (GID) the container should use.

### 17. **logging**
Defines how logs from a container should be handled. You can specify log drivers and options for container logs.

- **Example**:
  ```yaml
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
  ```

- **Purpose**: Allows you to control how Docker handles logs for your containers.

### 18. **build arguments (args)**
Sets build arguments that can be passed during the image build process.

- **Example**:
  ```yaml
  build:
    context: .
    args:
      NODE_ENV: production
  ```

- **Purpose**: Passes build-time arguments to the Docker build process, which can be used in the `Dockerfile`.

---

### Example Full `docker-compose.yml`:

```yaml
version: '3'

services:
  web:
    image: node:14
    container_name: myapp_container
    working_dir: /usr/src/app
    volumes:
      - .:/usr/src/app
    environment:
      - NODE_ENV=production
    ports:
      - "8080:80"
    command: bash -c "npm install && node server.js"
    restart: always
    depends_on:
      - db

  db:
    image: postgres:latest
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - my-network

volumes:
  db_data:

networks:
  my-network:
    driver: bridge
```

### Summary:

- **`version`**: Specifies the version of Docker Compose format.
- **`services`**: Defines individual services (containers) that are part of your app.
- **`image` / `build`**: Defines the image to use or the build process for the service.
- **`command`**: Overrides the default behavior and specifies what to run inside the container.
- **`ports`**: Exposes ports for communication with the outside world.
- **`volumes`**: Syncs files between the host and the container.
- **`networks`**: Defines network configurations for communication between containers.
- **`restart`**: Defines restart policies for your containers.
- **`environment`**: Sets environment variables inside the container.

This should give you a comprehensive overview of the most common `docker-compose.yml` commands and how to use them!