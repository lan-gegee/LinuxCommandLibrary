# TAGLINE

列出 Docker 容器及其状态

# TLDR

**列出运行中的容器**

```docker ps```

**列出所有容器**（包括已停止的）

```docker ps -a```

**使用自定义格式列出**

```docker ps --format "{{.ID}}: {{.Names}}"```

**仅列出容器 ID**

```docker ps -q```

**按名称过滤容器**

```docker ps -f name=[pattern]```

**按状态列出容器**

```docker ps -f status=[running|exited|paused]```

**显示容器大小**

```docker ps -s```

**列出最近创建的容器**

```docker ps -l```

# SYNOPSIS

**docker ps** [_options_]

# PARAMETERS

**-a**, **--all**
> 显示所有容器（默认只显示运行中的）。

**-q**, **--quiet**
> 仅显示容器 ID。

**-l**, **--latest**
> 显示最近创建的容器。

**-n** _num_
> 显示最近创建的 n 个容器。

**-s**, **--size**
> 显示文件总大小。

**-f**, **--filter** _filter_
> 根据条件过滤输出。

**--format** _string_
> 使用 Go 模板格式化输出。

**--no-trunc**
> 不截断输出。

# FILTERS

**id**: 容器 ID
**name**: 容器名称
**label**: 标签键或 key=value
**status**: created、restarting、running、paused、exited、dead
**ancestor**: 镜像名称或 ID
**network**: 网络名称或 ID
**publish** / **expose**: 端口号
**health**: healthy、unhealthy、starting、none

# FORMAT PLACEHOLDERS

**{{.ID}}**: 容器 ID
**{{.Names}}**: 容器名称
**{{.Image}}**: 镜像名称
**{{.Status}}**: 容器状态
**{{.Ports}}**: 发布的端口
**{{.State}}**: 容器状态
**{{.CreatedAt}}**: 创建时间
**{{.RunningFor}}**: 启动至今的时长
**{{.Size}}**: 容器磁盘占用
**{{.Mounts}}**: 挂载的卷名称
**{{.Networks}}**: 连接的网络名称
**{{.Command}}**: 带引号的命令
**{{.Label}}**: 容器标签值（例如 {{.Label "key"}}）

# DESCRIPTION

**docker ps** 列出 Docker 容器。默认只显示运行中的容器，包括其 ID、镜像、命令、创建时间、状态、端口和名称。

该命令提供过滤功能，可按多种条件查找特定容器。自定义格式可以精确显示所需信息，对脚本编写和自动化很有用。

容器 ID 默认截断显示；使用 **--no-trunc** 可查看完整 ID。**-q** 选项只输出 ID，便于传给其他命令。

# CAVEATS

已停止的容器默认隐藏；使用 **-a** 才能看到。大小计算（**-s**）在容器较多的系统上可能较慢。格式字符串使用 Go 模板语法。某些过滤器在使用通配符时可能出现意外行为。

# HISTORY

docker ps 自 **2013 年** Docker 最初发布起就是其一部分，仿照 Unix 中用于进程的 **ps** 命令设计。过滤和格式化选项是后来逐步加入的，以支持大规模容器管理。该命令仍然是检查运行中容器的主要方式。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-inspect](/man/docker-inspect)(1), [docker-logs](/man/docker-logs)(1), [docker-stats](/man/docker-stats)(1), [docker-rm](/man/docker-rm)(1), [docker-run](/man/docker-run)(1)
