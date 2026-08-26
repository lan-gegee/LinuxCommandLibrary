# TAGLINE

终端中的 2FA TOTP 令牌管理 TUI

# TLDR

**打开 Aegis 加密备份**

```andcli -t aegis [path/to/backup.json]```

**打开 andOTP 备份文件**

```andcli [path/to/backup.json]```

**打开 KeePass 数据库**

```andcli -t keepass [path/to/database.kdbx]```

**指定自定义剪贴板命令**

```andcli -c [pbcopy] [path/to/backup]```

**从标准输入读取密码**

```echo "[password]" | andcli --passwd-stdin [path/to/backup]```

# SYNOPSIS

**andcli** [_options_] _file_

# PARAMETERS

**-t**, **--type** _type_
> 保险库类型：aegis、andotp、twofas、stratum、keepass 或 proton

**-c**, **--clipboard-cmd** _command_
> 自定义剪贴板命令（如 xclip、pbcopy）

**--passwd-stdin**
> 从标准输入读取解密密码

**-v**, **--version**
> 打印版本信息

**-h**, **--help**
> 打印帮助信息

# DESCRIPTION

**andcli** 是一个用于管理 TOTP 双因素认证令牌的终端用户界面。它读取从流行认证器应用导出的加密备份文件，包括 andOTP、Aegis、2FAS、Stratum/Authenticator Pro、KeePass（.kdbx）和 ProtonPass，然后在交互式 TUI 中显示令牌。所有数据仅保留在内存中，绝不写入磁盘。

该工具使用 Go 编写，基于 Bubbletea TUI 框架，支持 Vim 风格导航（j/k）、模糊搜索（/）、令牌可见性切换（Enter）以及复制到剪贴板（c/y）。

# CAVEATS

仅支持 TOTP 条目；不支持 HOTP 及其他 OTP 类型。需要来自受支持认证器应用的带密码保护的加密备份文件。

# HISTORY

**andcli** 由 **tjblackheart** 创建，是一个采用 MIT 许可证的开源 Go 项目。其名称源自最初支持的保险库格式之一 andOTP。

# INSTALL

```aur: yay -S andcli```

```nix: nix profile install nixpkgs#andcli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[oathtool](/man/oathtool)(1), [pass](/man/pass)(1)
