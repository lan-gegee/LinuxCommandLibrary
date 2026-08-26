# TAGLINE

在文件之间创建链接

# TLDR

**创建符号链接**

```ln -s [target] [linkname]```

**创建硬链接**

```ln [target] [linkname]```

**创建符号链接（强制覆盖）**

```ln -sf [target] [linkname]```

**在目录中创建链接**

```ln -s [target] [directory/]```

**创建相对符号链接**

```ln -sr [target] [linkname]```

**详细输出**

```ln -sv [target] [linkname]```

# SYNOPSIS

**ln** [_options_] _target_ _linkname_

# PARAMETERS

_TARGET_
> 要链接到的文件或目录。

_LINKNAME_
> 链接的名称。

**-s**
> 创建符号链接（软链接）。

**-f**
> 强制执行，覆盖已存在的链接。

**-r**
> 创建相对符号链接。

**-v**
> 详细输出。

**-n**
> 不解引用符号链接。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ln** 在文件之间创建链接。硬链接共享同一个 inode；符号链接则是一种引用。

符号链接可以跨越文件系统并指向目录；硬链接不能。

# CAVEATS

硬链接不能跨文件系统。目标移动后符号链接可能失效。不允许对目录创建硬链接。

# HISTORY

ln 是传统的 **Unix** 命令，可追溯到最初的 Unix 系统，用于在文件之间创建链接。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[link](/man/link)(1), [unlink](/man/unlink)(1), [readlink](/man/readlink)(1)
