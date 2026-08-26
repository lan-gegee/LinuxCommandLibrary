# TAGLINE

比较 Arch 软件包文件差异

# TLDR

以 **tar 内容列表**模式比较软件包文件（默认）

```pkgctl diff -l path/to/file```

使用 **diffoscope** 比较软件包文件

```pkgctl diff -d path/to/file```

比较软件包的 **.PKGINFO** 文件

```pkgctl diff -p path/to/file```

比较软件包的 **.BUILDINFO** 文件

```pkgctl diff -b path/to/file```

# SYNOPSIS

**pkgctl diff** [_options_] _file|pkgname_

# PARAMETERS

**-l**, **--list**
> 使用 tar 内容列表模式进行比较（默认）

**-d**, **--diffoscope**
> 使用 diffoscope 进行详细差异比较

**-p**, **--pkginfo**
> 比较 .PKGINFO 元数据文件

**-b**, **--buildinfo**
> 比较 .BUILDINFO 文件

# DESCRIPTION

**pkgctl diff** 将本地构建的 **.pkg.tar.zst** 与官方 Arch 仓库中当前发布的同一软件包（或另一个本地软件包文件）进行比较。它是 Arch 软件包维护者在发布前的标准健全性检查，可以暴露意外的文件移动、丢失的二进制文件、soname 变更，以及非预期的 **.PKGINFO**/**.BUILDINFO** 漂移。

不带标志时以 **--list** 模式运行，比较 tar 清单。使用 **--diffoscope** 可查看字节级差异（慢但详尽），**--pkginfo** 用于运行时元数据，**--buildinfo** 用于验证与可重现性相关的字段（如编译器标志和构建依赖）。

# CAVEATS

**--diffoscope** 需要 **diffoscope** 软件包，对包含大型编译产物的软件包可能非常慢。当只传入裸 _pkgname_ 时，**pkgctl diff** 会从镜像站下载已发布的软件包，因此需要可用的网络和配置好的 Pacman 镜像列表。

# HISTORY

属于 **pkgctl** 的一部分，后者是面向官方仓库维护者的 Arch Linux 软件包控制工具。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [diffoscope](/man/diffoscope)(1)
