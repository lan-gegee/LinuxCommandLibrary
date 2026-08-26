# TAGLINE

通过 I2C 进行 DDC/CI 显示器控制

# TLDR

**列出**所有兼容的显示器

```ddcutil detect```

**将亮度设置**为 50%

```ddcutil -d [1] setvcp 10 [50]```

**将对比度提高**5%

```ddcutil -d [1] setvcp 12 + [5]```

**读取**所有显示器设置

```ddcutil -d [1] getvcp ALL```

# SYNOPSIS

**ddcutil** [_options_] _command_ [_arguments_]

# DESCRIPTION

**ddcutil** 通过 I2C 总线通信使用 DDC/CI（Display Data Channel Command Interface）协议查询和修改显示器设置。它可以控制亮度、对比度、输入源、色温以及许多原本需要按物理按钮或操作 OSD 菜单才能调整的显示器参数。

该工具通过 I2C 总线接口与显示器通信，这需要 i2c-dev 内核模块。每台显示器都暴露一组可读写的 VCP（Virtual Control Panel）特性。不同显示器支持的特性不同，ddcutil 可以查询能力信息来发现特定显示器支持哪些特性。

常见用例包括编写脚本按时间段调整亮度、自动切换显示器输入源、保存/恢复显示器配置。这对手动调节十分繁琐的多显示器环境特别有价值，也适用于需要对显示属性进行程序化控制的无障碍场景。该工具还支持通过 SSH 对无头系统的显示器进行远程管理。

# PARAMETERS

**detect**
> 列出已连接的支持 DDC 的显示器

**getvcp** _feature_
> 读取 VCP 特性的值

**setvcp** _feature_ _value_
> 设置 VCP 特性的值

**-d, --display** _num_
> 选择显示器编号

**vcpinfo** _feature_
> 显示 VCP 特性信息

**capabilities**
> 查询显示器能力

# VCP FEATURES

**0x10**
> 亮度

**0x12**
> 对比度

**0x60**
> 输入源

**ALL**
> 所有受支持的特性

# CAVEATS

需要 i2c-dev 模块：`modprobe i2c-dev`。可能需要将用户加入 i2c 组。并非所有显示器都支持 DDC/CI。某些特性可能是只读的。

# INSTALL

```apt: sudo apt install ddcutil```

```dnf: sudo dnf install ddcutil```

```pacman: sudo pacman -S ddcutil```

```apk: sudo apk add ddcutil```

```zypper: sudo zypper install ddcutil```

```brew: brew install ddcutil```

```nix: nix profile install nixpkgs#ddcutil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [modprobe](/man/modprobe)(8)

# RESOURCES

```[Source code](https://github.com/rockowitz/ddcutil)```

```[Documentation](https://www.ddcutil.com)```

<!-- verified: 2026-07-11 -->
