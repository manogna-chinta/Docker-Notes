Containers can be created in two ways:
1. on the top of VMs
2. on the top of physical servers

Nowadays, people prefer to use model 2 because when you maintain the physical server, you have to deal with a lot. So there is a dedicated team for it (refer to pic 1).

### What is a Container?

A container is a collection of application + system dependencies + libraries.

### Why are Containers Lightweight in Nature?

Containers are lightweight because they don't have a complete operating system, and they use resources from the OS they are running on.

### Life Cycle of Docker

To create a Docker image and execute it to create a container, you need to write a Dockerfile. There is something called the Docker engine, which collects all the inputs. For example, to create an image from a Dockerfile, you use "build," and to create a container from an image, you use "run."

Docker is very much dependent on the Docker engine, which is prone to single points of failure and layers. To avoid this, you can use Buildah. In Buildah, you write a shell script and put all the Buildah commands in the script. This can create Docker images as it supports Docker.

Check out the [Docker Zero to Hero repository](https://github.com/manogna-chinta/Docker-Zero-to-Hero).

### Docker Daemon

The Docker daemon runs with the root user, and it's a monolithic process.

### Difference Between Entrypoint and CMD

Both "Entrypoint" and "CMD" are used to start the command when somebody runs Docker. However, "Entrypoint" is something that you cannot change, whereas "CMD" is configurable during runtime.

### What Is Multi-Stage Build?

Multi-stage build allows you to build your Docker container in multiple stages, allowing you to copy artifacts from one stage to another. The major advantage of this is to build lightweight containers.

Multistage builds are :
Multistage builds , distroless builds

A distroless image is a lightweight Docker image that contains only runtime environments. A big advantage of distroless images is security.

### A Production Issue with Docker

One of the production issues we faced with Docker was using Ubuntu base images, which were exposed to some vulnerabilities. So, we moved to distroless images. For example, if you are using a Python application, we moved to Python distroless images, which only have the Python runtime. It usually doesn't have utilities like "find," "ls," "curl." This provided us the highest level of security, and after implementing distroless images, we can say our application is not prone to any OS-related issues.

(Revise docker multi stage builds if needed)

### Containers Are Ephemeral

Containers are ephemeral, meaning they are short-lived. When the container is down, the log files also get deleted. To address this, Docker introduced:

1. Bind Mounts
2. Volumes
      				| --------- |
				|  -------  |
				|  |     |  |
				|  | C1  |  |
				|  |-----|  |
				|    Host   |
				|-----------|

Here C1 means container, The c1 contains some folder like manu and it can mount to any folder in the / in the app directory (/app) of host system and using bind mounts it can store the logs or any data

### Bind Mounts and Volumes

Both bind mounts and volumes are used to persist data beyond the lifecycle of a container.

Bind mounts allow a container to store data on the host system. They can be useful for storing logs or any data.

Volumes are a more versatile solution, as they offer better lifecycle management. You can manage everything on the CLI, and they allow you to use external sources like S3 to store data.

Docker Commands:
- `docker -v <command>`
- `docker --mount <command>`

Both commands are essentially the same, with only a syntax difference.

Docker Volume Commands:
- `docker volume create manu`
- `docker volume inspect manu`
- `docker volume rm manu`
- `docker volume rm manu renu`

Docker Build and Run Commands:
- `docker build -t myfirst-docker-file .`
- `docker volume create manu`
- `docker run -d --mount source=manu,target=/app nginx:latest`

Docker PS and Inspect Commands:
- `docker ps`
- `docker inspect <container-id>`
- `docker volume rm manu `

Error occurs,To remove a Docker volume, first stop the container that uses it and then delete the volume.

### Docker Networking

Docker uses bridge networking, with the Docker daemon and host having separate IP addresses. In general, veth (or docker0) is used to maintain communication between them. To avoid network issues, you can use custom bridge networks. Other network types include host networking and overlay networking.

- `docker network rm test`
- `docker run -d --name host-demo --network=host nginx:latest`
- `docker inspect host-demo`
It shows no IP address because it is binded to the host network itself.

**Difference between ADD and COPY:**

One major difference between `ADD` and `COPY` is that if you add a file in the .tar.gz format, it will be automatically unzipped in the created container when using `ADD`, whereas `COPY` doesn't have this feature. Additionally, `ADD` is used to copy files from a URL, while `COPY` is used to copy files from one container to the host system.



### Real-Time Challenges with Docker

1. Docker is a single demon process which can cause a single point of failure if the docker demon goes down for some reason, all the applications are down . The alternative for this is Podman. We can use the same commands like run build and all this. But the advantage of using pod man is it doesn't have single point of failure.

2. Docker demon runs as a root user, which is a security threat. Any process running as a root can have adverse effects. when it is compromised for security reason. It can impact other applications or containers on the host.

3. Resource Constraints if you are running too many containers on a single host, you may experience issues with resource constraints. This can result in slow performance or crashes.

**Steps to Secure Containers:**

1. **Use Minimal Images**: Consider using distroless or images with a minimal number of packages as your final image in a multistage build. This reduces the chances of CVEs (Common Vulnerabilities and Exposures) or security issues.

2. **Proper Networking Configuration**: Ensure that networking is configured properly. Misconfigured networking is a common source of security issues. If needed, configure custom bridge networks and assign them to isolate containers.

3. **Container Image Scanning**: Use utilities like `snyc` to scan your container images for vulnerabilities and security issues.

