# TAGLINE

macOS 上 Apple Passwords 的 CLI

# TLDR

**启动后台守护进程**

```apw start```

向守护进程进行**身份验证**

```apw auth```

**交互式搜索密码**

```apw pw```

以 JSON 格式**列出指定域名的密码**

```apw pw list [domain.com]```

**交互式搜索 OTP 令牌**

```apw otp```

以 JSON 格式**列出指定域名的 OTP 密钥**

```apw otp list [domain.com]```

# SYNOPSIS

**apw** _command_ [_options_]

# PARAMETERS

**start**
> 启动后台守护进程

**auth**
> 让 CLI 向守护进程进行身份验证

**pw**
> 交互式列出和搜索密码

**pw list** [_domain_]
> 以 JSON 格式列出密码，可按域名过滤

**otp**
> 交互式列出和搜索 OTP 令牌

**otp list** [_domain_]
> 以 JSON 格式列出 OTP 密钥，可按域名过滤

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本号

# DESCRIPTION

**apw**（Apple Passwords）是访问 macOS 上 Apple Passwords（前身为 iCloud 钥匙串）的命令行接口。它无需打开系统设置即可通过 Shell 访问 iCloud 同步的登录凭据和 OTP 密钥。该工具采用守护进程架构，由后台进程与 macOS 内置的 Passwords 辅助工具通信。

身份验证使用 macOS 原生提示（触控 ID 或密码对话框），因此凭据不会以不安全的方式暴露。**list** 子命令输出 JSON，便于脚本编写和自动化。

# CAVEATS

需要 **macOS 14 (Sonoma) 或更高版本**。查询前守护进程必须已运行并通过身份验证。每次系统重启后都需要重新进行身份验证。

# HISTORY

**apw** 由 **Ben Dews**（bendews）开发，使用 TypeScript 编写、基于 Deno 并编译为静态二进制文件。采用 GPL-3.0 许可证，首次发布于 2024 年 3 月。

# INSTALL

```aur: yay -S apw```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pass](/man/pass)(1), [keychain](/man/keychain)(1)
