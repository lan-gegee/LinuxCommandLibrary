# TAGLINE

向容器 registry 进行身份验证

# TLDR

**登录 Docker Hub**

```podman login docker.io```

**登录特定 registry**

```podman login [registry.example.com]```

**使用凭据登录**

```podman login -u [username] -p [password] [registry]```

**通过 stdin 传入密码登录**

```echo [password] | podman login -u [user] --password-stdin [registry]```

**查看已登录的用户**（针对某个 registry）

```podman login --get-login [registry]```

**使用 TLS 客户端证书登录**

```podman login --cert-dir [/path/to/certs] [registry]```

# SYNOPSIS

**podman** **login** [_options_] _registry_

# PARAMETERS

**-u**, **--username** _name_
> registry 用户名。

**-p**, **--password** _pass_
> registry 密码。

**--password-stdin**
> 从 stdin 读取密码。

**--tls-verify**
> 联系 registry 时要求 HTTPS 并校验 TLS 证书（默认：**true**）。

**--authfile** _file_
> 身份验证文件的路径（默认：`${XDG_RUNTIME_DIR}/containers/auth.json`）。

**--cert-dir** _path_
> 使用 _path_ 处的 TLS 证书（*.crt、*.cert、*.key）连接 registry。

**--compat-auth-file** _path_
> 以 Docker 兼容格式将凭据写入 _path_。

**--get-login**
> 返回该 registry 的已登录用户。未找到登录信息时返回错误。

**--secret** _name_
> 从 podman secret 中读取密码。

**-v**, **--verbose**
> 打印关于凭据存储的详细信息。

# DESCRIPTION

**podman login** 向容器 registry 进行身份验证。凭据存储在 auth 文件中（默认：`${XDG_RUNTIME_DIR}/containers/auth.json`），供后续拉取和推送使用。如果未指定 registry，则使用 `registries.conf` 中 `[registries.search]` 下的第一个 registry。

支持 Docker Hub、Quay.io、GitHub Container Registry 以及私有 registry。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [podman-pull](/man/podman-pull)(1), [docker-login](/man/docker-login)(1)
