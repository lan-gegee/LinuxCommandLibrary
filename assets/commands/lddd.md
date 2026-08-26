# TAGLINE

扫描系统中共享库链接损坏的软件包

# TLDR

查找存在**库链接损坏**问题的软件包

```lddd```

# SYNOPSIS

**lddd**

# DESCRIPTION

**lddd** 扫描系统中共享库链接损坏的软件包。它会识别那些依赖于已被移除或已更新库的二进制文件，从而指出可能需要重新构建的软件包。

该工具专为 Arch Linux 系统设计，有助于在库更新后维护系统健康状态。

# CAVEATS

仅在 Arch Linux 上可用。在装有大量软件包的系统上可能耗时较长。完整扫描系统需要 root 权限。

# SEE ALSO

[ldd](/man/ldd)(1), [pacman](/man/pacman)(8), [checkupdates](/man/checkupdates)(8)
