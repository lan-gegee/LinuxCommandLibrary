# TAGLINE

命令行 WebDAV 客户端

# TLDR

**连接 WebDAV 服务器**

```cadaver [http://dav.example.com/]```

**通过指定端口连接**

```cadaver [http://example.com:8080/path/]```

**通过 HTTPS 连接**

```cadaver [https://secure.example.com/]```

**通过代理连接**

```cadaver -p [proxy:8080] [http://dav.example.com/]```

**使用自定义 rcfile**

```cadaver -r [~/.myrc] [http://dav.example.com/]```

# SYNOPSIS

**cadaver** [_options_] _URL_

# DESCRIPTION

**cadaver** 是 Unix 系统上的命令行 WebDAV 客户端。它支持文件上传、下载、屏幕显示、就地编辑、命名空间操作、集合管理、属性操作和资源锁定。

操作方式类似于 ftp(1) 和 smbclient(1)。

# PARAMETERS

**-t**, **--tolerant**
> 允许 cd/open 进入非 WebDAV 集合

**-r** _file_, **--rcfile**=_file_
> 使用指定的 rcfile 而不是 ~/.cadaverrc

**-p** _host[:port]_, **--proxy**=_host[:port]_
> 通过代理服务器连接

**-V**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助

# INTERACTIVE COMMANDS

**ls** [_path_]
> 列出集合内容

**cd** _path_
> 切换到指定集合

**pwd**
> 显示当前集合

**get** _file_
> 下载文件

**put** _file_
> 上传文件

**mkcol** _name_
> 创建集合（目录）

**delete** _file_
> 删除资源

**copy** _src_ _dest_
> 复制资源

**move** _src_ _dest_
> 移动资源

**edit** _file_
> 就地编辑文件

# CONFIGURATION

**~/.cadaverrc**
> 用户设置和脚本

**~/.netrc**
> 自动登录凭据

# CAVEATS

URL 必须是以 http: 或 https: 为 scheme 的绝对地址。某些服务器的 WebDAV 兼容性可能有问题；可使用 -t 标志提高容错性。

# INSTALL

```apt: sudo apt install cadaver```

```dnf: sudo dnf install cadaver```

```pacman: sudo pacman -S cadaver```

```apk: sudo apk add cadaver```

```zypper: sudo zypper install cadaver```

```brew: brew install cadaver```

```nix: nix profile install nixpkgs#cadaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [ftp](/man/ftp)(1), [smbclient](/man/smbclient)(1)

# RESOURCES

```[Source code](https://github.com/notroj/cadaver)```

```[Homepage](https://notroj.github.io/cadaver/)```

<!-- verified: 2026-06-22 -->
