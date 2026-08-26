# TAGLINE

用于创建自定义 Encode 模块的 Perl 工具

# TLDR

**从 UCM 文件创建 Encode 模块**

```enc2xs -M [ModuleName] [encoding.ucm]```

**构建并安装**

```enc2xs -C [encoding.ucm]```

**为指定** Perl 版本生成

```enc2xs --perl [/usr/bin/perl] [encoding.ucm]```

# SYNOPSIS

**enc2xs** [_options_] _ucm-files_

# PARAMETERS

_UCM-FILES_
> UCM（Unicode Character Map）文件。

**-M** _NAME_
> 模块名称。

**-C**
> 编译并安装。

**-o** _FILE_
> 输出文件。

**--perl** _PATH_
> Perl 解释器路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**enc2xs** 是一个 Perl 工具，用于从 UCM（Unicode Character Map）文件创建自定义 Encode 模块。它将字符编码定义编译为 Perl 模块。

该工具用于向 Perl 的 Encode 系统添加对非标准或专有字符编码的支持。UCM 文件定义字节序列与 Unicode 码位之间的映射。

enc2xs 生成可编译为可加载 Perl 模块的 XS 代码。

# CAVEATS

需要 Perl 开发环境。UCM 格式必须正确。XS 编译需要 C 编译器。主要面向编码开发者。

# HISTORY

enc2xs 是 Perl 核心中 **Encode** 模块的一部分，支持创建自定义字符编码支持。它使 Perl 能够处理标准发行版未内置的编码。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-dev```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl](/man/perl)(1)
