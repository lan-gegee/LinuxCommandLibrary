# TAGLINE

**aptdaemon** 软件包管理服务的命令行客户端

# TLDR

通过 aptd **安装**软件包

```aptdcon --install "[package1 package2]"```

**删除**软件包

```aptdcon --remove "[package]"```

**彻底清除**软件包（连同配置文件）

```aptdcon --purge "[package]"```

**升级**指定的软件包

```aptdcon --upgrade "[package]"```

**升级整个系统**

```aptdcon --upgrade-system```

**刷新**软件包缓存

```aptdcon --refresh```

**修复**损坏的依赖

```aptdcon --fix-depends```

**安装软件包并显示 dpkg 的终端输出**

```aptdcon --install "[package]" --show-terminal```

# SYNOPSIS

**aptdcon** [_action_] [_options_]

# DESCRIPTION

**aptdcon** 是 **aptdaemon** 的命令行客户端。aptdaemon 是一个系统级 D-Bus 服务，负责序列化 APT 操作并执行基于 PolicyKit 的身份验证。它暴露与 GNOME Software、Software-Properties-GTK 和 update-manager 相同的后端，因此通过 `aptdcon` 发起的操作能与正在运行的 GUI 软件包管理器顺畅协作。

操作会在守护进程上排队；多个 `aptdcon` 调用只是把任务交给 `aptd`，由其按顺序执行。PolicyKit 会按需提示进行身份验证（通过图形界面或 tty 代理）。

# PARAMETERS

**-i** _PKGS_, **--install** _PKGS_
> 安装列出的软件包。

**--reinstall** _PKGS_
> 重新安装列出的软件包。

**-r** _PKGS_, **--remove** _PKGS_
> 删除列出的软件包（保留配置文件）。

**-p** _PKGS_, **--purge** _PKGS_
> 删除并彻底清除列出的软件包（连同配置文件一起删除）。

**-u** _PKGS_, **--upgrade** _PKGS_
> 升级列出的软件包。

**--upgrade-system**
> 升级系统上的所有软件包（相当于 `apt upgrade`）。

**--refresh**
> 更新软件包列表。

**--fix-install**
> 通过 dpkg 完成先前被取消的安装。

**--fix-depends**
> 尝试解决未满足的依赖。

**--add-vendor-key** _PUBLIC_KEY_FILE_
> 从文件安装厂商签名密钥。

**--add-vendor-key-from-keyserver** _KEY_ID_
> 从密钥服务器获取并安装厂商密钥。

**--key-server** _KEYSERVER_
> 使用 _KEYSERVER_ 下载密钥。

**--remove-vendor-key** _FINGERPRINT_
> 删除具有给定指纹的厂商密钥。

**--list-trusted-vendors**
> 列出受信任的软件供应商及其密钥。

**--add-repository** _'DEB_LINE'_
> 将给定的 `deb` 行添加到软件源。

**--sources-file** _FILE_
> 仓库管理使用的替代 sources.list 位置。

**--show-terminal**
> 连接到 dpkg 的交互式终端（提示与进度信息）。

**--hide-terminal**
> 抑制 dpkg 的终端输出。

**--allow-unauthenticated**
> 允许安装非受信任供应商来源的软件包。

**-d**, **--debug**
> 打印额外的诊断信息。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示 aptdcon 版本。

# CAVEATS

需要 **aptdaemon** 服务。在没有 aptd 的系统上（现代 Ubuntu/Debian 正迁移到 `packagekit`），可直接用 `apt` 或 `apt-get` 替代。所有修改性操作都需要 PolicyKit 授权，因此在 GUI 代理或 tty 中会出现密码提示。

# HISTORY

**aptdaemon**（及其客户端 `aptdcon` 与 `aptd-cli`）由 **Sebastian Heinlein** 为 Ubuntu 编写，目的是为 PackageKit/Software Center/Update Manager 提供统一的 D-Bus 协调入口来调用 APT。

# SEE ALSO

[aptd](/man/aptd)(1), [apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [pkcon](/man/pkcon)(1), [pkexec](/man/pkexec)(1)
