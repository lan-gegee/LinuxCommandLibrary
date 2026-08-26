# TAGLINE

容器镜像分析与比较

# TLDR

**分析镜像大小**

```container-diff analyze [image:tag]```

**对两个镜像的 apt 软件包做差异比较**

```container-diff diff [image1] [image2] --type=apt```

**比较 pip 软件包差异**

```container-diff diff [image1] [image2] --type=pip```

**比较文件系统变化**

```container-diff diff [image1] [image2] --type=file```

**同时使用多个分析器比较**

```container-diff diff [image1] [image2] --type=apt --type=pip --type=node```

**以 JSON 输出**

```container-diff diff [image1] [image2] --type=apt -j```

**比较本地与远程镜像**

```container-diff diff daemon://[local:tag] remote://[repo/image:tag]```

# SYNOPSIS

**container-diff** _command_ [_options_] _image_...

# DESCRIPTION

**container-diff** 是一款在语义层面分析和比较容器镜像的工具。它不只是展示原始的文件系统差异，还能理解包管理器，并以实际软件包（apt、pip、npm）为单位报告变化，让人更容易理解镜像版本之间发生了什么改变。

该工具支持多种镜像来源，包括本地 Docker 守护进程中的镜像、远程仓库镜像以及 tarball 归档。它可以分析单个镜像或比较两个镜像，输出支持人类可读格式和 JSON 格式，便于集成到 CI/CD 流水线中。

container-diff 由 Google 作为其 Container Tools 套件的一部分开发，可用于调试镜像膨胀问题、理解层内容以及验证构建产生了预期的变化。它在安全审计和 Docker 镜像优化方面尤其有用。

# COMMANDS

**analyze**
> 分析单个镜像

**diff**
> 比较两个镜像

# PARAMETERS

**--type** _analyzer_
> 分析器类型：apt、rpm、pip、node、file、size、history。

**-j**, **--json**
> 以 JSON 格式输出。

**-o**, **--order**
> 按大小降序排列结果。

**-q**, **--quiet**
> 屏蔽 stderr 输出。

**-c**, **--cache** _dir_
> 缓存目录。

**--filename** _path_
> 比较特定文件。

# IMAGE SOURCES

**daemon://image**: 本地 Docker 守护进程

**remote://image**: 远程仓库

**path/to/image.tar**: 本地 tarball

# ANALYZERS

**apt**: Debian/Ubuntu 软件包

**rpm**: Red Hat/CentOS 软件包

**pip**: Python 软件包

**node**: npm 软件包

**file**: 文件系统差异

**size**: 镜像大小

**history**: 层历史记录

# CAVEATS

该项目已于 2024 年 3 月归档，不再活跃维护。不支持直接使用 Docker ID（需先打标签）。仓库认证请使用 docker-credential-helpers。不带 **--type** 时默认执行大小分析。

# INSTALL

```pacman: sudo pacman -S container-diff```

```zypper: sudo zypper install container-diff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [dive](/man/dive)(1)
