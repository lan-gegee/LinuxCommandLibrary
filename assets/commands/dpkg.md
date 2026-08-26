# TAGLINE

低层 Debian 软件包管理器

# TLDR

**安装**一个软件包

```sudo dpkg -i [path/to/file.deb]```

**移除**一个软件包

```sudo dpkg -r [package]```

**列出**已安装的软件包

```dpkg -l [pattern]```

列出一个软件包的**内容**

```dpkg -L [package]```

列出**本地软件包文件**的内容

```dpkg -c [path/to/file.deb]```

查找哪个软件包**拥有**某个文件

```dpkg -S [path/to/file]```

**彻底清除**一个软件包（包括配置文件）

```sudo dpkg -P [package]```

显示软件包**状态**

```dpkg -s [package]```

# SYNOPSIS

**dpkg** [_options_] _action_ [_package_|_file_]

# DESCRIPTION

**dpkg** 是基于 Debian 的系统的低层软件包管理器。它负责 .deb 软件包的安装、卸载和管理。**apt** 和 **apt-get** 等更高层的工具在内部使用 dpkg。

# PARAMETERS

**-i, --install file.deb**
> 从 .deb 文件安装软件包

**-r, --remove package**
> 卸载软件包（保留配置文件）

**-P, --purge package**
> 卸载软件包及其配置文件

**-l, --list pattern**
> 列出匹配模式的软件包

**-L, --listfiles package**
> 列出某软件包安装的文件

**-c, --contents file.deb**
> 列出 .deb 文件的内容

**-S, --search path**
> 查找拥有某个文件的软件包

**-s, --status package**
> 显示软件包状态详情

**--configure package**
> 配置已解包但未配置的软件包

**--unpack file.deb**
> 只解包软件包而不进行配置

**--get-selections** [_pattern_]
> 获取软件包选择列表

**--set-selections**
> 从标准输入设置软件包选择

**--audit**, **-C**
> 搜索未完全安装的软件包并给出修复建议。

**--force-**_things_
> 覆盖安全检查（例如 **--force-all**、**--force-overwrite**）。请谨慎使用。

**--no-act**, **--dry-run**, **--simulate**
> 只显示将要执行的操作，而不实际更改。

# CAVEATS

dpkg 不会自动处理依赖关系。请使用 **apt** 或 **apt-get** 来解决依赖。默认情况下，卸载软件包时会保留配置文件。

# HISTORY

**dpkg** 由 **Ian Murdock** 于 **1994 年**为 **Debian** 项目创建，随后由成为其主力开发者的 **Ian Jackson** 用 C 语言重写。它至今仍是基于 Debian 的系统上软件包管理的基石。

# INSTALL

```apt: sudo apt install dpkg```

```dnf: sudo dnf install dpkg```

```pacman: sudo pacman -S dpkg```

```apk: sudo apk add dpkg```

```zypper: sudo zypper install dpkg```

```brew: brew install dpkg```

```nix: nix profile install nixpkgs#dpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg-deb](/man/dpkg-deb)(1), [dpkg-query](/man/dpkg-query)(1)
