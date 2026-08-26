# TAGLINE

F-Droid 软件仓库的命令行客户端

# TLDR

**搜索应用**

```fdroidcl search [query]```

**安装应用**

```fdroidcl install [app.id]```

**更新所有应用**

```fdroidcl upgrade```

**列出已安装的应用**

```fdroidcl list installed```

**显示应用详情**

```fdroidcl show [app.id]```

**刷新仓库**索引

```fdroidcl update```

**列出已连接的 Android 设备**

```fdroidcl devices```

只下载 APK 而**不安装**

```fdroidcl download [app.id]```

# SYNOPSIS

**fdroidcl** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作：search、install、upgrade、list、show。

**search** _QUERY_
> 搜索应用。

**install** _APP_
> 安装应用。

**upgrade**
> 更新所有已安装的应用。

**uninstall** _APP_
> 移除应用。

**list** _TYPE_
> 列出应用（installed、upgradable、all）。

**show** _APP_
> 显示应用详情。

**update**
> 刷新仓库索引。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fdroidcl** 是 F-Droid——自由软件 Android 应用仓库——的命令行客户端。它无需图形客户端即可从 F-Droid 仓库搜索、安装和管理应用。

该工具连接到 F-Droid 仓库，并使用 ADB 在已连接的 Android 设备上安装应用。它可以管理多台设备，并提供适合脚本的输出以便自动化。

fdroidcl 让高级用户和自动化部署场景可以通过命令行管理 F-Droid 应用。

# CAVEATS

需要 ADB 和已连接的设备。设备必须允许安装未知来源应用。某些应用需要特定的 Android 版本。

# HISTORY

fdroidcl 作为 F-Droid 图形客户端的命令行替代品而创建，支持以脚本方式管理来自 F-Droid 仓库的开源 Android 应用。

# INSTALL

```apt: sudo apt install fdroidcl```

```brew: brew install fdroidcl```

```nix: nix profile install nixpkgs#fdroidcl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fdroid](/man/fdroid)(1), [adb](/man/adb)(1)
