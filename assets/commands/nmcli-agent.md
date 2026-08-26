# TAGLINE

将 nmcli 作为代理守护进程运行，以响应 NetworkManager 的请求

# TLDR

将 nmcli 注册为**密钥代理（secret agent）**并监听密钥请求

```nmcli agent secret```

将 nmcli 注册为 **polkit 代理**并监听授权请求

```nmcli agent polkit```

将 nmcli 同时注册为**密钥代理和 polkit 代理**

```nmcli agent all```

# SYNOPSIS

**nmcli agent** _command_

# PARAMETERS

**secret, s**
> 作为 NetworkManager 密钥代理运行，以提供密码/凭据

**polkit, p**
> 作为 polkit 代理运行，以处理授权请求

**all, a**
> 同时作为密钥代理和 polkit 代理运行

# DESCRIPTION

**nmcli agent** 将 nmcli 作为代理守护进程运行，用于响应 NetworkManager 对密钥（密码、密钥）或 polkit 授权请求的需求。在没有桌面密钥代理或 polkit 代理的环境中，这非常有用。

作为**密钥代理**，当 NetworkManager 需要建立连接时，nmcli 可以提供 Wi-Fi 密码、VPN 凭据和其他密钥。它会在终端中提示用户输入所需的凭据。

作为 **polkit 代理**，nmcli 处理特权 NetworkManager 操作的授权提示，从而在没有图形化 polkit 代理的情况下也能进行命令行身份验证。

# CAVEATS

代理在前台运行，必须保持运行才能处理请求。每种类型的密钥代理或 polkit 代理一次只能注册一个。主要用于无头系统或纯终端环境。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-general](/man/nmcli-general)(1), [NetworkManager](/man/NetworkManager)(8), [polkit](/man/polkit)(8)
