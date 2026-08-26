# TAGLINE

面向 BitTorrent 客户端的文本界面

# TLDR

**连接默认的 Transmission 守护进程**

```tewi```

**连接 qBittorrent 实例**

```tewi --client-type qbittorrent --port [8080]```

**通过 Web API 连接 Deluge 实例**

```tewi --client-type deluge --port [8112]```

**连接远程主机**

```tewi --host [192.168.1.10] --port [9091]```

**使用指定的配置 profile**

```tewi --profile [myprofile]```

# SYNOPSIS

**tewi** [**--host** _host_] [**--port** _port_] [**--client-type** _type_] [**--profile** _name_] [**--help**]

# PARAMETERS

**--host** _host_
> 守护进程主机地址（默认：localhost）

**--port** _port_
> 守护进程端口（Transmission 默认：9091）

**--client-type** _type_
> 客户端类型：transmission、qbittorrent 或 deluge

**--profile** _name_
> 加载指定名称的配置 profile

**--profiles**
> 列出可用的配置 profile

**--badge-max-count** _N_
> 种子卡片中显示的最大徽标数量

**--badge-max-length** _N_
> 种子卡片中徽标的最大长度

**--search-providers** _providers_
> 指定启用的搜索提供者/索引器

**--list-search-providers**
> 显示可用的搜索提供者

**--help**
> 显示所有可用选项

# DESCRIPTION

**tewi** 是一个终端 UI，可在同一界面中管理 Transmission、qBittorrent 和 Deluge 等 BitTorrent 守护进程。它支持多种视图模式（card、compact、oneline）、种子管理操作、分类与标签管理、备用限速切换，以及与 Jackett、Prowlarr 和 bitmagnet 的搜索集成。配置 profile 允许管理多个守护进程连接。

# HISTORY

**tewi** 由 **Anton Larionov**（anlar）创建，使用 **Python** 编写（要求 Python 3.10+）。可通过 `pipx install tewi-torrent` 安装。2.0 版加入了 Deluge 支持、配置 profile 和搜索提供者集成。

# INSTALL

```aur: yay -S tewi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1), [superseedr](/man/superseedr)(1), [rtorrent](/man/rtorrent)(1)
