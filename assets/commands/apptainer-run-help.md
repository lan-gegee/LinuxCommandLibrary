# TAGLINE

显示容器内嵌的帮助文本。

# TLDR

**显示容器的 run-help**

```apptainer run-help [container.sif]```

**显示容器内特定应用的帮助**

```apptainer run-help --app [appname] [container.sif]```

**显示 Docker Hub 镜像的帮助**

```apptainer run-help docker://[image:tag]```

**显示库镜像中的帮助**

```apptainer run-help library://[user/collection/image:tag]```

# SYNOPSIS

**apptainer run-help** [_options_] _image_path_

# PARAMETERS

_image_path_
> SIF 文件的路径，或容器镜像的 URI（docker://、library://、oci-archive://）。

**--app** _string_
> 显示容器内定义的特定应用的帮助，而不是容器的一般帮助。帮助文本来自该应用的 **%apphelp** 部分。

**-h**, **--help**
> 显示 run-help 命令的帮助信息。

# DESCRIPTION

**apptainer run-help** 显示嵌入在 Apptainer/Singularity 容器内的帮助文本。这些帮助信息在容器构建时通过定义文件中的 **%help** 部分定义。使用 **--app** 标志时，则显示指定应用的 **%apphelp** 部分的内容。

容器作者利用 %help 部分来记录容器的用法，包括预期的参数、所需的绑定挂载、环境变量和示例命令。这为用户提供了容器专属的使用说明，无需查阅外部文档。

对没有帮助部分的容器调用此命令时，不会有任何输出。帮助文本存储在容器的元数据中，对容器运行时大小的影响微乎其微。

此命令在 HPC 环境中特别有用——用户可能遇到陌生的容器并需要快速了解用法。它与显示技术元数据而非面向用户文档的 **apptainer inspect** 互为补充。

# CAVEATS

只有当容器作者在构建时包含了 %help 部分，才会显示帮助。如果未定义帮助内容，命令不返回任何信息（也不报错）。无法在不重建容器的情况下为其添加帮助。

# HISTORY

run-help 功能自 Singularity/Apptainer 早期版本起就已存在，为容器作者记录容器用法提供了标准化的方式。**2021** 年 Singularity 在 Linux 基金会旗下更名为 Apptainer 后，该命令被保留下来。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-inspect](/man/apptainer-inspect)(1), [apptainer-build](/man/apptainer-build)(1)
