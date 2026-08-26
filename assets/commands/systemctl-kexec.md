# TAGLINE

使用 kexec 快速路径重启

# TLDR

快速 **kexec** 重启

```systemctl kexec```

未加载 kexec 内核时**回退**到正常重启

```systemctl kexec --force```

# SYNOPSIS

**systemctl kexec** [_OPTIONS_]

# PARAMETERS

**-f**, **--force**
> 在没有 kexec 内核的情况下继续执行，改为执行正常重启。如果指定两次，则跳过服务关闭过程并立即重启（可能导致数据丢失）。

# DESCRIPTION

**systemctl kexec** 通过 kexec 关闭并重启系统。kexec 会直接加载并引导新内核，无需经过 BIOS/UEFI 固件。由于跳过了硬件初始化，重启速度明显更快。

必须事先加载好 kexec 内核（例如通过 `kexec -l`），否则此命令会失败。如果没有已加载的内核，可以使用 `--force` 回退到正常重启。

# CAVEATS

需要先用 `kexec -l` 预加载内核。由于跳过了固件初始化，某些硬件可能出现问题。并非所有硬件都能可靠支持 kexec。启用 Secure Boot 时可能无法工作。

# HISTORY

**kexec** 子命令将 Linux 的 kexec 功能与 systemd 的关机流程集成在一起，使对启动时间要求苛刻的环境能够实现快速重启。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-reboot](/man/systemctl-reboot)(1), [kexec](/man/kexec)(8)
