# TAGLINE

Koji 的命令行客户端，Koji 是 Fedora、CentOS 使用的构建系统

# TLDR

执行**子命令**

```koji [subcommand]```

测试与 kojihub 的**连通性**

```koji moshimoshi```

显示**全局帮助**

```koji -h```

显示**所有命令**

```koji help```

显示**特定子命令**的帮助

```koji [subcommand] -h```

显示**版本号**

```koji version```

# SYNOPSIS

**koji** [_options_] _subcommand_ [_arguments_]

# PARAMETERS

**moshimoshi**
> 测试与 koji hub 的连通性

**help**
> 显示所有可用命令

**build**
> 提交构建任务

**tag-build**
> 为构建打标签

**download-build**
> 下载构建产物

**buildinfo**
> 显示构建信息

**call**
> 执行任意 XML-RPC 调用

**version**
> 显示版本信息

# DESCRIPTION

**koji** 是 Koji 的命令行客户端，Koji 是 Fedora、CentOS 及其他基于 RPM 的发行版使用的构建系统。它通过与 Koji hub 交互来提交构建、管理标签并下载软件包。

Koji 负责整个构建过程，包括软件包构建、测试和分发。开发者用它提交源码软件包，以便在多种架构上进行编译。

# CAVEATS

需要正确的身份验证配置。某些操作需要特定权限。需要能够访问 Koji hub 的网络。

# HISTORY

Koji 由 Red Hat 开发，于 **2007 年**发布，作为 Fedora 的构建系统。"Koji" 一词来自日语中表示酿造所用曲霉（酵母/霉菌）的词，呼应其在"酿造"软件包中的角色。

# INSTALL

```dnf: sudo dnf install koji```

```brew: brew install koji```

```nix: nix profile install nixpkgs#koji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mock](/man/mock)(1), [rpmbuild](/man/rpmbuild)(8)
