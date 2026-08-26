# TAGLINE

离线 Windows 密码与注册表编辑器

# TLDR

以**交互**模式打开 SAM 数据库

```chntpw -i [path/to/sam_file]```

**列出** Windows SAM 文件中的用户名

```chntpw -l [path/to/sam_file]```

离线编辑**指定用户**（密码/解锁）

```chntpw -u [username] [path/to/sam_file]```

# SYNOPSIS

**chntpw** [_options_] _sam_file_ [_system_file_] [_security_file_]

# DESCRIPTION

**chntpw** 是一款离线的 Windows 密码与注册表编辑器。它可以重置本地用户密码、将用户提升为管理员、解锁账户，以及直接编辑 Windows 注册表。

该工具的原理是在 Windows 未运行时修改其 SAM（Security Account Manager）数据库文件。这通常通过从 Linux live CD 启动来完成。

# PARAMETERS

**-l**
> 列出 SAM 文件中的用户

**-u** _username_
> 选择要编辑的用户

**-i**
> 带菜单的交互模式

**-e**
> 注册表编辑器模式

**-L**
> 将被更改文件的名称写入 /tmp/changed

# CAVEATS

需要对 Windows 分区的离线访问。无法重置 Microsoft 账户（云账户）密码。BitLocker 加密的驱动器必须先解密。修改前务必备份 SAM 文件。

# HISTORY

**chntpw** 由 Petter Nordahl-Hagen 创建，用于恢复对 Windows 系统的访问。它已成为 Kali Linux 等注重安全的 Linux 发行版中收录的标准工具。

# INSTALL

```apt: sudo apt install chntpw```

```dnf: sudo dnf install chntpw```

```pacman: sudo pacman -S chntpw```

```apk: sudo apk add chntpw```

```zypper: sudo zypper install chntpw```

```nix: nix profile install nixpkgs#chntpw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

