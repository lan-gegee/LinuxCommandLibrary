# TAGLINE

管理 Apptainer 容器用户和组的 Linux capabilities

# TLDR

**列出授予特定用户的 capabilities**

```sudo apptainer capability list --user [username]```

**为用户授予一个 capability**

```sudo apptainer capability add --user [username] [CAP_NET_RAW]```

**从用户移除一个 capability**

```sudo apptainer capability drop --user [username] [CAP_NET_RAW]```

**为组授予所有 capabilities**

```sudo apptainer capability add --group [groupname] all```

**列出全部可用**的 Linux capabilities 及其说明

```apptainer capability avail```

**移除用户的全部 capabilities**

```sudo apptainer capability drop --user [username] all```

# SYNOPSIS

**apptainer capability** _subcommand_ [_options_]

# DESCRIPTION

**apptainer capability** 管理授予用户和组、供其在 Apptainer 容器内使用的 Linux capabilities。管理员使用此命令授权特定用户或组在容器运行时请求特定的 capabilities。

Capabilities 存储在 Apptainer 维护的 **capability.json** 文件中。授予 capability 并不会自动在容器内启用它——用户必须在运行时通过 **--add-caps** 标志显式请求已授予的 capabilities，配合 **apptainer exec** 或 **apptainer run** 等命令使用。

# SUBCOMMANDS

**add**
> 为用户或组授予一个或多个 Linux capabilities。需要 root 权限。

**drop**
> 从用户或组撤销一个或多个 Linux capabilities。需要 root 权限。

**list**
> 显示当前分配给用户或组的 capabilities。

**avail**
> 显示所有可识别的 Linux capabilities 及其简要说明。

# PARAMETERS

**--user** _name_
> 针对 add、drop 或 list 操作指定目标用户。

**--group** _name_
> 针对 add、drop 或 list 操作指定目标组。

# CAVEATS

向用户授予 Linux capabilities 通常等同于授予主机系统的 root 级访问权限。大多数 capabilities 都能让用户突破容器并提升权限。此功能面向受信任的环境，而非多租户 HPC 集群。**add** 和 **drop** 都接受大小写不敏感的关键字 **all**，可一次性对所有可用的 capabilities 进行操作。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-run](/man/apptainer-run)(1), [capabilities](/man/capabilities)(7)
