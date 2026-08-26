# TAGLINE

控制由 NetworkManager 管理的无线接口软件无线电开关

# TLDR

显示 **Wi-Fi 状态**

```nmcli radio wifi```

**打开或关闭 Wi-Fi**

```nmcli radio wifi [on|off]```

显示 **WWAN 状态**（移动宽带）

```nmcli radio wwan```

**打开或关闭 WWAN**

```nmcli radio wwan [on|off]```

显示**两个开关的状态**

```nmcli radio```

**同时打开或关闭两个开关**

```nmcli radio all [on|off]```

# SYNOPSIS

**nmcli radio** [_switch_] [_on_|_off_]

# PARAMETERS

**wifi, w**
> 控制或显示 Wi-Fi 无线电状态

**wwan, ww**
> 控制或显示 WWAN（移动宽带）无线电状态

**all, a**
> 同时控制所有无线电开关

**on**
> 启用指定的无线电

**off**
> 禁用指定的无线电

# DESCRIPTION

**nmcli radio** 控制 NetworkManager 所管理无线接口的软件无线电开关。这相当于飞行模式功能，允许独立地启用或禁用 Wi-Fi 和移动宽带无线电。

禁用无线电开关会关闭相应的硬件发射器，阻止任何无线通信。这与仅仅断开连接不同——无线电本身被关闭了。

如果不带 on/off 参数，该命令会显示指定无线电的当前状态。

# CAVEATS

软件无线电控制依赖于硬件和驱动支持。某些笔记本电脑有物理无线电开关，其优先级高于软件控制。启用无线电并不会自动连接到网络；它只是让硬件可用于连接。

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-networking](/man/nmcli-networking)(1), [rfkill](/man/rfkill)(8), [NetworkManager](/man/NetworkManager)(8)
