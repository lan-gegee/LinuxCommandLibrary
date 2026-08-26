# TAGLINE

将可执行文件压缩为自解压归档

# TLDR

**就地压缩可执行文件**

```bzexe [path/to/executable]```

**压缩多个可执行文件**

```bzexe [executable1] [executable2]```

**解压之前压缩过的可执行文件**

```bzexe -d [path/to/executable]```

# SYNOPSIS

**bzexe** [**-d**] _file..._

# DESCRIPTION

**bzexe** 就地压缩可执行文件，创建自解压的可执行文件，在运行时会自动解压并执行。原始文件会以波浪号（~）后缀保存作为备份。

运行压缩后的可执行文件时，它会将自身透明地解压到临时位置再执行。这是用执行速度换取磁盘空间，对存储空间有限的系统很有用。

例如，压缩 **/bin/cat** 会创建：
- **/bin/cat** - 自解压的可执行文件
- **/bin/cat~** - 原始未压缩的二进制文件（备份）

# PARAMETERS

**-d**
> 解压指定的可执行文件而不是压缩它们

# CAVEATS

压缩后的可执行文件以 shell 脚本实现，可能带来安全问题。它依赖 **PATH** 环境变量来查找 **bzip2** 以及 **tail**、**chmod**、**ln** 和 **sleep** 等工具。

文件属性可能无法完全保留。压缩后你可能需要手动使用 **chmod** 修复权限或使用 **chown** 修复所有者。

确认压缩后的可执行文件能正常工作后，即可删除备份文件（带 ~ 后缀）。

# INSTALL

```apt: sudo apt install bzip2```

```dnf: sudo dnf install bzip2```

```pacman: sudo pacman -S bzip2```

```zypper: sudo zypper install bzip2```

```brew: brew install bzip2```

```nix: nix profile install nixpkgs#bzip2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bzip2](/man/bzip2)(1), [bunzip2](/man/bunzip2)(1), [gzexe](/man/gzexe)(1)

# RESOURCES

```[Source code](https://gitlab.com/bzip2/bzip2)```

```[Homepage](https://sourceware.org/bzip2/)```

<!-- verified: 2026-06-22 -->
