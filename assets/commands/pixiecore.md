# TAGLINE

一体化 PXE 网络启动服务器

# TLDR

**从内核和 initrd 启动**

```sudo pixiecore boot [vmlinuz] [initrd.img]```

**附带内核命令行参数启动**

```sudo pixiecore boot [vmlinuz] [initrd.img] --cmdline "[console=ttyS0]"```

**与现有 DHCP 服务器共存启动**

```sudo pixiecore boot [vmlinuz] [initrd.img] --dhcp-no-bind```

**通过外部 API 端点提供启动配置**

```sudo pixiecore api [http://localhost:8080]```

**监听特定地址**

```sudo pixiecore boot [vmlinuz] [initrd.img] --listen-addr [192.168.1.1]```

**启用调试输出**

```sudo pixiecore boot [vmlinuz] [initrd.img] --debug```

# SYNOPSIS

**pixiecore** _command_ [_options_] [_args_]

# PARAMETERS

**boot** _KERNEL_ _INITRD_...
> 向所有客户端提供静态启动配置。

**api** _URL_
> 将启动配置委托给外部 HTTP API（通过 MAC 地址实现每台机器的配置）。

**--cmdline** _ARGS_
> 传递给启动机器的内核命令行参数。

**--listen-addr** _IP_
> 监听地址（默认：所有接口）。

**--port** _N_
> 用于提供启动文件的 HTTP 端口（默认：80）。

**--dhcp-no-bind**
> 不绑定 DHCP 端口；作为 ProxyDHCP 与现有 DHCP 服务器协同工作。

**--log-timestamps**
> 为日志输出添加时间戳。

**--debug**
> 启用详细的调试输出。

# DESCRIPTION

**pixiecore** 是一个一体化的网络启动服务器，将 DHCP/ProxyDHCP、TFTP 和 HTTP 服务整合进单个二进制文件，用于在本地网络上对机器进行 PXE 引导。传统 PXE 方案需要分别配置 DHCP、TFTP 和启动菜单服务，而 pixiecore 在内部处理整个启动过程，并且可以与现有 DHCP 服务器共存，无需改动网络的任何 DHCP 配置。

该工具提供三种运行模式。静态启动模式向所有客户端提供相同的内核和 initrd 配置。API 模式将启动配置委托给外部 HTTP 服务，可根据 MAC 地址或其他标识符进行每台机器的定制，特别适合大规模部署。快速模式则为常见 Linux 发行版提供现成的预设，只需极少配置即可让机器通过网络启动。

# CAVEATS

绑定 DHCP/TFTP 端口需要 root 或同等权限。若不使用 **--dhcp-no-bind**，可能与现有 DHCP 服务器冲突。网络必须允许广播流量。仅支持 BIOS PXE 和 iPXE；对 UEFI 的支持有限。

# HISTORY

**Pixiecore** 由 **Google** 创建，用于简单、API 驱动的网络启动。它省去了单独配置 DHCP/TFTP 的需要，简化了 PXE 部署。

# INSTALL

```nix: nix profile install nixpkgs#pixiecore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnsmasq](/man/dnsmasq)(1), [pxelinux](/man/pxelinux)(1), [tftp](/man/tftp)(1)
