# TAGLINE

多容器 Docker 编排

# TLDR

**启动**服务

```docker-compose up```

**后台启动**

```docker-compose up -d```

**停止**服务

```docker-compose down```

**查看**日志

```docker-compose logs```

**构建**服务

```docker-compose build```

**列出**容器

```docker-compose ps```

# SYNOPSIS

**docker-compose** [_options_] _command_

# DESCRIPTION

**docker-compose** 是一个通过 YAML 配置文件来定义和运行多容器 Docker 应用的工具。Compose 让你在单个 docker-compose.yml 文件中声明整个应用栈，而不必用复杂的标志管理多条 docker run 命令。

该工具负责服务编排、网络、卷管理以及容器间的依赖关系。它会自动为应用创建隔离的网络，通过 depends_on 指令管理启动顺序，并提供便捷命令用于查看日志、执行命令和管理应用的完整生命周期。

Docker Compose 对本地开发环境至关重要——当应用需要多个服务（Web 服务器、数据库、缓存、队列）时尤其如此。它保证了开发团队之间的一致性，并简化了从开发到生产环境的过渡。现代 Docker 将 Compose V2 作为原生插件提供（docker compose），取代独立的 docker-compose 命令。

# PARAMETERS

**up** [**-d**]
> 创建并启动容器

**down**
> 停止并移除容器、网络

**build**
> 构建或重新构建服务

**start**
> 启动服务

**stop**
> 停止服务

**restart**
> 重启服务

**ps**
> 列出容器

**logs** [**-f**]
> 查看容器的输出

**exec** _service_ _command_
> 在运行中的容器内执行命令

**pull**
> 拉取服务镜像

**config**
> 校验并查看 compose 文件

# DOCKER-COMPOSE.YML

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db/myapp
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

# WORKFLOW

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and start
docker-compose up --build

# Execute command
docker-compose exec web bash

# Run one-off command
docker-compose run web npm test

# Scale service
docker-compose up --scale worker=3
```

# COMMON OPERATIONS

```bash
# Check status
docker-compose ps

# Pull latest images
docker-compose pull

# View configuration
docker-compose config

# Remove volumes
docker-compose down -v

# Restart single service
docker-compose restart web

# View logs for service
docker-compose logs -f web

# Execute in service
docker-compose exec db psql -U postgres
```

# FEATURES

- 多容器编排
- 网络隔离
- 卷管理
- 环境变量处理
- 服务依赖
- 健康检查
- 资源限制

# FILE LOCATIONS

默认文件名（按顺序）：
1. docker-compose.override.yml
2. docker-compose.yml

自定义文件：
```bash
docker-compose -f custom-compose.yml up
```

# CONFIGURATION

**docker-compose.yml**
> 定义服务、网络、卷及其关系的主配置文件。放置在项目根目录。

**docker-compose.override.yml**
> 可选的覆盖文件，与 docker-compose.yml 一起自动加载，便于在不修改主文件的情况下进行本地定制。

**.env**
> 由 Docker Compose 自动加载的环境变量文件，用于填充 compose 文件中的变量替换。

# CAVEATS

不适用于生产环境编排（请使用 Kubernetes）。文件格式版本很重要。环境变量需要正确加引号。网络隔离可能增加调试难度。存在卷权限问题。注意 Compose V2（docker compose）与 V1（docker-compose）的差异。

# HISTORY

**docker-compose** 由 Orchard Labs（后被 Docker 收购）于 **2014 年**前后以 Fig 的名义创建，后来成为 Docker Compose，并成为 Docker 开发工作流的重要组成部分。

# INSTALL

```apt: sudo apt install docker-compose```

```dnf: sudo dnf install docker-compose```

```pacman: sudo pacman -S docker-compose```

```apk: sudo apk add docker-cli-compose```

```zypper: sudo zypper install docker-compose```

```brew: brew install docker-compose```

```nix: nix profile install nixpkgs#docker-compose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [kubectl](/man/kubectl)(1), [podman-compose](/man/podman-compose)(1)
