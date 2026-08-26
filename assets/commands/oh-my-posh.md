# TAGLINE

提示符主题引擎

# TLDR

**为 Shell 初始化**

```eval "$(oh-my-posh init [bash|zsh|fish])"```

**使用特定主题**

```eval "$(oh-my-posh init bash --config [theme.json])"```

**列出可用主题**

```oh-my-posh get themes```

**打印当前配置**

```oh-my-posh print primary```

**调试提示符**

```oh-my-posh debug```

# SYNOPSIS

**oh-my-posh** [_command_] [_options_]

# PARAMETERS

**init** _SHELL_
> 生成 Shell 初始化脚本（bash、zsh、fish、powershell、cmd、nu）。

**get themes**
> 列出可用主题。

**get shell**
> 显示当前 Shell 信息。

**config export**
> 导出当前主题配置。

**config migrate**
> 将配置迁移到当前版本的格式。

**font install**
> 安装 Nerd Font。

**cache clear**
> 清除提示符缓存。

**upgrade**
> 将 oh-my-posh 更新到最新版本。

**toggle** _segment_
> 启用或禁用特定的提示符片段。

**debug**
> 显示提示符渲染的诊断信息。

**--config** _FILE_
> 配置文件路径（JSON、YAML 或 TOML）。

# DESCRIPTION

**oh-my-posh** 是一个跨平台的提示符主题引擎，通过可配置的片段渲染自定义 Shell 提示符，可显示 git 状态、语言版本、执行时间等信息。它支持 bash、zsh、fish、PowerShell、cmd 和 nu。

# CAVEATS

显示图标需要 Nerd Font。跨平台可用。配置采用 JSON/YAML/TOML 格式。

# HISTORY

oh-my-posh 为在不同 Shell 之间实现**可自定义的提示符**而诞生。

# INSTALL

```dnf: sudo dnf install oh-my-posh```

```brew: brew install oh-my-posh```

```nix: nix profile install nixpkgs#oh-my-posh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[starship](/man/starship)(1), [powerline](/man/powerline)(1), [p10k](/man/p10k)(1)
