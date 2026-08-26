# TAGLINE

重启系统

# TLDR

**重启**系统

```systemctl reboot```

重启进入**固件**设置界面

```systemctl reboot --firmware-setup```

**强制**立即重启

```systemctl reboot -f```

一次性**重启**进入指定的引导加载器条目

```systemctl reboot --boot-loader-entry=[entry_id]```

**安排**在特定时间重启

```systemctl reboot --when=+30min```

# SYNOPSIS

**systemctl reboot** [_OPTIONS_]

# PARAMETERS

**-f, --force**
> 跳过服务的优雅关闭

**--force --force** (-ff)
> 立即重启，不做清理（危险）

**--firmware-setup**
> 重启进入 BIOS/UEFI 固件设置菜单

**--no-wall**
> 不向用户发送 wall 消息

**--boot-loader-menu=** _TIMEOUT_
> 重启进入引导加载器菜单，并按指定超时时间显示它

**--boot-loader-entry=** _ID_
> 一次性重启进入指定的引导加载器条目（使用 `--boot-loader-entry=help` 可列出可用条目）

**--when=** _TIMESTAMP_
> 安排在特定时间重启（使用 `--when=cancel` 可取消已安排的重启）

# DESCRIPTION

**systemctl reboot** 重启系统：先优雅地停止所有服务并卸载文件系统，然后触发硬件复位。

**--firmware-setup** 选项会设置一个 EFI 变量，告知固件在下次启动时进入设置模式。这样无需在恰当时机按键即可进入 UEFI 设置。

# CAVEATS

强制模式可能导致数据丢失。固件设置功能取决于 UEFI 实现。某些系统可能不支持 firmware-setup 标志。

# HISTORY

**reboot** 子命令与 systemd 的关机基础设施集成，提供计划重启和固件设置入口等传统 reboot 命令不具备的功能。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl-poweroff](/man/systemctl-poweroff)(1), [systemctl-halt](/man/systemctl-halt)(1), [systemctl-soft-reboot](/man/systemctl-soft-reboot)(1), [reboot](/man/reboot)(8), [shutdown](/man/shutdown)(8)
