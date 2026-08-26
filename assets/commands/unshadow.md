# TAGLINE

合并 passwd 和 shadow 文件以供审计

# TLDR

合并**系统**的 passwd 和 shadow 文件

```sudo unshadow /etc/passwd /etc/shadow```

合并**任意**文件

```sudo unshadow [path/to/passwd] [path/to/shadow]```

# SYNOPSIS

**unshadow** _PASSWD_FILE_ _SHADOW_FILE_

# DESCRIPTION

**unshadow** 将 /etc/passwd 和 /etc/shadow 文件合并为传统的 Unix 密码文件格式。John the Ripper 等密码破解工具需要这种统一格式。

该工具是 John the Ripper 项目的一部分，用于在获授权的密码安全审计中准备待分析的密码哈希。

# CAVEATS

读取 shadow 文件需要 root 权限。仅应用于获授权的安全测试。输出包含敏感的密码哈希。

# HISTORY

**unshadow** 作为 **John the Ripper** 密码破解项目的一部分开发，用于处理将密码哈希分离到 shadow 文件中的现代 Unix 系统。

# INSTALL

```apt: sudo apt install john```

```dnf: sudo dnf install john```

```pacman: sudo pacman -S john```

```apk: sudo apk add john```

```zypper: sudo zypper install john```

```brew: brew install john```

```nix: nix profile install nixpkgs#john```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(8), [passwd](/man/passwd)(5)
