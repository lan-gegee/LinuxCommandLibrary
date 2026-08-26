# TAGLINE

管理 X11 输入设备

# TLDR

**列出**所有输入设备

```xinput list```

**禁用**输入设备

```xinput disable id```

**启用**输入设备

```xinput enable id```

**列出设备属性**

```xinput list-props id```

**设置**设备属性值

```xinput set-prop id property value```

使设备与其主设备**分离**

```xinput float id```

将设备重新**附加**到主设备

```xinput reattach id master_id```

**测试**设备的输入事件

```xinput test id```

# SYNOPSIS

**xinput** [_COMMAND_] [_OPTIONS_] [_DEVICE_]

# DESCRIPTION

**xinput** 是一个用于列出可用输入设备、查询设备信息和更改 X Window System 中输入设备设置的工具。它可以控制键盘、鼠标、触摸板及其他输入设备。

# PARAMETERS

**list**
> 列出所有输入设备及其 ID

**enable ID**
> 启用输入设备

**disable ID**
> 禁用输入设备

**list-props ID**
> 列出设备的可配置属性

**set-prop ID PROPERTY VALUE**
> 设置属性值（支持 8、16 或 32 位格式）

**watch-props ID**
> 实时监视属性变化

**query-state ID**
> 查询设备的当前状态

**set-mode ID MODE**
> 将设备模式设置为 ABSOLUTE（绝对）或 RELATIVE（相对）

**set-button-map ID MAP**
> 将物理按钮重映射为逻辑按钮

**map-to-output ID OUTPUT**
> 将设备限制到特定的显示输出

**float ID**
> 使从设备与其主设备分离

**reattach ID MASTER_ID**
> 将从设备重新附加到另一个主设备

**create-master NAME**
> 创建新的主设备对

**remove-master ID**
> 移除主设备及其配对设备

**test ID**
> 注册扩展事件并显示数据

# CAVEATS

在 Xwayland 上，xinput 只影响连接到该 Xwayland 实例的 X11 客户端，不影响 Wayland 原生应用。配置更改可能不会跨会话保留；永久性更改请使用系统配置文件。

# HISTORY

**xinput** 是 X.Org 输入工具的一部分，提供对 XInput 扩展设备的命令行管理。

# INSTALL

```apt: sudo apt install xinput```

```dnf: sudo dnf install xinput```

```apk: sudo apk add xinput```

```zypper: sudo zypper install xinput```

```brew: brew install xinput```

```nix: nix profile install nixpkgs#xinput```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [xset](/man/xset)(1), [xmodmap](/man/xmodmap)(1), [setxkbmap](/man/setxkbmap)(1)
