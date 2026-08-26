# TAGLINE

构建 Linux 操作系统镜像的命令行工具

# TLDR

**从描述文件构建镜像**

```sudo kiwi-ng system build --description [path] --target-dir [output]```

**使用自定义软件仓库创建镜像**

```sudo kiwi-ng system build --description [path] --set-repo [repo-url] --target-dir [output]```

**列出可用的镜像类型**

```kiwi-ng image list```

**准备镜像根目录**

```sudo kiwi-ng system prepare --description [path] --root [rootdir]```

# SYNOPSIS

**kiwi-ng** [_options_] _command_ [_args_...]

# PARAMETERS

**system build**
> 从描述文件构建完整镜像。

**system prepare**
> 准备镜像的根文件系统。

**--description** _path_
> 镜像描述文件的路径。

**--target-dir** _path_
> 镜像输出目录。

**--set-repo** _url_
> 设置软件仓库 URL。

**--profile** _name_
> 构建指定的 profile。

# DESCRIPTION

**kiwi-ng** 是一款用于构建 Linux 操作系统镜像的命令行工具。它支持多种输出格式，包括 ISO、虚拟机镜像、容器和云镜像。它使用基于 XML 的描述文件来定义镜像配置。

# SEE ALSO

[mkisofs](/man/mkisofs)(1), [docker](/man/docker)(1)
