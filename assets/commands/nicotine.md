# TAGLINE

Soulseek 点对点文件共享网络的图形客户端

# TLDR

**启动 Nicotine+**

```nicotine```

**以无头模式启动**

```nicotine --headless```

**启动后最小化到托盘**

```nicotine --hidden```

**指定配置目录**

```nicotine --config [/path/to/config]```

**显示版本**

```nicotine --version```

# SYNOPSIS

**nicotine** [_--headless_] [_--hidden_] [_--config dir_] [_options_]

# PARAMETERS

**--headless**, **-s**
> 不带 GUI 运行。

**--hidden**, **-t**
> 启动后最小化到系统托盘。

**-c** _DIR_, **--config** _DIR_
> 配置目录。

**-u** _USER_, **--user** _USER_
> 登录用的用户名。

**-p** _PASS_, **--password** _PASS_
> 登录用的密码。

**--rescan**
> 重新扫描共享文件。

**--version**, **-v**
> 显示版本。

**--help**, **-h**
> 显示帮助。

# DESCRIPTION

**Nicotine+** 是 Soulseek 点对点文件共享网络的图形客户端。它让你可以与 Soulseek 网络的其他用户一起搜索、下载和共享文件。

这个网络以音乐为主，尤其是稀有和冷门的录音。用户共享自己的收藏，也可以浏览他人的曲库。

搜索可以在整个网络中查找文件。结果会显示文件详情、用户状态以及下载槽位情况。队列管理负责处理多个下载任务。

聊天室和私信支持社区交流。用户在其中讨论音乐、互相推荐并协调互传。

共享文件夹定义了你向他人开放的内容。上传限额和槽位管理则控制带宽的使用。

无头模式下程序不启动 GUI 运行，适合用作专门的共享服务器。

# CAVEATS

需要 Soulseek 网络账号。该网络有自己独特的分享文化和惯例。文件核验由用户自行负责。部分内容可能受版权保护。

# HISTORY

**Nicotine+** 是原 Nicotine 客户端的分支，后者于 **2000 年代初**作为一个开源的 Soulseek 客户端诞生。Nicotine+ 自 **2020 年**以来一直活跃维护，持续对代码库进行现代化改造并添加新功能。

# SEE ALSO

[transmission](/man/transmission)(1), [deluge](/man/deluge)(1)
