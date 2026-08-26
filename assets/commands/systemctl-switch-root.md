# TAGLINE

切换到真正的根文件系统

# TLDR

**切换**到新的根文件系统

```systemctl switch-root [/path/to/new_root]```

切换并运行**指定的 init**

```systemctl switch-root [/path/to/new_root] [/sbin/init]```

以**详细输出**方式切换

```systemctl switch-root [/path/to/new_root] -v```

# SYNOPSIS

**systemctl switch-root** _ROOT_ [_INIT_]

# PARAMETERS

**-v, --verbose**
> 启用详细输出

_ROOT_
> 新根文件系统的路径

_INIT_
> 要执行的 init 程序（默认：systemd）

# DESCRIPTION

**systemctl switch-root** 将系统从 initramfs 切换到真正的根文件系统，并启动新的系统管理器。这是 initramfs 设置好真正的根之后的最后一步启动流程。

此命令通常由 initramfs 在内部调用来完成启动过程，而非手动调用。

# CAVEATS

仅供 initramfs 在启动过程中使用。使用不当可能导致系统无法启动。新的根必须包含有效的 init 系统。旧根上的所有进程都会被终止。

# HISTORY

**switch-root** 子命令将 initramfs 到真正根文件系统的切换流程规范化到 systemd 中，取代了传统的 pivot_root 操作。

# SEE ALSO

[systemctl](/man/systemctl)(1), [pivot_root](/man/pivot_root)(2)
