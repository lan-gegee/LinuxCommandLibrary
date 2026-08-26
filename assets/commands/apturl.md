# TAGLINE

从 apt: 协议 URL 安装软件包

# TLDR

通过 apt: URL **安装**软件包

```apturl apt:firefox```

安装**多个**软件包

```apturl "apt:vim,git,curl"```

从特定的**仓库分区**安装

```apturl "apt:[package]?section=universe"```

# SYNOPSIS

**apturl** [_options_] _apt:package_[,_package_...]

# DESCRIPTION

**apturl** 是一个简单的图形应用程序，它接受 apt 协议的 URL 作为命令行参数并处理软件包安装。当用户在网页浏览器中点击 apt: 链接时，apturl 会启动并在安装指定软件包前提示确认。

自 Ubuntu 7.10 起预装于 Ubuntu，提供一种无需命令行的友好软件安装方式。

# PARAMETERS

**-p**, **--http-proxy**
> 为软件包下载指定 HTTP 代理

**apt:_package_**
> 要安装的软件包

**apt:_package1_,_package2_**
> 要安装的多个软件包

**?channel=**
> 软件仓库或 PPA 源（如 ?channel=lucid-partner）

**?section=**
> 要启用的仓库分区（如 ?section=universe）

**?refresh=yes**
> 在查找软件包前强制刷新仓库

# CAVEATS

需要图形环境（X11/Wayland）。只应使用受信任的链接，验证对话框务必仔细阅读。退出码：0 = 成功，1 = 已取消，2 = 错误，3 = 参数无效。

# HISTORY

**apturl** 为 Ubuntu 开发，旨在简化软件安装，让网站能为 Linux 软件包提供直接安装链接。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1), [snap](/man/snap)(8)
