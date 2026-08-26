# TAGLINE

下载 RPM 软件包而不安装

# TLDR

**下载软件包**到当前目录

```dnf download [package]```

**下载到指定目录**

```dnf download [package] --destdir [path/to/directory]```

**下载软件包及其全部依赖**

```dnf download --resolve [package]```

**下载软件包的源码 RPM**

```dnf download --source [package]```

**打印 URL** 而不下载

```dnf download --url [package]```

# SYNOPSIS

**dnf download** [_options_] _package_ [_package_...]

# DESCRIPTION

**dnf download** 从已配置的 DNF 软件仓库下载 RPM 包但不安装。它属于 **dnf-plugins-core** 软件包。适合获取软件包用于离线安装、检查，或分发给与外网隔离的系统。

# PARAMETERS

**--destdir** _dir_
> 下载目标目录。默认为当前目录。

**--url**
> 打印下载 URL 到 stdout 而不下载。

**--source**
> 下载源码 RPM 而非二进制包。会自动启用源码仓库。

**--resolve**
> 同时下载指定软件包所有未安装的依赖。

**--alldeps**
> 与 --resolve 搭配时，下载全部依赖（包括已安装的）。

**--arch** _arch_
> 仅限指定架构的软件包。

# CAVEATS

需要安装 **dnf-plugins-core**。下载的软件包不会被自动安装。使用 --resolve 时默认只下载缺失的依赖。

# SEE ALSO

[dnf](/man/dnf)(8), [rpm](/man/rpm)(8), [yumdownloader](/man/yumdownloader)(1)
