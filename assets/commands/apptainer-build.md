# TAGLINE

从定义文件或远程源构建 Apptainer 容器镜像。

# TLDR

从**定义文件**构建容器

```apptainer build [path/to/image.sif] [path/to/definition.def]```

从 **Docker Hub** 构建容器

```apptainer build [path/to/image.sif] docker://[image]:[tag]```

从 **Container Library** 构建容器

```apptainer build [path/to/image.sif] library://[user/collection/container]:[tag]```

构建**可写沙箱**目录而不是镜像文件

```apptainer build -s [path/to/directory] docker://[image]:[tag]```

构建容器时**不使用缓存**

```apptainer build --disable-cache [path/to/image.sif] docker://[image]:[tag]```

**强制覆盖**已有的镜像文件

```apptainer build -F [path/to/image.sif] [path/to/definition.def]```

使用 **fakeroot** 进行非特权构建

```apptainer build -f [path/to/image.sif] [path/to/definition.def]```

# SYNOPSIS

**apptainer build** [_options_] _image_ _build-spec_

# DESCRIPTION

**apptainer build** 从多种来源创建 Apptainer 容器镜像，包括定义文件、Docker Hub、OCI 注册表和 Sylabs Container Library。生成的 SIF（Singularity Image Format）文件是一个可移植的不可变容器镜像。

定义文件（**.def**）以可复现的方式指定基础镜像、软件安装步骤、环境变量和运行脚本。沙箱模式则创建一个可写的目录结构，适合开发和测试。

# PARAMETERS

**-s, --sandbox**
> 构建可写目录，而不是不可变的 SIF 镜像

**-F, --force**
> 不提示直接覆盖已存在的镜像文件

**-f, --fakeroot**
> 使用 fakeroot 构建，表现为以 root 身份运行（非特权定义构建的默认方式）。

**--disable-cache**
> 在构建过程中不使用也不创建缓存镜像。

**--no-cleanup**
> 构建失败后保留临时构建目录（用于调试）。

**-u, --update**
> 在现有沙箱容器上重新执行定义文件，重跑 %post 等部分。

**-T, --notest**
> 构建容器但不执行 %test 部分。

**--section** _name_
> 只运行给定的定义部分而不是全部（如 post、environment）。

**-e, --encrypt**
> 构建带有加密文件系统的镜像（需设置 APPTAINER_ENCRYPTION_PASSPHRASE 或 APPTAINER_ENCRYPTION_PEM_PATH）。

**--build-arg** _key=value_
> 用给定值替换定义文件中的 {{ key }} 占位符。

**--arch** _arch_
> 要构建的目标架构（默认：amd64）。

# CONFIGURATION

**/etc/apptainer/apptainer.conf**
> 主配置文件，控制构建行为、安全设置、绑定路径和 fakeroot 映射。

# CAVEATS

构建容器通常需要提升的权限或 fakeroot 配置。某些基础镜像可能与 fakeroot 构建不兼容。大型构建可能在缓存目录中占用大量磁盘空间。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-exec](/man/apptainer-exec)(1), [apptainer-shell](/man/apptainer-shell)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
