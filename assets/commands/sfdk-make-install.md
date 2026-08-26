# TAGLINE

将构建产物安装到 Sailfish OS 构建目标

# TLDR

将先前构建的项目**安装**到构建目标 sysroot

```sfdk make-install```

**安装到自定义目的地**目录

```sfdk make-install DESTDIR=[path]```

**并行安装**，使用 N 个任务

```sfdk make-install -j[N]```

**详细输出地安装**

```sfdk make-install V=1```

# SYNOPSIS

**sfdk make-install** [_make_arguments_...]

# DESCRIPTION

**sfdk make-install** 在 Sailfish OS 构建目标内运行底层构建系统（通常是 **make**、**cmake** 或 **qmake** 生成的 Makefile）的 `install` 目标。它是 **sfdk make** 的轻量封装，会选择 install 目标并把其余参数转发给构建工具。

该命令通常在 **sfdk build** 或 **sfdk make** 之后执行，作为开发工作流的一部分：为打包进 RPM 软件包而暂存文件，或将构建产物部署到构建目标 sysroot 以便测试。

# PARAMETERS

**DESTDIR=**_path_
> 将安装暂存到 _path_ 而不是默认的 sysroot 前缀。遵循标准 make/autotools 约定。

**-j**_N_
> 最多并行运行 _N_ 个安装任务。

**V=1**
> 启用详细构建输出。

# CAVEATS

需要已初始化的 Sailfish SDK 构建引擎以及通过 **sfdk config** 配置的激活构建目标。项目必须已经完成构建；**sfdk make-install** 不会触发编译。具体行为取决于项目自身的安装规则。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-make](/man/sfdk-make)(1)
