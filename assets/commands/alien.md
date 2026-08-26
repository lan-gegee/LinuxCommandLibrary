# TAGLINE

在各种 Linux 软件包格式之间转换。

# TLDR

将文件转换为 **Debian 格式**（.deb）

```sudo alien -d [path/to/file]```

将文件转换为 **Red Hat 格式**（.rpm）

```sudo alien -r [path/to/file]```

将文件转换为 **Slackware 格式**（.tgz）

```sudo alien -t [path/to/file]```

转换为 Debian 格式并**安装**到系统

```sudo alien -d -i [path/to/file]```

转换时**保留原始版本号**

```sudo alien -k [path/to/file]```

# SYNOPSIS

**alien** [_--to-deb_] [_--to-rpm_] [_--to-tgz_] [_--to-slp_] [_options_] _file_ [...]

# DESCRIPTION

**alien** 是一个在 Red Hat rpm、Debian deb、Stampede slp、Slackware tgz 和 Solaris pkg 文件格式之间转换的程序。它让用户能够把软件包从一种 Linux 发行版格式转换为另一种并进行安装。

# PARAMETERS

**-d, --to-deb**
> 创建 Debian 软件包（默认）

**-r, --to-rpm**
> 创建 RPM 软件包

**-t, --to-tgz**
> 创建 TGZ（Slackware）软件包

**--to-slp**
> 创建 SLP（Stampede）软件包

**-p, --to-pkg**
> 创建 Solaris pkg 软件包

**-i, --install**
> 自动安装生成的软件包

**-g, --generate**
> 创建临时目录以便手动构建软件包

**-k, --keep-version**
> 不递增版本号

**-c, --scripts**
> 转换安装/卸载脚本

**--fixperms**
> 规范文件权限（仅限 Debian）

**-v, --verbose**
> 显示执行的命令

**-T, --test**
> 用 lintian 测试生成的软件包

**--bump**=_N_
> 版本号递增 N 而不是 1

**-h, --help**
> 显示用法摘要

**--version**
> 显示 alien 版本

# CAVEATS

发行版特有的依赖和脚本可能无法在格式间正确转换，因此转换后的软件包未必能完美工作。

# HISTORY

它的诞生是为了帮助用户在原生软件包不可用时安装来自其他 Linux 发行版的软件。

# INSTALL

```dnf: sudo dnf install alien```

```apk: sudo apk add alien```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dpkg](/man/dpkg)(1), [rpm](/man/rpm)(8), [debtap](/man/debtap)(1)
