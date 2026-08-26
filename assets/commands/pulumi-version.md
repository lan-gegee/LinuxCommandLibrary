# TAGLINE

显示已安装的 Pulumi CLI 版本

# TLDR

**显示 Pulumi 版本**

```pulumi version```

# SYNOPSIS

**pulumi** **version**

# PARAMETERS

**--color** _mode_
> 为输出着色。可选值：`always`、`never`、`raw`、`auto`（默认：`auto`）。

**--non-interactive**
> 为所有命令禁用交互模式。

**--logflow**
> 将日志设置传递给插件等子进程。

**--logtostderr**
> 日志输出到 stderr 而非文件。

**-v**, **--verbose** _level_
> 以指定级别启用详细日志。

# DESCRIPTION

**pulumi version** 打印已安装的 Pulumi CLI 的版本号。可用于验证安装并检查是否有可用升级。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-about](/man/pulumi-about)(1)
