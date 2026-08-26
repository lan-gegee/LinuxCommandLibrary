# TAGLINE

速度最快的异步互联网端口扫描器

# TLDR

**扫描单个端口**

```sudo masscan [192.168.1.0/24] -p [80]```

**扫描端口范围**

```sudo masscan [192.168.1.0/24] -p [1-65535]```

**扫描常用端口**

```sudo masscan [192.168.1.0/24] --ports [0-1023]```

**以指定速率扫描**

```sudo masscan [192.168.1.0/24] -p [80] --rate [10000]```

**输出到文件**

```sudo masscan [192.168.1.0/24] -p [80] -oL [results.txt]```

**排除目标**

```sudo masscan [10.0.0.0/8] -p [80] --excludefile [exclude.txt]```

# SYNOPSIS

**masscan** [_options_] _targets_

# DESCRIPTION

**masscan** 是速度最快的互联网端口扫描器，能够在 6 分钟内扫描整个互联网。它采用异步传输方式发送数据包，无需等待响应。

该工具专为授权安全评估中的大规模网络侦察而设计。为了兼容性，其输出格式与 nmap 类似。

# PARAMETERS

**-p** _ports_
> 要扫描的端口。

**--rate** _pps_
> 每秒数据包数。

**--banners**
> 抓取横幅信息。

**-oL** _file_
> 列表格式输出。

**-oJ** _file_
> JSON 输出。

**-oG** _file_
> 可 grep 的输出。

**-oX** _file_
> XML 输出。

**--excludefile** _file_
> 排除的地址。

**--adapter** _name_
> 网络接口。

**-c** _file_
> 配置文件。

**--wait** _seconds_
> 发送后的等待时间。

# CAVEATS

需要 root/raw 套接字。高发包速率可能压垮网络。仅限授权测试。可能触发 IDS 告警。无状态扫描可能漏掉被过滤的端口。

# HISTORY

**masscan** 由 **Robert David Graham** 创建并于 **2013 年**发布。它旨在证明全网扫描是可行的，并为大规模的合法安全研究提供工具。

# INSTALL

```apt: sudo apt install masscan```

```dnf: sudo dnf install masscan```

```pacman: sudo pacman -S masscan```

```apk: sudo apk add masscan```

```brew: brew install masscan```

```nix: nix profile install nixpkgs#masscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [zmap](/man/zmap)(1), [rustscan](/man/rustscan)(1), [unicornscan](/man/unicornscan)(1)
