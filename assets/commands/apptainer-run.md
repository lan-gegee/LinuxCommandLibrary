# TAGLINE

执行容器的默认 runscript。

# TLDR

**运行容器的默认动作**

```apptainer run [container.sif]```

**运行容器**并将参数传递给 runscript

```apptainer run [container.sif] [arg1] [arg2]```

从 Docker Hub **运行**并绑定目录

```apptainer run --bind [/data]:[/mnt/data] docker://[python:3.11] [script.py]```

**启用 NVIDIA GPU 支持**运行

```apptainer run --nv [container.sif]```

**在隔离环境中运行**

```apptainer run --containall [container.sif]```

**以可写 overlay 运行**

```apptainer run --overlay [overlay.img] [container.sif]```

**以 fakeroot 运行**以执行类似 root 的操作

```apptainer run --fakeroot [container.sif]```

**使用自定义环境变量运行**

```apptainer run --env [KEY=value] [container.sif]```

# SYNOPSIS

**apptainer run** [_options_] _container_ [_args_]

# PARAMETERS

**--bind**, **-B** _src[:dest[:opts]]_
> 将宿主机路径绑定挂载到容器中。

**--overlay**, **-o** _image_
> 使用 overlay 镜像作为可写层。

**--writable**, **-w**
> 将容器文件系统设为读写（默认只读）。

**--writable-tmpfs**
> 添加可写的 tmpfs overlay；退出时更改会被丢弃。

**--nv**
> 启用 NVIDIA GPU 支持。

**--rocm**
> 启用 AMD ROCm GPU 支持。

**--contain**, **-c**
> 使用最小化的 /dev，home/tmp 等目录置空。

**--containall**, **-C**
> 完全隔离文件系统、PID、IPC 和环境变量。

**--cleanenv**, **-e**
> 运行前清理环境变量。

**--env** _VAR=value_
> 设置环境变量。

**--home**, **-H** _path_
> 指定自定义主目录。

**--pwd** _path_
> 设置容器内的工作目录。

**--fakeroot**, **-f**
> 在不使用宿主机 root 的情况下以表面上的 root 权限运行。

**--net**, **-n**
> 在新的网络命名空间中运行。

**--app** _name_
> 运行容器内的特定 SCIF 应用。

**--no-home**
> 不绑定主目录。

# DESCRIPTION

**apptainer run** 执行 Apptainer 容器的默认 runscript。runscript 在构建时于容器的 **%runscript** 部分定义，通常包含容器的主要功能或入口点。

这与运行任意命令的 **apptainer exec** 不同。运行容器时，Apptainer 会像调用普通可执行文件一样调用 runscript，并把额外的命令行参数传给它。

容器可以是本地 SIF 文件、Docker 引用（docker://）、库引用（library://）或 OCI 归档。如果容器未定义 runscript，该命令将执行一个 shell。

run 命令通过 **--app** 标志支持 SCIF（Scientific Filesystem）应用，使容器能够打包多个具有独立入口点的应用程序。标准的绑定挂载、环境变量和 GPU 支持与其他 Apptainer 命令一致。

# CONFIGURATION

**/etc/apptainer/apptainer.conf**
> 主配置文件，控制默认绑定路径、安全选项、GPU 支持和命名空间设置。

# CAVEATS

容器必须定义了 runscript 才能有可预期的行为。容器路径之后的参数会传给 runscript，而不是 Apptainer。如有需要，可用 **--** 分隔 Apptainer 选项和 runscript 参数。GPU 支持需要相应的驱动程序和容器配置。

# HISTORY

自 **2015** 年项目在劳伦斯伯克利国家实验室启动以来，run 命令一直是 Singularity/Apptainer 的核心。它的设计目标是让容器的行为像可执行文件一样，从而简化其与 HPC 工作流的集成。**2021** 年项目在 Linux 基金会旗下从 Singularity 过渡为 Apptainer 时继承了这一功能。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-shell](/man/apptainer-shell)(1), [apptainer-run-help](/man/apptainer-run-help)(1), [apptainer-build](/man/apptainer-build)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
