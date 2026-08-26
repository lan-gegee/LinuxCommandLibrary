# TAGLINE

终端 UI 操作系统与窗口管理复用器

# TLDR

**启动终端复用器**

```tuios```

**以 SSH 服务器模式启动**

```tuios --ssh```

**回放 tape 录制文件**

```tuios play [recording.tape]```

# SYNOPSIS

**tuios** [_options_]

# DESCRIPTION

**tuios** 是一个基于终端的窗口管理器，使用 Go 和 Bubble Tea 构建。它提供类 Vim 的模态界面、9 个独立工作区、自动平铺、鼠标支持、SSH 服务器模式、用于自动化的 tape 脚本以及 60Hz 实时更新。

# HISTORY

**tuios** 由 **Gaurav Gosain**（Gaurav-Gosain）创建，用 **Go** 编写。

# INSTALL

```brew: brew install tuios```

```nix: nix profile install nixpkgs#tuios```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [zellij](/man/zellij)(1)
