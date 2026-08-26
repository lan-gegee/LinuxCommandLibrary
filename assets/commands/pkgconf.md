# TAGLINE

查询库的编译和链接标志

# TLDR

**获取编译器标志**

```pkgconf --cflags [library]```

**获取链接器标志**

```pkgconf --libs [library]```

**检查库是否存在**

```pkgconf --exists [library] && echo "Found"```

**获取版本**

```pkgconf --modversion [library]```

**列出所有软件包**

```pkgconf --list-all```

# SYNOPSIS

**pkgconf** [_options_] _packages_...

# PARAMETERS

**--cflags**
> 编译器标志。

**--libs**
> 链接器标志。

**--exists**
> 检查是否存在。

**--modversion**
> 软件包版本。

**--list-all**
> 列出所有软件包。

**--variable** _name_
> 获取变量的值。

**--print-requires**
> 显示依赖项。

# DESCRIPTION

**pkgconf** 是一个帮助配置库的编译器和链接器标志的程序。它是 pkg-config 的直接替代品，具有更好的性能和更多特性。

# EXAMPLES

```bash
# Compile with library
gcc $(pkgconf --cflags --libs openssl) -o prog prog.c

# Check version requirement
pkgconf --atleast-version=1.1.0 openssl

# Get library directory
pkgconf --variable=libdir openssl

# In Makefile
CFLAGS += $(shell pkgconf --cflags gtk+-3.0)
LDFLAGS += $(shell pkgconf --libs gtk+-3.0)
```

# ENVIRONMENT

```bash
PKG_CONFIG_PATH   # Additional .pc file paths
PKG_CONFIG_LIBDIR # Override default paths
```

# CAVEATS

读取 .pc 文件。与 pkg-config 兼容。大多数构建系统都在使用它。

# HISTORY

pkgconf 由 **William Pitcock** 开发，是 freedesktop.org 的 pkg-config 更轻量、更快速的替代方案。

# INSTALL

```apt: sudo apt install pkgconf-bin```

```dnf: sudo dnf install pkgconf```

```pacman: sudo pacman -S pkgconf```

```apk: sudo apk add pkgconf```

```zypper: sudo zypper install pkgconf```

```brew: brew install pkgconf```

```nix: nix profile install nixpkgs#pkgconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkg-config](/man/pkg-config)(1), [gcc](/man/gcc)(1), [make](/man/make)(1)
