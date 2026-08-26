# TAGLINE

下载并启动 Tor Browser

# TLDR

**启动 Tor Browser**

```torbrowser-launcher```

**打开设置对话框**

```torbrowser-launcher --settings```

**检查更新**

```torbrowser-launcher```

# SYNOPSIS

**torbrowser-launcher** [_options_]

# PARAMETERS

**--settings**
> 打开 Tor Browser Launcher 设置对话框。

**--help**
> 显示帮助信息。

# DESCRIPTION

**torbrowser-launcher** 在 Linux 上下载、安装并启动 Tor Browser。首次运行时，它会从 Tor Project 下载最新的 Tor Browser，验证签名，并将其安装到用户主目录。

后续运行会检查更新并启动浏览器。启动器会为你的架构和语言下载正确的版本，并在更新过程中保留书签和偏好设置。

设置对话框允许配置下载镜像、是否使用系统 Tor 服务进行下载以及其他选项。

Tor Browser 通过 Tor 网络路由流量来支持匿名上网，对连接加密并隐藏用户的 IP 地址。

# CAVEATS

首次启动需要联网下载 Tor Browser。下载耗时取决于网络速度。某些网络会封锁 Tor；如有需要可在设置中使用网桥（bridge）。签名验证依赖 GPG。

# HISTORY

**torbrowser-launcher** 由 Micah Lee 创建，旨在简化 Tor Browser 在 Linux 上的安装。它通过自动化签名验证解决了手动安装的安全隐患。该启动器已被 Debian、Ubuntu 和 Fedora 等 Linux 发行版广泛打包收录。

# INSTALL

```dnf: sudo dnf install torbrowser-launcher```

```pacman: sudo pacman -S torbrowser-launcher```

```zypper: sudo zypper install torbrowser-launcher```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tor](/man/tor)(1), [firefox](/man/firefox)(1), [gpg](/man/gpg)(1)
