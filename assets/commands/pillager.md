# TAGLINE

在文件系统中搜刮敏感信息

# TLDR

**扫描当前目录中的机密信息**

```pillager hunt .```

**启动交互式 TUI 扫描器**

```pillager```

# SYNOPSIS

**pillager** [_command_] [_options_] [_path_]

# DESCRIPTION

**pillager** 是一个文件系统扫描器，递归搜索目录中的敏感信息，如 API 密钥、密码和凭证。它使用并发工作线程实现快速扫描，并采用 Gitleaks 规则进行模式匹配。发现的机密可以发送到远程目的地，包括 S3/MinIO、webhook 或 Sliver C2 战利品库。

# CAVEATS

仅限防御性、教育性以及经授权的安全研究用途。

# HISTORY

**pillager** 由 **Britton Hayes**（brittonhayes）创建，用 **Go** 编写。

# INSTALL

```aur: yay -S pillager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitleaks](/man/gitleaks)(1), [trufflehog](/man/trufflehog)(1), [grep](/man/grep)(1)
