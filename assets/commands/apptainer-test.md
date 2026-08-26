# TAGLINE

运行容器中定义的验证测试

# TLDR

**运行容器的测试脚本**

```apptainer test [container.sif]```

**测试 Docker Hub 镜像**

```apptainer test docker://[image:tag]```

**测试容器内的特定应用**

```apptainer test --app [appname] [container.sif]```

**绑定目录进行测试**

```apptainer test --bind [/data]:[/mnt] [container.sif]```

**启用 NVIDIA GPU 支持进行测试**

```apptainer test --nv [container.sif]```

# SYNOPSIS

**apptainer test** [_options_] _container_

# PARAMETERS

**--app** _name_
> 运行特定 SCIF 应用的测试部分。

**--bind**, **-B** _src[:dest[:opts]]_
> 将宿主机路径绑定挂载到容器中。

**--nv**
> 启用 NVIDIA GPU 支持。

**--rocm**
> 启用 AMD ROCm GPU 支持。

**--contain**, **-c**
> 使用最小化的 /dev，并将其他目录置空。

**--containall**, **-C**
> 完全隔离模式。

**--cleanenv**, **-e**
> 测试前清理环境变量。

**--fakeroot**
> 以模拟的 root 权限运行测试。

**--cwd**, **--pwd** _path_
> 设置容器内的工作目录。

**--writable**, **-w**
> 使文件系统以读写方式访问。

**--writable-tmpfs**
> 使文件系统可读写但数据不持久（tmpfs overlay）。

**--help**, **-h**
> 显示 test 命令的帮助信息。

# DESCRIPTION

**apptainer test** 执行容器 **%test** 部分中定义的测试脚本。它为容器作者提供了一种标准化的方式来包含验证检查，确认容器功能正常。

测试脚本通常检查所需软件是否已安装、库是否可访问，以及容器能否完成其预期功能。测试脚本的退出码决定通过（0）或失败（非零）状态。

对于使用 Scientific Filesystem（SCIF）的容器，**--app** 标志会运行容器内特定应用的测试部分。这使多应用容器可以拥有各自独立的测试套件。

容器作者在构建时定义测试。如果不存在 %test 部分，命令会成功完成而不执行任何内容。此命令在 CI/CD 流水线中很有用，可在部署前验证容器构建。

# CAVEATS

只有在容器构建时定义了 %test 部分才会运行测试。即使不存在任何测试也会返回成功（静默通过）。测试脚本与容器运行时具有相同的环境约束。复杂的测试可能需要绑定挂载或 GPU 标志才能正常工作。

# HISTORY

test 子命令自 Singularity/Apptainer 早期版本起就是其组成部分，为容器作者提供了验证构建的标准方式。它通过确保容器达到预期功能，支持了科学计算的可复现性目标。**2021** 年项目从 Singularity 分叉出 Apptainer 时保留了这一特性。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-build](/man/apptainer-build)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-inspect](/man/apptainer-inspect)(1)
