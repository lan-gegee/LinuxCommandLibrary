# TAGLINE

列出容器及其状态

# TLDR

**列出运行中的容器**

```podman ps```

**列出所有容器**

```podman ps -a```

**仅显示 ID**

```podman ps -q```

**自定义格式输出**

```podman ps --format "{{.Names}} {{.Status}}"```

**显示最新的容器**

```podman ps -l```

# SYNOPSIS

**podman ps** [_options_]

# PARAMETERS

**-a**, **--all**
> 显示所有容器。

**-q**, **--quiet**
> 仅显示 ID。

**-l**, **--latest**
> 显示最新的容器。

**--format** _FORMAT_
> 输出格式模板。

**-n** _N_
> 显示最后 N 个容器。

**--no-trunc**
> 不截断输出。

# DESCRIPTION

**podman ps** 列出 Podman 管理的容器，显示容器 ID、镜像、命令、创建时间、状态、端口和名称。默认只显示运行中的容器；使用 **-a** 可包含已停止的容器。

**--format** 选项接受 Go 模板用于自定义输出格式。使用 **-q** 仅显示容器 ID（便于脚本处理），**-l** 显示最近创建的容器，**-n** 限制为最后 N 个容器。与 Docker ps 兼容。

# CAVEATS

仅显示 podman 容器。输出与 Docker 兼容。

# HISTORY

podman ps 提供**容器列表**功能。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [podman-run](/man/podman-run)(1), [docker-ps](/man/docker-ps)(1)
