# TAGLINE

用于仓库访问的简单 Git 协议服务器

# TLDR

**启动 Git 守护进程**

```git daemon --base-path=[/path/to/repos]```

**启用 upload-pack**

```git daemon --enable=upload-pack --base-path=[/repos]```

**允许推送**

```git daemon --enable=receive-pack --base-path=[/repos]```

**在前台运行**

```git daemon --verbose --base-path=[/repos]```

**导出所有目录**

```git daemon --export-all --base-path=[/repos]```

# SYNOPSIS

**git** **daemon** [_options_] [_directory_...]

# PARAMETERS

**--base-path** _path_
> 仓库的基础路径。

**--export-all**
> 导出所有仓库。

**--enable** _service_
> 启用服务。

**--disable** _service_
> 禁用服务。

**--port** _port_
> 监听端口（默认 9418）。

**--listen** _host_
> 监听地址。

**--verbose**
> 记录详细日志。

**--inetd**
> 由 inetd 运行。

# DESCRIPTION

**git daemon** 基于 git:// 协议提供一个简单轻量的 Git 仓库服务器。它默认启用对仓库的匿名只读访问，写入访问则需要显式开启，适合公共仓库托管和内部网络共享。

守护进程默认监听 9418 端口，从指定的基础路径对外提供仓库服务。与基于 HTTP 的 Git 服务器不同，git daemon 无需搭建 web 服务器，为只读仓库访问提供了极低的开销。

其安全性是有意受限的：仓库必须显式导出（通过 --export-all 或 git-daemon-export-ok 文件），且写入访问只应在可信环境中开启。对于需要身份验证和加密的生产系统，建议改用 HTTPS 或 SSH 协议。

# INSTALL

```dnf: sudo dnf install git-daemon```

```zypper: sudo zypper install git-daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO
