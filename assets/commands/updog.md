# TAGLINE

支持上传的简易 HTTP 文件服务器

# TLDR

**启动服务器**

```updog```

**自定义端口**

```updog -p [8080]```

**启用上传**

```updog --upload```

**设置密码**

```updog --password [secret]```

**自定义目录**

```updog -d [path/to/directory]```

# SYNOPSIS

**updog** [_-p port_] [_-d dir_] [_--upload_] [_options_]

# PARAMETERS

**-p** _PORT_
> 端口号。

**-d** _DIR_
> 要对外服务的目录。

**--upload**
> 允许上传。

**--password** _PASS_
> 设置密码。

**--ssl**
> 启用 HTTPS。

# DESCRIPTION

**updog** 是一款基于 Python 的 HTTP 文件服务器，定位是 Python 内置 SimpleHTTPServer 的现代化替代品。它从某个目录对外提供文件服务，界面简洁，支持浏览、下载以及可选的文件上传。

除了基础的文件服务之外，它还提供密码保护的访问控制、SSL/HTTPS 支持和自适应网页界面等特性。通过 **--upload** 标志即可开启文件上传，非常适合在局域网的机器之间快速传输文件。

updog 面向开发用途和临时性文件共享，并非为生产环境设计。它以合理的默认配置快速启动，并可通过命令行选项自定义端口、目录、身份验证和加密方式。

# CAVEATS

需要 Python 环境。仅供开发使用。不适合生产环境。

# HISTORY

**updog** 作为 SimpleHTTPServer 的现代化 Python 替代方案而诞生，并加入了文件上传支持。

# INSTALL

```nix: nix profile install nixpkgs#updog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [serve](/man/serve)(1), [http-server](/man/http-server)(1)
