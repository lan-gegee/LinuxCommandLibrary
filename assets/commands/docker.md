# TAGLINE

用于应用部署的容器平台

# TLDR

**运行**容器

```docker run [image]```

**列出**容器

```docker ps```

**构建**镜像

```docker build -t [name] [.]```

**拉取**镜像

```docker pull [image]```

**停止**容器

```docker stop [container]```

**删除**容器

```docker rm [container]```

在容器中**执行**命令

```docker exec -it [container] [bash]```

# SYNOPSIS

**docker** _command_ [_options_]

# DESCRIPTION

**docker** 是一个用于开发、交付和以容器方式运行应用的平台。容器将应用程序及其依赖打包成标准化单元，确保从开发到生产的不同环境之间的一致性。

Docker 解决了"在我机器上能跑"的问题，从而彻底改变了应用部署和开发工作流。它使用操作系统级虚拟化来隔离应用，使其可移植、高效且易于伸缩。容器共享主机内核，但保持隔离的文件系统、进程和网络。

Docker 生态系统包括 Docker Engine（运行时）、Docker Hub（镜像仓库）以及一套用于管理容器、镜像、网络和卷的完整 CLI。Docker 镜像采用分层构建，便于高效分发和更新。该平台既支持单容器应用，也支持复杂的多服务架构。

# PARAMETERS

**run** [_options_] _image_
> 创建并启动容器

**ps** [**-a**]
> 列出容器

**build** **-t** _name_ _path_
> 从 Dockerfile 构建镜像

**pull** _image_
> 从镜像仓库拉取镜像

**push** _image_
> 将镜像推送到镜像仓库

**exec** _container_ _command_
> 在运行中的容器中执行命令

**logs** _container_
> 获取容器日志

**stop** _container_
> 停止运行中的容器

**start** _container_
> 启动已停止的容器

**rm** _container_
> 删除容器

**rmi** _image_
> 删除镜像

**images**
> 列出镜像

# RUN OPTIONS

**-d**, **--detach**
> 在后台运行

**-it**
> 交互模式并分配 TTY

**-p** _host_**:**_container_
> 发布端口

**-v** _host_**:**_container_
> 挂载卷

**--name** _name_
> 为容器指定名称

**-e** _var_**=**_value_
> 设置环境变量

**--rm**
> 退出时自动删除

**--network** _network_
> 连接到网络

# WORKFLOW

```bash
# Run container
docker run -d -p 80:80 --name webserver nginx

# Interactive container
docker run -it ubuntu bash

# With environment variables
docker run -e DATABASE_URL=postgres://... myapp

# With volume mount
docker run -v $(pwd):/app -w /app node npm install

# Build image
docker build -t myapp:latest .

# Push to registry
docker tag myapp:latest user/myapp:latest
docker push user/myapp:latest

# View logs
docker logs -f container_name

# Execute command
docker exec -it container_name bash

# Clean up
docker stop container_name
docker rm container_name
docker rmi image_name
```

# DOCKERFILE

```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

# COMMON OPERATIONS

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# List images
docker images

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# System-wide cleanup
docker system prune -a

# Inspect container
docker inspect container_name

# Container stats
docker stats
```

# CONFIGURATION

**/etc/docker/daemon.json**
> Docker 守护进程配置，包括存储驱动、日志、镜像仓库加速器和资源限制。

**~/.docker/config.json**
> 用户级配置，包括镜像仓库身份验证、默认命令设置和 CLI 偏好。

# CAVEATS

需要 Docker 守护进程处于运行状态。需要 root 权限或 docker 组成员身份。网络配置可能比较复杂。卷权限问题常见。镜像可能很大。生产环境需考虑安全问题。在不同操作系统上行为有所差异。

# HISTORY

**Docker** 由 Solomon Hykes 于 **2013 年**在 dotCloud 创建，随后开源并彻底改变了应用容器化领域。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [podman](/man/podman)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Homepage](https://www.docker.com/)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
