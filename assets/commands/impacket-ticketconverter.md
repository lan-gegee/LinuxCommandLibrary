# TAGLINE

在 ccache 和 kirbi 格式之间转换 Kerberos 票据

# TLDR

**将 kirbi 票据转换为 ccache** 格式

```impacket-ticketConverter [ticket.kirbi] [ticket.ccache]```

**将 ccache 票据转换为 kirbi** 格式

```impacket-ticketConverter [ticket.ccache] [ticket.kirbi]```

**转换 base64 编码的票据**

```impacket-ticketConverter -b [encoded_ticket.txt] [ticket.ccache]```

# SYNOPSIS

**impacket-ticketConverter** [**-h**] [**-b**] _input_file_ _output_file_

# PARAMETERS

_input_file_
> kirbi（KRB-CRED）或 ccache 格式的源票据文件。格式会被自动检测。

_output_file_
> 转换后票据的目标文件名。

**-b, --base64**
> 在转换前先将输入票据从 base64 编码解码。

**-h, --help**
> 显示帮助信息并退出。

# DESCRIPTION

**impacket-ticketConverter** 在两种常见的 Kerberos 身份验证票据格式之间转换：**ccache**（Impacket 等 UNIX 工具使用）和 **kirbi** / KRB-CRED（Mimikatz 等 Windows 工具使用）。该工具通过检查文件的首个字节自动检测输入格式，并转换为相反的格式。

在经授权的安全评估中进行跨平台操作时，这很有用：在 Windows 上获取的票据需要交给基于 Linux 的工具使用，反之亦然。

# CAVEATS

属于 **Impacket** 工具集。该工具仅在 ccache 和 kirbi 格式之间转换；它不创建、修改或校验票据。需要安装 Python 和 Impacket 库。仅限在经授权的安全测试环境中使用。

# HISTORY

**Impacket** 最初由 **SecureAuth** 开发，现由 **Fortra's Core Security** 维护。它是一组用于处理网络协议的 Python 类，旨在帮助安全专业人员开展渗透测试和安全研究。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[impacket](/man/impacket)(1), [kinit](/man/kinit)(1)
