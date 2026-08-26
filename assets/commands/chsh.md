# TAGLINE

更改用户的登录 Shell

# TLDR

以**交互方式**设置登录 Shell

```chsh```

**列出**可用的 Shell

```chsh -l```

为当前用户设置**指定的登录 Shell**

```chsh -s [path/to/shell]```

为**指定用户**设置登录 Shell

```sudo chsh -s [path/to/shell] [username]```

# SYNOPSIS

**chsh** [_options_] [_username_]

# DESCRIPTION

**chsh** 更改用户的登录 Shell，即用户通过终端登录时启动的程序。除非由 root 执行，否则新 Shell 必须列在 **/etc/shells** 中。

普通用户可以更改自己的 Shell；root 可以更改任何用户的 Shell。更改在下次登录时生效。执行更改前会对用户进行身份验证，因此需要输入密码（以 root 运行时除外）。

常见用例包括在 bash、zsh、fish 或其他 Shell 之间切换。Linux 系统上属于 **util-linux** 软件包。

# PARAMETERS

**-s, --shell** _shell_
> 指定新的登录 Shell

**-l, --list-shells**
> 列出 /etc/shells 中的 Shell

**-h, --help**
> 显示帮助信息

# CONFIGURATION

**/etc/shells**
> 有效登录 Shell 的列表。非 root 用户只能设置为其中列出的 Shell。

# CAVEATS

Shell 必须以二进制文件形式存在并列在 /etc/shells 中。设置无效或不存在的 Shell 可能导致用户无法登录账户（可用 root 执行 **usermod -s /bin/bash** 修复）。更改在下次登录时生效。在某些系统上（如 macOS），chsh 使用不同的实现，选项略有差异。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[usermod](/man/usermod)(8), [passwd](/man/passwd)(1), [login](/man/login)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1)
