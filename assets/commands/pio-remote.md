# TAGLINE

启用 PlatformIO 的远程开发功能

# TLDR

**启动远程代理**

```pio remote agent start```

**列出远程设备**

```pio remote device list```

**远程构建并上传**

```pio remote run --target upload```

**打开远程串口监视器**

```pio remote device monitor```

# SYNOPSIS

**pio remote** _command_ [_options_]

# PARAMETERS

**agent** _action_
> 管理远程代理（start、list）。

**device** _action_
> 远程设备操作。

**run**
> 执行远程构建/上传。

**test**
> 运行远程测试。

**-a**, **--agent** _name_
> 指定目标代理。

# DESCRIPTION

**pio remote** 用于启用 PlatformIO 的远程开发。可以在连接了硬件的远程机器上执行构建和上传。需要 PlatformIO 账户并运行远程代理。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-device](/man/pio-device)(1)
