# TAGLINE

在容器内打开交互式 shell

# TLDR

在容器内**启动交互式 shell**

```apptainer shell [container.sif]```

**打开 shell 并绑定目录**

```apptainer shell --bind [/host/path]:[/container/path] [container.sif]```

进入 Docker Hub 镜像的 **shell**

```apptainer shell docker://[ubuntu:latest]```

**启动支持 NVIDIA GPU 的 shell**

```apptainer shell --nv [container.sif]```

**以干净的环境打开 shell**

```apptainer shell --cleanenv [container.sif]```

**完全隔离的 shell**（与宿主机隔离）

```apptainer shell --containall [container.sif]```

**以可写 overlay 启动 shell**

```apptainer shell --overlay [overlay.img] [container.sif]```

**具有 fakeroot 权限的 shell**

```apptainer shell --fakeroot [container.sif]```

# SYNOPSIS

**apptainer shell** [_options_] _container_

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
> 使用最小化的 /dev，并将其他目录置空。

**--containall**, **-C**
> 完全隔离文件系统、PID、IPC 和环境变量。

**--cleanenv**, **-e**
> 启动 shell 前清理环境变量。

**--env** _VAR=value_
> 在容器内设置环境变量。

**--home**, **-H** _path_
> 设置自定义主目录。

**--pwd** _path_
> 容器内的初始工作目录。

**--fakeroot**, **-f**
> 在不使用宿主机 root 的情况下以表面上的 root 权限运行。

**--net**, **-n**
> 在新的网络命名空间中运行。

**--shell**, **-s** _path_
> 指定要使用的 shell（默认：/bin/sh）。

**--no-home**
> 不绑定主目录。

# DESCRIPTION

**apptainer shell** 在 Apptainer 容器内启动交互式 shell 会话。它在容器内提供一个命令行环境，用于探索、调试和交互式操作。

默认情况下，shell 会继承你的用户身份、主目录和当前工作目录。除非使用隔离选项，宿主机环境大体上会被保留。这让 shell 的体验保持熟悉，同时可以访问容器的文件系统和已安装的软件。

容器可以是本地 SIF 文件、Docker 引用（docker://）、库引用（library://）或 OCI 归档。默认 shell 为 **/bin/sh**，如果容器内有其他 shell 可用，可以通过 **--shell** 选项覆盖。

开发时，可结合 **--overlay** 或 **--writable-tmpfs** 允许在容器内进行临时修改。当操作需要表面上的 root 权限但又没有实际的宿主机 root 访问权限时，使用 **--fakeroot**。

# CAVEATS

shell 是否可用取决于容器内安装了什么。某些极简容器可能只有 /bin/sh。宿主机到容器的环境变量泄漏可能导致意外行为；为了可复现性请使用 **--cleanenv**。除非使用可写 overlay 或绑定挂载，否则 shell 会话中所做的更改会丢失。

# HISTORY

自 **2015** 年项目在劳伦斯伯克利国家实验室创建以来，shell 命令一直是 Singularity/Apptainer 的核心功能。它的设计目的是让用户以熟悉的方式交互式访问容器，支持用户需要在容器环境中测试和调试的 HPC 使用场景。**2021** 年从 Singularity 分叉出 Apptainer 时，该命令保持了完全兼容。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-build](/man/apptainer-build)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
