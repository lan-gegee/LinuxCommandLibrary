# TAGLINE

用于管理 Terraform 状态的文本界面工具

# TLDR

**启动 Terraform 状态 TUI**

```tftui```

**以离线模式启动**

```tftui -o```

# SYNOPSIS

**tftui** [_options_]

# DESCRIPTION

**tftui** 是一个终端应用程序，让你通过直观的文本界面查看和操作 Terraform 状态。它提供状态树可视化、资源检查、搜索功能、计划的创建与应用，以及资源操作（taint、untaint、delete、destroy）。它支持 Terragrunt 等 Terraform 包装器，并提供离线模式。

# HISTORY

**terraform-tui** 由 **Ido Avraham**（idoavrah）创建，使用 **Python** 编写。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terragrunt](/man/terragrunt)(1), [tofuref](/man/tofuref)(1)
