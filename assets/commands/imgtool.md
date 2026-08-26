# TAGLINE

管理 MCUboot 固件镜像

# TLDR

**创建 MCUboot 镜像**

```imgtool create --key [key.pem] --align 4 --version 1.0.0 [app.bin] [signed.bin]```

**签名镜像**

```imgtool sign --key [key.pem] [input.bin] [output.bin]```

**获取镜像信息**

```imgtool getinfo [image.bin]```

**生成密钥**

```imgtool keygen --key [key.pem] --type rsa-2048```

# SYNOPSIS

**imgtool** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的操作。

**create**
> 创建已签名的镜像。

**sign**
> 对现有镜像进行签名。

**getinfo**
> 显示镜像信息。

**keygen**
> 生成签名密钥。

**--key** _FILE_
> 密钥文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**imgtool** 用于管理 MCUboot 固件镜像。它创建、签名和检查与引导加载程序兼容的镜像。

该工具是安全启动工作流中不可或缺的一环。它负责处理镜像头部、签名和版本信息。

# CAVEATS

属于 MCUboot 项目。使用特定的镜像格式。需要加密密钥。

# HISTORY

imgtool 是 **MCUboot** 的一部分，这是一个面向微控制器的开源安全引导加载程序。

# INSTALL

```apt: sudo apt install mame-tools```

```dnf: sudo dnf install mame-tools```

```pacman: sudo pacman -S mame-tools```

```zypper: sudo zypper install mame-tools```

```nix: nix profile install nixpkgs#mame-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1)
