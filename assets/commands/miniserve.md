# TAGLINE

简单的文件服务器

# TLDR

**提供当前目录服务**

```miniserve .```

**提供指定目录服务**

```miniserve [/path/to/dir]```

**提供单个文件服务**

```miniserve [file.zip]```

**自定义端口**

```miniserve -p [8080] .```

**启用上传**

```miniserve -u .```

**启用身份验证**

```miniserve -a [user:pass] .```

# SYNOPSIS

**miniserve** [_options_] _path_

# PARAMETERS

_PATH_
> 要提供服务的文件或目录。

**-p** _PORT_
> 端口号。

**-u**
> 启用上传。

**-a** _CREDS_
> Basic 认证（user:pass）。

**-i** _ADDR_
> 要绑定的网络接口。

**--help**
> 显示帮助信息。

# DESCRIPTION

**miniserve** 是一个简单的文件服务器。它以极少的配置通过 HTTP 提供文件服务。

该工具支持上传、身份验证和二维码。使用 Rust 编写以保证性能。

# CAVEATS

建议仅用于开发用途。不适合生产环境。基于 Rust。

# HISTORY

miniserve 作为快速、极简的 **Rust 编写** HTTP 文件服务器而创建，用于快速共享文件。

# INSTALL

```pacman: sudo pacman -S miniserve```

```apk: sudo apk add miniserve```

```brew: brew install miniserve```

```nix: nix profile install nixpkgs#miniserve```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [http-server](/man/http-server)(1), [serve](/man/serve)(1)
