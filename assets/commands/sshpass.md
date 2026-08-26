# TLDR

**使用密码进行 SSH 连接**

```sshpass -p '[password]' ssh [user@host]```

**从文件读取密码进行 SSH 连接**

```sshpass -f [password_file] ssh [user@host]```

**从环境变量读取密码进行 SSH 连接**

```SSHPASS='[password]' sshpass -e ssh [user@host]```

**使用密码进行 SCP 传输**

```sshpass -p '[password]' scp [file] [user@host:/path/]```

**使用密码进行 Rsync 同步**

```sshpass -p '[password]' rsync -avz [files] [user@host:/path/]```

# SYNOPSIS

**sshpass** [_-p password_] [_-f file_] [_-e_] [_options_] _command_ [_args_]

# PARAMETERS

**-p** _PASSWORD_
> 在命令行上提供密码。

**-f** _FILE_
> 从文件读取密码。

**-e**
> 从 SSHPASS 环境变量读取密码。

**-d** _FD_
> 从文件描述符读取密码。

**-P** _PROMPT_
> 设置密码提示的匹配模式。

**-v**
> 详细输出模式。

**-h**
> 显示帮助。

**-V**
> 显示版本。

# DESCRIPTION

**sshpass** 为 SSH 提供非交互式的密码认证，无需手动输入。它适用于无法使用密钥认证的场景下的自动化操作。

密码来源包括命令行、文件和环境变量。相比在命令行上暴露密码，使用文件更安全。

该工具可与任何期待 SSH 风格密码提示的程序配合使用：ssh、scp、rsync 等。

首次连接需要处理主机密钥。自动化场景可以使用 -o StrictHostKeyChecking=no，但这会带来安全隐患。

对大多数用途而言，优先推荐 SSH 密钥。sshpass 用于填补密钥认证不可行或不实用的场景空缺。

# CAVEATS

命令行上的密码会在进程列表中可见。安全性不如 SSH 密钥。不建议用于交互式场景。可能将密码暴露到日志中。

# HISTORY

**sshpass** 由 **Shachar Shemesh** 编写，旨在解决脚本和自动化中无法使用密钥认证时的非交互式 SSH 密码输入需求。

# INSTALL

```apt: sudo apt install sshpass```

```dnf: sudo dnf install sshpass```

```pacman: sudo pacman -S sshpass```

```apk: sudo apk add sshpass```

```zypper: sudo zypper install sshpass```

```brew: brew install sshpass```

```nix: nix profile install nixpkgs#sshpass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1), [expect](/man/expect)(1), [ssh-agent](/man/ssh-agent)(1)

# RESOURCES

```[Homepage](https://sourceforge.net/projects/sshpass/)```

<!-- verified: 2026-06-10 -->
