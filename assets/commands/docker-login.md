# TAGLINE

向 Docker 镜像仓库进行身份验证

# TLDR

**登录 Docker Hub**，使用设备码流程

```docker login```

**登录 Docker Hub**，指定用户名（会提示输入密码）

```docker login -u [username]```

**登录特定的**镜像仓库

```docker login [registry.example.com]```

**非交互式登录**，密码通过 stdin 提供

```echo [token] | docker login -u [username] --password-stdin```

**登录 GitHub** Container Registry

```echo [PAT] | docker login ghcr.io -u [username] --password-stdin```

# SYNOPSIS

**docker** **login** [_options_] [_server_]

# PARAMETERS

**-u**, **--username** _string_
> 用户名。

**-p**, **--password** _string_
> 密码或个人访问令牌（不安全，建议使用 --password-stdin）。

**--password-stdin**
> 从 stdin 读取密码。

# DESCRIPTION

**docker login** 用于向 Docker 镜像仓库进行身份验证。未指定服务器时，除非提供了 --username，否则默认使用设备码流程向 Docker Hub 验证身份。凭据存储在 ~/.docker/config.json 中，或在已配置的情况下存储在外部凭据管理器（如操作系统原生钥匙串）中。推送镜像和访问私有软件仓库都需要先进行身份验证。

# CONFIGURATION

**~/.docker/config.json**
> 存储镜像仓库凭据和身份验证令牌。在可用时使用凭据辅助工具进行安全存储。

# CAVEATS

使用 -p 会把密码暴露在 shell 历史记录和日志文件中。脚本化登录时务必使用 --password-stdin。

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

[docker-pull](/man/docker-pull)(1), [docker-build](/man/docker-build)(1)
