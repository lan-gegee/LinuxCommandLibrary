# TAGLINE

非交互式网络文件下载器

# TLDR

**下载文件**

```wget [https://example.com/file]```

**以自定义输出文件名下载**

```wget -O [filename] [url]```

**下载到指定目录**

```wget -P [directory] [url]```

**继续未完成的下载**

```wget -c [url]```

**在后台下载**

```wget -b [url]```

**递归下载**（镜像网站）

```wget -r [url]```

**带身份验证下载**

```wget --user=[username] --password=[password] [url]```

**限制下载速度**

```wget --limit-rate=[200k] [url]```

**从 URL 列表下载**

```wget -i [urls.txt]```

# SYNOPSIS

**wget** [_options_] [_url_...]

# PARAMETERS

**-O** _file_
> 写入指定文件

**-P** _prefix_
> 保存到指定目录

**-c**, **--continue**
> 继续未完成的下载

**-b**, **--background**
> 启动后转入后台

**-q**, **--quiet**
> 安静模式（无输出）

**-r**, **--recursive**
> 递归下载

**-l** _depth_, **--level**=_depth_
> 最大递归深度（0 = 无限）

**-k**, **--convert-links**
> 转换链接以便本地查看

**-p**, **--page-requisites**
> 下载页面所需的全部资源（图片、CSS 等）

**-m**, **--mirror**
> 镜像模式（-r -N -l inf --no-remove-listing）

**-i** _file_, **--input-file**=_file_
> 从文件读取 URL

**--limit-rate**=_rate_
> 限制下载速度

**--user**=_user_, **--password**=_pass_
> HTTP/FTP 身份验证

**-U** _agent_, **--user-agent**=_agent_
> 设置 User-Agent 请求头

**--no-check-certificate**
> 不验证 SSL 证书

**--header**=_string_
> 发送额外的 HTTP 请求头

# DESCRIPTION

**wget** 是一款非交互式网络下载器，支持 HTTP、HTTPS 和 FTP。它可以下载文件、跟随链接、镜像整个网站，并能处理中断和重试失败的传输。

对于简单下载，wget 会自动根据 URL 命名输出文件。使用 **-O** 指定其他名称，或使用 **-O -** 输出到标准输出。

配合 **-r** 的递归下载会跟随链接并下载关联页面。可结合 **-l** 限制深度、**-k** 转换链接便于离线浏览，以及 **-p** 获取页面资源。

Wget 自动处理重定向、cookie 和身份验证。它适合脚本化，非常适合自动化下载和 cron 任务。

# CAVEATS

递归下载可能消耗大量带宽和存储空间。镜像时务必用 **-l** 限制深度，并遵守 robots.txt（wget 默认遵守）。

**--no-check-certificate** 会绕过 SSL 验证——仅在必要时使用，并了解其安全影响。

某些网站会根据 User-Agent 阻止 wget。必要时可用 **-U** 设置类浏览器的 User-Agent 字符串。

对于需要多次重试和带宽控制的复杂下载，可以考虑创建 **.wgetrc** 配置文件。

# INSTALL

```apt: sudo apt install wget```

```pacman: sudo pacman -S wget```

```apk: sudo apk add wget```

```zypper: sudo zypper install wget```

```brew: brew install wget```

```nix: nix profile install nixpkgs#wget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [aria2c](/man/aria2c)(1), [httrack](/man/httrack)(1), [lftp](/man/lftp)(1)
