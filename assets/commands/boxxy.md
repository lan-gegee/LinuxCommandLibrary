# TAGLINE

利用 Linux 命名空间重定向应用的文件路径。

# TLDR

**带文件重定向规则运行应用**

```boxxy [application]```

**使用自定义配置文件**

```boxxy --config [boxxy.yaml] [application]```

**在命令行添加规则**

```boxxy --rule "[rule_name]:~/.config/app:~/.local/share/app" [application]```

**扫描主目录以获取规则建议**

```boxxy --scan```

**不加载配置文件运行**

```boxxy --no-config [application]```

# SYNOPSIS

**boxxy** [_options_] [_application_] [_arguments_]

# DESCRIPTION

**boxxy** 会把行为不端的 Linux 应用"关进盒子"，迫使它们把文件和目录放到正确的位置，而无需符号链接。它利用 Linux 命名空间透明地重定向文件操作。

该工具旨在管理那些在不合适的位置创建点文件或目录的应用，将它们重定向到符合 XDG 规范的路径或其他首选位置。

# PARAMETERS

**--config** _file_
> 使用指定的配置文件。

**--rule** _rule_
> 在命令行添加规则（格式：name:target:rewrite）。

**--no-config**
> 禁止加载配置文件。

**--scan**
> 扫描主目录并给出规则建议。

**-v, --verbose**
> 启用详细输出。

**-h, --help**
> 显示帮助并退出。

# CONFIGURATION

boxxy.yaml 中的规则包括：

**name**
> 易于辨识的规则标识符。

**target**
> 要遮蔽的文件或目录。

**rewrite**
> 替代用的文件或目录。

**mode**
> "directory" 或 "file"（默认：directory）。

**commands**
> 可选，规则适用的命令列表。

# CAVEATS

需要 Linux 内核的命名空间支持。当目标是一个文件时，规则必须指定 mode，尤其是目标尚不存在时。项目本地的 boxxy.yaml 文件和 .env 文件可以自动加载。

# INSTALL

```pacman: sudo pacman -S boxxy```

```nix: nix profile install nixpkgs#boxxy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firejail](/man/firejail)(1), [bwrap](/man/bwrap)(1), [unshare](/man/unshare)(1)
