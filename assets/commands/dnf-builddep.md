# TAGLINE

安装 RPM 软件包的构建依赖

# TLDR

为 spec 文件安装**构建依赖**

```dnf builddep [path/to/specification.spec]```

从**源码 RPM** 安装依赖

```dnf builddep [path/to/package.src.rpm]```

安装依赖并**跳过不可用**的软件包

```dnf builddep --skip-unavailable [path/to/specification.spec]```

在依赖解析期间**定义 RPM 宏**

```dnf builddep -D '[macro expression]' [path/to/specification.spec]```

从软件仓库按**包名**安装依赖

```dnf builddep [package_name]```

安装依赖且**不弹出确认**提示

```dnf builddep -y [path/to/specification.spec]```

# SYNOPSIS

**dnf builddep** [_options_] _package_

# DESCRIPTION

**dnf builddep** 根据包的 spec 文件或源码 RPM 安装构建该包所需的全部依赖。属于 dnf-plugins-core。

从源码构建 RPM 软件包时的必备工具。

# PARAMETERS

**--skip-unavailable**
> 跳过软件仓库中没有的构建依赖。

**-D**, **--define** _macro_
> 解析 spec 文件时定义 RPM 宏（对 SRPM 不生效）。

**--spec**
> 将参数视为 .spec 文件。

**--srpm**
> 将参数视为源码 RPM 文件。

**--nobest**
> 不将软件包限制为最优版本。

**-y**, **--assumeyes**
> 对所有问题自动回答 yes。

**--help-cmd**
> 显示本命令的帮助。

# CAVEATS

需要 dnf-plugins-core。构建依赖可能包含大量软件包。通常需要 root 权限。builddep 不支持 --skip-broken 选项。

# SEE ALSO

[dnf](/man/dnf)(8), [rpmbuild](/man/rpmbuild)(8), [rpm](/man/rpm)(8), [mock](/man/mock)(1)
