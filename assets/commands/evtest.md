# TAGLINE

输入设备事件监视与查询工具

# TLDR

**列出**所有检测到的输入设备

```sudo evtest```

显示指定设备的**事件**

```sudo evtest /dev/input/event[number]```

**独占抓取**设备（阻止其他应用接收事件）

```sudo evtest --grab /dev/input/event[number]```

**查询**特定按键或按钮的状态

```sudo evtest --query /dev/input/event[number] EV_KEY [KEY_A]```

# SYNOPSIS

**evtest** [**--grab**] _/dev/input/eventX_

**evtest** **--query** _/dev/input/eventX_ _event_type_ _event_code_

# PARAMETERS

**--grab**
> 使用 EVIOCGRAB 独占抓取设备，阻止其他进程接收事件。

**--query** _device_ _type_ _code_
> 查询特定按键/按钮/开关的状态。type 可以是 EV_KEY、EV_SW、EV_SND、EV_LED 或数字值。未按下时返回退出码 0，按下时返回 10。

# DESCRIPTION

**evtest** 显示来自 Linux 输入子系统设备驱动的信息。在捕获模式下，它会显示设备支持的所有事件，然后持续监视该设备并展示产生的全部事件，如按键、鼠标移动和触摸事件。

在查询模式下，它对特定按键、开关、声音或 LED 的状态执行一次性查询。

# CAVEATS

需要 root 权限才能读取 /dev/input/ 设备。抓取设备后，在 evtest 退出之前其他应用都无法收到事件。

# INSTALL

```apt: sudo apt install evtest```

```dnf: sudo dnf install evtest```

```pacman: sudo pacman -S evtest```

```apk: sudo apk add evtest```

```zypper: sudo zypper install evtest```

```nix: nix profile install nixpkgs#evtest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xinput](/man/xinput)(1), [libinput](/man/libinput)(1)
