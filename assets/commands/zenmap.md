# TAGLINE

Nmap 扫描器的图形界面

# TLDR

**启动图形界面**

```zenmap```

**扫描目标**

```zenmap -t [target]```

**打开已有的扫描结果**

```zenmap -f [results.xml]```

# SYNOPSIS

**zenmap** [_options_] [_results_file_]

# PARAMETERS

**-t**, **--target** _target_
> 以指定目标启动

**-p**, **--profile** _profile_
> 以指定扫描配置启动

**-f**, **--file** _file_
> 打开扫描结果文件

**-n**, **--nmap** _path_
> nmap 可执行文件的路径

**-v**, **--verbose**
> 增加详细输出

**--help**
> 显示帮助信息

# DESCRIPTION

**Zenmap** 是网络安全扫描器 Nmap 的官方图形用户界面。它提供可视化的网络拓扑图、扫描结果对比以及配置管理，让 Nmap 更容易上手。

界面包含预定义的扫描配置（Intense scan、Quick scan、Ping scan 等），并允许创建自定义配置。扫描结果以多种视图展示：Nmap 输出、端口/主机表格、拓扑图和主机详情。

Zenmap 可将扫描结果保存到其数据库中以便日后对比，帮助跟踪网络随时间的变化。拓扑视图将发现的主机及其关系可视化。

扫描配置会转换为 Nmap 命令行，并在界面中可见。这有助于用户在使用 GUI 的同时学习 Nmap 的选项。

# CAVEATS

许多扫描类型需要 root/管理员权限才能访问原始套接字。

未经授权扫描网络可能违法。只扫描你拥有或已获得明确测试许可的网络。

基于 GTK 的界面可能并非在所有系统上都可用。nmap 命令行则到处可用。

Zenmap 的开发不如 Nmap 本身活跃。一些较新的 Nmap 功能可能没有 GUI 支持。

# INSTALL

```pacman: sudo pacman -S zenmap```

```nix: nix profile install nixpkgs#zenmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [netstat](/man/netstat)(8)
