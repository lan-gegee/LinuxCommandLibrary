# TAGLINE

轻量级的多连接下载加速器

# TLDR

使用多个连接**下载**文件

```axel [https://example.com/file.zip]```

以**指定数量的连接**下载

```axel -n [16] [https://example.com/file.zip]```

以其他文件名**保存**

```axel -o [output.zip] [https://example.com/file.zip]```

将速度**限制**为给定的每秒字节数

```axel -s [1024000] [https://example.com/file.zip]```

设置自定义 **user agent**

```axel -U "[Mozilla/5.0]" [https://example.com/file.zip]```

若文件已存在则**跳过**下载

```axel -c [https://example.com/file.zip]```

# SYNOPSIS

**axel** [_options_] _url_

# DESCRIPTION

**axel** 是一款轻量级的下载加速器，它会针对同一个文件打开多个 HTTP/FTP 连接。通过同时下载文件的不同部分，与单连接工具相比，它可以显著加快下载速度。

对于未对单个连接限速的服务器上的大文件，该工具尤为有效。

# PARAMETERS

**--num-connections=**_num_, **-n** _num_
> 要打开的连接数。

**--output=**_file_, **-o** _file_
> 保存到的本地文件名。

**--max-speed=**_bytes_, **-s** _bytes_
> 尝试将平均速度保持在此每秒字节数左右。

**--alternate**, **-a**
> 显示带有各线程状态的备用进度条。

**--quiet**, **-q**
> 不向 stdout 输出任何内容。

**--verbose**, **-v**
> 显示更多状态消息。重复使用可获得更多细节。

**--header=**_header_, **-H** _header_
> 以 'Header: Value' 的形式添加 HTTP 头。

**--user-agent=**_agent_, **-U** _agent_
> 设置 HTTP user agent。

**--no-proxy**, **-N**
> 不使用任何代理服务器。

**--no-clobber**, **-c**
> 若同名文件已存在则跳过下载。

**--insecure**, **-k**
> 不验证 SSL 证书。

**--timeout=**_secs_, **-T** _secs_
> 设置 I/O 与连接超时。

**--max-redirect=**_num_
> 最大重定向次数（默认：20）。

# FEATURES

- 多个并发连接
- 恢复被中断的下载
- 速度限制
- 支持 FTP 和 HTTP
- 进度指示
- 支持代理

# CONFIGURATION

**/etc/axelrc**
> 系统级配置文件。

**~/.axelrc**
> 每用户配置文件，用于设置连接数和速度限制等默认值。

# CAVEATS

某些服务器会阻止多连接。可能被一些网站视为激进行为。并非所有服务器都支持范围请求。连接数上限设置过高可能浪费带宽。功能不如 aria2 丰富。

# HISTORY

**axel** 由 Wilmer van der Gaast 于 **2001** 年前后创建，作为下载管理器的轻量替代品，专注于通过并行连接提升速度。

# INSTALL

```apt: sudo apt install axel```

```dnf: sudo dnf install axel```

```pacman: sudo pacman -S axel```

```apk: sudo apk add axel```

```zypper: sudo zypper install axel```

```brew: brew install axel```

```nix: nix profile install nixpkgs#axel```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [aria2](/man/aria2)(1)

# RESOURCES

```[Source code](https://github.com/axel-download-accelerator/axel)```

<!-- verified: 2026-06-18 -->
