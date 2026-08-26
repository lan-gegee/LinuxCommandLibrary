# TAGLINE

管理 Docker 容器、镜像、卷和网络的终端 UI

# TLDR

**启动 lazydocker**

```lazydocker```

**使用指定的 Docker 配置启动**

```lazydocker -f [/path/to/config.yml]```

**使用指定的 Docker Compose 文件**

```lazydocker -f [docker-compose.yml]```

**启动时不进行实时更新**

```lazydocker --no-live```

# SYNOPSIS

**lazydocker** [_-f config_] [_--no-live_] [_-v_]

# PARAMETERS

**-f**, **--config** _file_
> Docker Compose 配置文件或 lazydocker 配置文件的路径。

**--no-live**
> 禁用容器统计信息的实时更新。

**-v**, **--version**
> 打印版本信息。

**-d**, **--debug**
> 启用调试日志。

**-h**, **--help**
> 显示帮助。

# KEYBOARD SHORTCUTS

**Tab / Shift+Tab**
> 在各面板之间切换。

**↑ / ↓** 或 **j / k**
> 浏览列表项。

**Enter**
> 聚焦选中的条目。

**d**
> 删除/移除选中项。

**s**
> 停止容器。

**r**
> 重启容器。

**a**
> 附加到容器。

**m**
> 查看容器日志。

**e**
> 在容器中执行 Shell。

**b**
> 查看批量命令。

**[**
> 上一个标签页。

**]**
> 下一个标签页。

**/**
> 过滤条目。

**x**
> 打开菜单。

**q** 或 **Ctrl+c**
> 退出。

**?**
> 显示帮助。

# DESCRIPTION

**lazydocker** 是一个用于管理 Docker 容器、镜像、卷和网络的终端 UI。它提供交互式仪表盘，实时展示容器统计信息和日志，让你无需输入 docker 命令即可完成常见操作。

界面划分为多个面板：容器、镜像、卷以及一个主视图区域。每个面板都会列出资源及其状态指示。选中某个条目后，主面板中会显示对应的详情、统计信息、日志或配置。

针对容器，你可以查看实时的 CPU/内存统计、滚动查看日志、附加进去交互，或在其中执行 Shell。批量操作支持停止、移除或重启多个容器。镜像管理则涵盖拉取、构建和清理（prune）。

配置保存在 **~/.config/lazydocker/config.yml** 中，允许自定义按键绑定、颜色以及 Docker 连接设置。还可以为常用的操作定义自定义命令。

该工具同时兼容 Docker 和 Docker Compose 项目，能够自动检测 compose 文件并支持按服务逐一操作。

# CAVEATS

需要能够访问 Docker 守护进程（用户必须在 docker 组中或使用 sudo）。实时统计会增加 CPU 开销。并非所有 Docker 功能都被暴露出来。在现代终端模拟器中效果最佳。容器数量很大时可能影响性能。

# HISTORY

**lazydocker** 由 Jesse Duffield 于 **2019 年**前后创建，属于一系列 "lazy" 终端 UI（包括 lazygit）中的一员。它用 Go 编写，初衷是希望有一种更直观的方式来管理 Docker，而不必离开终端。该项目如今在偏好键盘驱动界面的开发者中相当流行。

# INSTALL

```pacman: sudo pacman -S lazydocker```

```apk: sudo apk add lazydocker```

```brew: brew install lazydocker```

```nix: nix profile install nixpkgs#lazydocker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [lazygit](/man/lazygit)(1), [ctop](/man/ctop)(1), [podman](/man/podman)(1), [dive](/man/dive)(1)
