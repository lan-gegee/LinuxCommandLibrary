# TAGLINE

以加锁方式安全编辑密码文件

# TLDR

编辑 **password** 文件（/etc/passwd）

```sudo vipw```

编辑 **shadow** 密码文件（/etc/shadow）

```sudo vipw -s```

编辑 **group** 文件（/etc/group）

```sudo vipw -g```

显示**版本**

```vipw -V```

# SYNOPSIS

**vipw** [_OPTIONS_]

# PARAMETERS

**-g, --group**
> 编辑组文件（/etc/group）。等同于以 `vigr` 调用。

**-p, --passwd**
> 编辑 passwd 文件（默认）。

**-s, --shadow**
> 编辑影子密码文件（/etc/shadow）；与 -g 组合时编辑影子组文件（/etc/gshadow）。

**-q, --quiet**
> 安静模式。

**-h, --help**
> 显示帮助并退出。

**-V, --version**
> 显示版本信息。

# DESCRIPTION

**vipw** 安全地编辑密码文件（/etc/passwd）。它会锁定文件以防同时编辑，运行编辑器，并在保存前校验文件格式。

使用 vipw 而不是直接编辑密码文件，可以避免并发访问和语法错误导致的文件损坏。

# CAVEATS

需要 root 权限。通过 EDITOR 或 VISUAL 环境变量选择编辑器。编辑期间文件被锁定。编辑组文件请使用 vigr。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vigr](/man/vigr)(8), [passwd](/man/passwd)(1), [useradd](/man/useradd)(8), [usermod](/man/usermod)(8)
