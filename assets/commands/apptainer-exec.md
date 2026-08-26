# TAGLINE

在 Apptainer 容器内执行命令。

# TLDR

在容器内**执行命令**

```apptainer exec [container.sif] [command]```

将目录从宿主机**绑定挂载到容器中运行**

```apptainer exec --bind [/host/path]:[/container/path] [container.sif] [command]```

以可写 overlay **执行**

```apptainer exec --overlay [overlay.img] [container.sif] [command]```

**启用 GPU 支持**（NVIDIA）运行

```apptainer exec --nv [container.sif] [command]```

从 Docker Hub 镜像**执行**

```apptainer exec docker://[image:tag] [command]```

在隔离网络中**运行**

```apptainer exec --net --network none [container.sif] [command]```

使用自定义环境变量**执行**

```apptainer exec --env [VAR=value] [container.sif] [command]```

在可写沙箱目录中**运行**

```apptainer exec --writable [sandbox/] [command]```

# SYNOPSIS

**apptainer exec** [_options_] _container_ _command_ [_args_]

# PARAMETERS

**--bind**, **-B** _src[:dest[:opts]]_
> 将宿主机的路径绑定挂载到容器中。

**--overlay** _image_
> 使用 overlay 文件系统作为可写层。

**--nv**
> 在容器内启用 NVIDIA GPU 支持。

**--rocm**
> 启用 AMD ROCm GPU 支持。

**--contain**, **-c**
> 使用最小化的 /dev，并将其他目录置空。

**--containall**, **-C**
> 完全隔离：包含文件系统，外加新的 PID 和 IPC 命名空间以及干净的环境。

**--cleanenv**, **-e**
> 运行容器前清理环境变量。

**--env** _VAR=value_
> 在容器内设置环境变量。

**--env-file** _file_
> 从文件加载环境变量。

**--home** _path_
> 设置自定义主目录。

**--cwd** _path_
> 设置容器内的初始工作目录。（**--pwd** 是已废弃的同义词。）

**--net**
> 启用网络命名空间。

**--network** _type_
> 指定网络类型（none、bridge 等）。

**--fakeroot**
> 以模拟的 root 权限运行容器。

**--writable-tmpfs**
> 添加可写的 tmpfs overlay。

**--no-mount** _type_
> 禁用特定的挂载点。有效值：proc、sys、dev、devpts、home、tmp、hostfs、cwd。

**--no-home**
> 不将用户的主目录挂载到容器中。

**--writable**, **-w**
> 将容器文件系统设为读写（需要可写镜像或沙箱目录）。

**--scratch**, **-S** _dir_
> 在容器内包含一个 scratch 目录，它链接到宿主机上的临时目录。

**--workdir**, **-W** _path_
> 使用 **--contain** 或 **--scratch** 时，用于覆盖 /tmp、/var/tmp 和 $HOME 的工作目录。

**--ipc**, **-i**
> 在新的 IPC 命名空间中运行容器。

**--pid**, **-p**
> 在新的 PID 命名空间中运行容器。

**--userns**, **-u**
> 在新的用户命名空间中运行容器。

**--uts**
> 在新的 UTS 命名空间中运行容器。

**--no-eval**
> 不对环境变量或 OCI CMD/ENTRYPOINT 进行 shell 求值。

**--fusemount** _spec_
> 在容器内挂载 FUSE 文件系统，格式为：_type:fuse_command container_path_。

# DESCRIPTION

**apptainer exec** 在 Apptainer 容器内运行指定的命令。与提供交互式会话的 **apptainer shell** 不同，exec 运行单条命令并返回其退出状态，因此非常适合批处理和脚本场景。

容器可以是本地 SIF 文件、库 URI（library://）、Docker URI（docker://）或 OCI 归档。命令及其参数在容器环境中执行，并保留当前用户的身份。

默认情况下，Apptainer 会将当前目录、主目录和标准系统路径挂载进容器。可以使用 **--bind** 绑定更多路径。对于 HPC 工作负载，**--nv** 或 **--rocm** 标志可启用 GPU 直通。

该命令默认继承宿主机的环境变量。为了可复现性可使用 **--cleanenv**，为了隔离性可使用 **--contain**。退出状态反映所执行命令的返回码。

# CONFIGURATION

**/etc/apptainer/apptainer.conf**
> 主配置文件，控制默认绑定路径、安全选项、GPU 支持和命名空间设置。

# CAVEATS

无 root 运行要求内核启用用户命名空间。某些容器可能需要 **--writable-tmpfs** 或 **--overlay** 才能正常工作。NVIDIA GPU 支持需要 nvidia-container-cli 和兼容的驱动程序。除非配置了用户命名空间，否则网络命名空间需要 root 或相应权限。

# HISTORY

Apptainer 是 **Singularity** 项目于 **2021** 年加入 Linux 基金会之后的延续。exec 子命令自 **2015** 年 Singularity 在劳伦斯伯克利国家实验室诞生以来一直是核心功能。Apptainer 1.0 于 **2022** 年发布，在保持与 Singularity 容器格式完全兼容的同时加入了新特性。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-shell](/man/apptainer-shell)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-build](/man/apptainer-build)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-overlay](/man/apptainer-overlay)(1), [docker](/man/docker)(1)
