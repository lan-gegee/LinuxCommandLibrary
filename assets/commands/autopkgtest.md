# TAGLINE

为 Debian 软件包运行 DEP-8 测试

# TLDR

构建软件包并直接在系统上**运行全部测试**

```autopkgtest -- null```

运行软件包的**某个指定测试**

```autopkgtest --test-name=[test_name] -- null```

下载**指定软件包**并运行全部测试

```autopkgtest [package] -- null```

使用**全新根目录**（chroot）进行测试

```autopkgtest -- chroot [path/to/new_root]```

**不重新构建**软件包直接测试

```autopkgtest -B -- null```

# SYNOPSIS

**autopkgtest** [_options_] _source_ **--** _virtualization_

# DESCRIPTION

**autopkgtest** 按照 DEP-8（autopkgtest）规范运行 Debian 源码包中定义的测试。它支持多种虚拟化后端来提供隔离的测试环境。

该工具通过 **--** 分隔符将测试说明与执行环境分离。虚拟化后端（null、chroot、schroot、lxc、qemu 等）决定测试如何隔离。

# PARAMETERS

**--test-name=**_name_
> 只运行指定名称的测试。

**--skip-test=**_name_
> 跳过指定名称的测试。

**-B, --no-built-binaries**
> 测试前不构建软件包；使用现成的二进制文件。

**--setup-commands=**_commands_
> 在测试开始前于测试床中运行给定的 shell 命令。

**-U, --apt-upgrade**
> 测试前在测试床中运行 apt-get update 和 dist-upgrade。

**-s, --shell-fail**
> 测试失败时在测试床中打开一个 shell 以便调试。

**--shell**
> 每个测试结束后都在测试床中打开一个 shell。

**-o** _directory_, **--output-dir=**_directory_
> 将测试产物和日志写入指定目录。

# VIRTUALIZATION BACKENDS

**null**
> 直接在当前系统上运行测试（无隔离）

**chroot** _path_
> 使用 chroot 环境

**schroot** _name_
> 使用 schroot 环境

**lxc** _container_
> 使用 LXC 容器

**qemu** _image_
> 使用 QEMU 虚拟机

# CAVEATS

**null** 后端会直接修改系统，可能留下残余变更。chroot 及其他后端能提供更好的隔离。测试定义必须遵循 **debian/tests/control** 中的 DEP-8 规范。

# INSTALL

```aur: yay -S autopkgtest```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[dpkg-buildpackage](/man/dpkg-buildpackage)(1), [lxc](/man/lxc)(1), [schroot](/man/schroot)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/ci-team/autopkgtest)```

```[Documentation](https://wiki.debian.org/ContinuousIntegration/autopkgtest)```

<!-- verified: 2026-06-17 -->
