# TAGLINE

通过网络提供电子书库服务

# TLDR

**启动内容服务器并加载书库**

```calibre-server [/path/to/library]```

**在指定端口启动**

```calibre-server --port [8080] [/path/to/library]```

**启用身份验证**

```calibre-server --enable-auth --userdb [users.sqlite] [/path/to/library]```

**管理用户账户**

```calibre-server --manage-users --userdb [users.sqlite]```

**启用本地写入权限**

```calibre-server --enable-local-write [/path/to/library]```

**提供多个书库**

```calibre-server [/library1] [/library2]```

**通过 Bonjour 广播**

```calibre-server --enable-use-bonjour [/path/to/library]```

# SYNOPSIS

**calibre-server** [_options_] [_library_path_...]

# DESCRIPTION

**calibre-server** 将 Calibre 电子书库发布到网络上。用户可以在网页浏览器中直接访问、浏览和阅读书籍。该服务器支持 OPDS 订阅源、离线缓存和身份验证。

# PARAMETERS

**--port**=_number_
> 监听端口（默认：8080）

**--listen-on**=_address_
> 绑定的网络接口（默认：全部）

**--enable-auth**
> 要求密码验证

**--userdb**=_path_
> SQLite 用户数据库的路径

**--manage-users**
> 交互式用户管理模式

**--enable-local-write**
> 允许本地客户端修改书库

**--enable-use-bonjour**
> 通过 Bonjour/mDNS 广播 OPDS

**--url-prefix**=_prefix_
> 用于反向代理的 URL 路径前缀

**--daemonize**
> 以后台守护进程方式运行

**--pidfile**=_path_
> 将进程 ID 写入文件

# FEATURES

**OPDS 订阅源**
> 与基于 OPDS 的阅读应用兼容

**离线阅读**
> 浏览器会缓存书籍以便离线访问

**远程访问**
> 可从网络上的任意设备访问书库

# CAVEATS

暴露到互联网前请先启用身份验证。macOS 上，可执行文件位于 calibre.app 包内。要让 calibredb 远程访问，需使用 --enable-local-write。

# INSTALL

```dnf: sudo dnf install calibre```

```pacman: sudo pacman -S calibre```

```zypper: sudo zypper install calibre```

```nix: nix profile install nixpkgs#calibre```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[calibredb](/man/calibredb)(1), [calibre](/man/calibre)(1), [ebook-convert](/man/ebook-convert)(1)

# RESOURCES

```[Source code](https://github.com/kovidgoyal/calibre)```

```[Homepage](https://calibre-ebook.com/)```

```[Documentation](https://manual.calibre-ebook.com/)```

<!-- verified: 2026-06-22 -->
