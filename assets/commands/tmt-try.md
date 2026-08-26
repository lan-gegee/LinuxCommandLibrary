# TAGLINE

交互式 tmt 测试试验

# TLDR

使用默认调配方式**试验**

```tmt try```

在**当前**目录中运行测试

```cd [path/to/test_directory] && tmt try```

针对特定**镜像**试验

```tmt try [fedora]```

选择镜像和**调配方式**

```tmt try [fedora@container]```

仅运行匹配**正则表达式**的测试

```tmt try -t [feature]```

只做调配然后**询问**下一步做什么

```tmt try -a```

不运行测试，直接**登录**客户机

```tmt try -l```

通过 IP 或 FQDN 连接到**正在运行的客户机**

```tmt try [192.168.12.23@connect]```

# SYNOPSIS

**tmt try** [_OPTIONS_] [_IMAGE_[@_HOW_]]...

# PARAMETERS

**-t**, **--test** _REGEXP_
> 运行匹配给定正则表达式的测试。默认执行当前工作目录下的所有测试。可多次指定。

**-p**, **--plan** _REGEXP_
> 使用匹配的计划。默认使用用户配置中的 `/user/plan*` 计划，否则使用默认计划。

**-l**, **--login**
> 仅登录客户机，不运行任何测试。

**-a**, **--ask**
> 只调配客户机，然后询问下一步做什么。

**--epel**
> 在客户机上启用 EPEL 仓库。

**--fips**
> 在客户机上启用 FIPS 模式。

**--install** _PACKAGE_
> 在客户机上安装指定软件包。可多次指定。

**--arch** _ARCH_
> 指定客户机的 CPU 架构。

**--help**
> 显示帮助信息。

# DESCRIPTION

**tmt try** 提供一个交互式会话来运行测试或在客户机上进行试验。它会调配一台客户机，运行当前工作目录中发现的测试，然后展示后续操作的菜单。如果未检测到任何测试，它会登录到客户机，让你开始动手实验。

用镜像名称指定客户机，例如 `tmt try fedora`。追加 `@HOW` 可为每台客户机选择调配方式，例如 `fedora@container` 或 `centos-stream-9@virtual`。将 `@connect` 与 FQDN 或 IP 地址一起使用可连接到已在运行的客户机，例如 `192.168.12.23@connect`。

# CAVEATS

如果当前目录中没有找到测试，**tmt try** 只会登录客户机。镜像可用性取决于资源调配后端。交互模式需要终端访问，某些镜像可能需要身份验证或特殊配置。

# INSTALL

```dnf: sudo dnf install tmt```

```brew: brew install tmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmt](/man/tmt)(1), [tmt-run](/man/tmt-run)(1), [podman](/man/podman)(1)
