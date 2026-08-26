# TAGLINE

将网站下载到本地目录以便离线浏览的网站复制工具

# TLDR

**将网站镜像到当前目录**

```httrack [https://example.com]```

**将网站镜像到指定目录**

```httrack [https://example.com] -O [path/to/output]```

**按指定深度限制镜像网站**

```httrack [https://example.com] -r[3]```

**继续中断的下载**

```httrack --continue```

**更新已有的镜像**

```httrack --update```

**通过代理镜像网站**

```httrack [https://example.com] -P [proxy:8080]```

**只镜像特定类型的文件**

```httrack [https://example.com] +*.pdf +*.jpg -* ```

**限制下载速度**（字节/秒）

```httrack [https://example.com] -A[102400]```

# SYNOPSIS

**httrack** [_url_] [_-options_] [_+filters_] [_-filters_]

**httrack** --mirror _url_ -O _path_

**httrack** --continue | --update

# PARAMETERS

**-O**, **--path** _PATH_
> 输出/项目路径

**-w**, **--mirror**
> 镜像网站（默认模式）

**-W**, **--mirror-wizard**
> 通过交互式向导镜像网站

**-g**, **--get-files**
> 只获取文件，不镜像目录结构

**-i**, **--continue**
> 继续中断的下载

**-r** _N_, **--depth** _N_
> 设置链接深度限制（默认：镜像模式下不限制）

**-m** _N_, **--max-files** _N_
> 最大下载文件数

**-M** _N_, **--max-size** _N_
> 最大总大小（字节）

**-E** _N_, **--max-time** _N_
> 最大镜像时长（秒）

**-A** _N_, **--max-rate** _N_
> 最大传输速率（字节/秒）

**-c** _N_, **--sockets** _N_
> 同时连接的数量

**-T** _N_, **--timeout** _N_
> 连接超时时间（秒）

**-R** _N_, **--retries** _N_
> 重试次数

**-P**, **--proxy** _HOST:PORT_
> 使用代理服务器

**-K** _N_, **--keep-links** _N_
> 保持原始链接格式（0=相对，2=绝对）

**-x**, **--replace-external**
> 用错误页面替换外部链接

**-n**, **--near**
> 获取链接附近的非 HTML 文件

**-t**, **--test**
> 仅测试链接，不下载

**-q**, **--quiet**
> 安静模式，无输出

**-v**, **--verbose**
> 详细输出

**-s0**, **--robots=0**
> 忽略 robots.txt

**-F** _STRING_
> 为 HTTP 请求设置 User-Agent 头

**-N** _N_
> 已保存文件的命名结构类型规范

**-%c** _N_
> 每秒最大连接数

**-h**, **--help**
> 显示帮助

# FILTERS

**+**_pattern_
> 包含匹配模式的 URL

**-**_pattern_
> 排除匹配模式的 URL

**+*.pdf**
> 包含所有 PDF 文件

**-*.exe**
> 排除所有 EXE 文件

**+example.com/*  -***
> 只从特定域名镜像

# DESCRIPTION

**httrack** 是一款网站复制工具，可将网站下载到本地目录以便离线浏览。它会保留原始站点结构，并将链接转换为可在本地使用的形式。镜像出来的站点可以用任何 Web 浏览器离线浏览。

该工具按指定深度跟踪链接、下载文件并重建相对路径。它支持 HTTP 和 HTTPS 协议、身份验证、cookie 以及代理服务器。过滤器通过通配符模式控制要下载哪些文件。

HTTrack 可以更新之前镜像过的站点，只下载发生变化的文件。借助 continue 选项，它能妥善处理中断的下载。**webhttrack** 命令提供基于浏览器的图形界面。

# CAVEATS

镜像网站可能违反服务条款或版权法。务必检查 robots.txt 和站点政策。JavaScript 渲染的内容和动态生成的页面可能无法正确镜像。一些站点采用反爬措施，可能会阻止 HTTrack。CGI 脚本和服务器端功能在离线副本中无法工作。大型站点可能占用大量磁盘空间和带宽。

# HISTORY

HTTrack 由 **Xavier Roche** 创建，于 **1998 年**首次发布。它采用 C 语言编写，是最受欢迎的开源网站镜像工具之一。该项目在 Windows、Linux 及其他类 Unix 系统上同时提供命令行和 GUI 界面。开发仍在继续，定期更新以适应现代 Web 技术。

# INSTALL

```apt: sudo apt install httrack```

```dnf: sudo dnf install httrack```

```pacman: sudo pacman -S httrack```

```zypper: sudo zypper install httrack```

```brew: brew install httrack```

```nix: nix profile install nixpkgs#httrack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [wget2](/man/wget2)(1)
