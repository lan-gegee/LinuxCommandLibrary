# TAGLINE

将系统挂起到内存

# TLDR

**挂起到内存（S3）**

```sudo pm-suspend```

**唤醒后若屏幕仍无显示则点亮显示器**

```sudo pm-suspend --quirk-dpms-on```

**唤醒时重新 POST 视频 BIOS**

```sudo pm-suspend --quirk-vbe-post```

**保存/恢复 VGA 卡的 PCI 配置**

```sudo pm-suspend --quirk-save-pci```

**将有效的 quirk 持久保存到最近已知可用数据库**

```sudo pm-suspend --store-quirks-as-lkw```

# SYNOPSIS

**pm-suspend** [_--quirk-*_] [_--store-quirks-as-lkw_] [_--help_]

# PARAMETERS

**--quirk-dpms-on**
> 唤醒后若显示器仍无显示，用 DPMS 点亮它。

**--quirk-dpms-suspend**
> 挂起前用 DPMS 关闭显示器。

**--quirk-radeon-off**
> 挂起前禁用 Radeon 显示，唤醒时重新启用（旧款 ThinkPad）。

**--quirk-s3-bios**
> S3 唤醒过程中调用视频 BIOS。

**--quirk-s3-mode**
> 将显卡设置为 VGA 文本模式，然后在唤醒时调用 BIOS。

**--quirk-vbe-post**
> 唤醒时通过 VESA BIOS 对显卡重新 POST。

**--quirk-vbemode-restore**
> 在挂起前后保存和恢复 VESA 模式，防止 X 显示损坏。

**--quirk-vbestate-restore**
> 在挂起前后保存和恢复底层视频状态。

**--quirk-vga-mode-3**
> 唤醒时强制进入 VGA 文本模式 3。

**--quirk-save-pci**
> 保存并恢复 VGA 卡的 PCI 配置空间。

**--store-quirks-as-lkw**
> 若本次调用成功，将所用 quirks 写入 `/var/cache/pm-utils/last_known_working.quirkdb`，以便下次自动应用。

**--help**
> 显示帮助。

# DESCRIPTION

**pm-suspend** 让机器进入 ACPI S3 状态（挂起到内存）。大多数设备会断电，但系统状态保留在 RAM 中，因此几乎可以立即恢复，代价是持续的少量耗电。典型的笔记本电脑靠电池可以维持 S3 一到三天。

**pm-suspend** 是 **pm-utils** 的一部分。它在睡眠前和恢复时分别运行 `/etc/pm/sleep.d/` 和 `/usr/lib/pm-utils/sleep.d/` 中的钩子脚本。钩子的第一个参数是 `suspend`/`resume`（或 `hibernate`/`thaw`）：

```bash
#!/bin/sh
case "$1" in
    suspend|hibernate) : # before sleep ;;
    resume|thaw)       : # after wake ;;
esac
```

视频硬件是恢复失败最常见的原因；`--quirk-*` 标志提供了各种已知问题的变通方法。可以使用 `pm-suspend --auto-quirks`（如果发行版提供），或将 `--store-quirks-as-lkw` 与能解决问题的 quirks 结合使用使其持久生效。

# CAVEATS

在基于 systemd 的发行版上已被弃用；建议改用 **systemctl suspend**（它使用 systemd-logind 和 systemd-sleep）。需要 root 权限和正常的 ACPI/内核挂起路径。正确的 `--quirk-*` 标志组合因硬件而异；排查唤醒黑屏问题时请逐一尝试。

# HISTORY

**pm-utils** 由 **Richard Hughes**、**Peter Jones** 以及 Fedora/openSUSE 电源管理团队于 2000 年代后期开发，用于取代较早基于 `hal` 的脚本。它曾是大多数 Linux 发行版的标准挂起/休眠前端，直到 2012-2015 年间被 **systemd-logind** 和 **systemd-sleep** 取代。

# INSTALL

```apk: sudo apk add pm-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [rtcwake](/man/rtcwake)(8)
