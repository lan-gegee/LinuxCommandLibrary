# TAGLINE

安全的密码与密钥存储守护进程

# TLDR

**启动密钥环守护进程**

```gnome-keyring-daemon --start```

**以指定组件启动**

```gnome-keyring-daemon --start --components=secrets,ssh```

**替换正在运行的守护进程**

```gnome-keyring-daemon --replace```

**通过 CLI 存储机密**

```secret-tool store --label="My Secret" service myapp```

**查找机密**

```secret-tool lookup service myapp```

# SYNOPSIS

**gnome-keyring-daemon** [_options_]

# PARAMETERS

**--start**
> 若未运行则启动守护进程。

**--replace**
> 替换正在运行的守护进程。

**--components** _list_
> 组件：secrets、pkcs11、ssh。

**--daemonize**
> 以守护进程方式运行。

**-f**, **--foreground**
> 在前台运行。

**--unlock**
> 从 stdin 读取密码并解锁登录密钥环，若不存在则创建它。

**-l**, **--login**
> 从 stdin 读取登录密码（供 PAM 使用）。

**-C**, **--control-directory** _directory_
> 用于创建通信套接字的目录。

**-V**, **--version**
> 打印版本并退出。

# DESCRIPTION

**GNOME Keyring** 是一个存储机密、密码和密钥的守护进程。它为应用程序提供安全存储，并处理 SSH 密钥管理。

密钥环通常在登录时启动，并用用户密码解锁。应用程序通过 libsecret 或 Secret Service D-Bus API 访问它。

# COMPONENTS

- **secrets**：密码/机密存储
- **ssh**：SSH 代理（替代 ssh-agent）
- **pkcs11**：PKCS#11 智能卡支持

# CONFIGURATION

**~/.local/share/keyrings/**
> 存放密钥环数据文件的目录。

# CAVEATS

通常由桌面会话启动。ssh 组件可能与 ssh-agent 冲突。会话锁定时密钥环也会锁定。非 GNOME 桌面可能需要手动配置。

# HISTORY

GNOME Keyring 为 GNOME 桌面而生，提供安全的凭据存储。它实现了 freedesktop.org 的 Secret Service 规范，以保证跨桌面兼容性。

# INSTALL

```apt: sudo apt install gnome-keyring```

```dnf: sudo dnf install gnome-keyring```

```pacman: sudo pacman -S gnome-keyring```

```apk: sudo apk add gnome-keyring```

```zypper: sudo zypper install gnome-keyring```

```nix: nix profile install nixpkgs#gnome-keyring```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[secret-tool](/man/secret-tool)(1), [ssh-agent](/man/ssh-agent)(1), [gpg](/man/gpg)(1)
