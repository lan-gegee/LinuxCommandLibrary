# TAGLINE

管理 OCI/Docker 注册表认证

# TLDR

**列出**所有已配置的 OCI 注册表凭据

```apptainer registry list```

**登录** Docker 注册表

```apptainer registry login --username [user] docker://[docker.io]```

**登录** OCI 注册表，**密码从标准输入读取**

```apptainer registry login --username [user] --password-stdin oras://[registry.example.com]```

从注册表**登出**

```apptainer registry logout docker://[docker.io]```

使用自定义**认证文件登录**

```apptainer registry login --authfile [path/to/authfile.json] --username [user] docker://[registry.example.com]```

# SYNOPSIS

**apptainer registry** [_subcommand_] [_options_]

# PARAMETERS

**-c, --config** _string_
> 注册表配置文件的路径（默认 ~/.apptainer/remote.yaml）

**-h, --help**
> 显示 registry 命令的帮助信息

# DESCRIPTION

**apptainer registry** 管理通过 **docker://** 或 **oras://** 协议访问的独立 OCI/Docker 注册表的认证。它提供登录、登出以及列出已配置注册表凭据的子命令。

该命令将凭据与 Apptainer 的远程端点分开管理，可以直接向任何兼容 OCI 的注册表（如 Docker Hub、GitHub Container Registry 或私有注册表）进行认证。

# SUBCOMMANDS

**apptainer registry list**
> 显示所有已配置的 OCI 注册表凭据

**apptainer registry login**
> 向 OCI/Docker 注册表进行身份验证

**apptainer registry logout**
> 移除对 OCI/Docker 注册表的身份验证

# CAVEATS

注册表凭据默认存储在 Apptainer 配置文件 **~/.apptainer/remote.yaml** 中。该文件包含认证令牌，应妥善保管。通过 **apptainer registry** 配置的凭据与 **apptainer remote** 管理的凭据相互独立，后者负责 Sylabs Cloud 和库端点。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-push](/man/apptainer-push)(1), [apptainer-search](/man/apptainer-search)(1)
