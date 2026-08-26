# TAGLINE

读写 KDE Wallet 的命令行工具

# TLDR

列出默认文件夹中的**所有条目**

```kwallet-query kdewallet --list-entries```

列出**特定文件夹**中的条目

```kwallet-query kdewallet --list-entries --folder [folder_name]```

列出钱包中的**所有文件夹**

```kwallet-query kdewallet --list-entries --folder ""```

从文件夹中**读取密码**条目

```kwallet-query kdewallet --folder [folder] --read-password [entry]```

向文件夹**写入密码**（从 stdin 读取值）

```kwallet-query kdewallet --folder [folder] --write-password [entry] < [secret.txt]```

显示**帮助**

```kwallet-query --help```

# SYNOPSIS

**kwallet-query** _wallet_ [_options_]

# DESCRIPTION

**kwallet-query** 是一个用于读写 KDE Wallet 的命令行工具。它让脚本和命令行用户无需图形界面即可访问存储的密码和机密信息。

# PARAMETERS

**wallet**
> 要查询的钱包名称（通常为 "kdewallet"）

**-l, --list-entries**
> 列出指定文件夹中的条目

**-f, --folder FOLDER**
> 指定要查询的文件夹（空字符串表示列出所有文件夹）

**-r, --read-password ENTRY**
> 读取指定条目的密码

**-w, --write-password ENTRY**
> 写入指定条目的密码

**-h, --help**
> 显示帮助信息

# CAVEATS

查询前必须先解锁钱包。读取条目时，敏感数据会以明文形式显示。钱包守护进程 **kwalletd** 必须处于运行状态，否则查询将无法连接。

# HISTORY

**KWallet** 是 **KDE** 的凭据存储子系统，推出于 21 世纪初，相当于 KDE 版的 GNOME Keyring。**kwallet-query** 的加入为脚本和无头环境提供了非交互式、可脚本化的钱包内容访问接口，是图形化工具 **kwalletmanager** 的补充。

# INSTALL

```apt: sudo apt install kwallet6```

```apk: sudo apk add kwallet-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[secret-tool](/man/secret-tool)(1)
