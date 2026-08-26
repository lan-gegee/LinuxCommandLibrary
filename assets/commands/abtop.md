# TAGLINE

面向 AI 编码代理会话的 htop 风格监视器

# TLDR

**监视**代理会话

```abtop```

通过 cargo 或安装脚本进行**安装**

```cargo install abtop```

# SYNOPSIS

**abtop** [*options*]

# DESCRIPTION

**abtop** 以一个精神上类似 **htop** 的实时 TUI，观察本地 AI 编码代理进程（如 Claude Code、Codex CLI）的会话、token/上下文用量、速率限制及相关端口。在同时管理多个代理终端时非常有用。

# PARAMETERS

启动后进入交互式 TUI。可选标志用于选择刷新间隔和过滤器——见 **abtop --help**。

# CAVEATS

效果取决于各代理暴露指标的方式；并非所有工具都以相同方式上报 token。在受限系统上，进程自省可能需要相应权限。

# INSTALL

```aur: yay -S abtop```

```nix: nix profile install nixpkgs#abtop```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[htop](/man/htop)(1), [btop](/man/btop)(1), [ps](/man/ps)(1)

# RESOURCES

```[Source code](https://github.com/graykode/abtop)```

<!-- verified: 2026-07-19 -->
