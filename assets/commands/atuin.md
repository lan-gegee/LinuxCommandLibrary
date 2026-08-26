# TAGLINE

支持同步和搜索的神奇 Shell 历史工具

# TLDR

**交互式搜索**命令历史

```atuin search -i [query]```

从当前 Shell **导入**现有历史

```atuin import auto```

将历史**同步**到服务器

```atuin sync```

显示 Shell 使用情况**统计**

```atuin stats```

**登录**同步服务器

```atuin login```

**注册**新的同步账户

```atuin register -u [username] -e [email] -p [password]```

**列出**最近的命令历史

```atuin history list```

运行**诊断**以检查常见问题

```atuin doctor```

# SYNOPSIS

**atuin** _command_ [_options_]

# DESCRIPTION

**atuin** 用 SQLite 数据库取代 Shell 自带的历史记录，提供强大的搜索、上下文跟踪，以及可选的跨机器端到端加密同步。

它会记录退出状态、耗时、工作目录和主机名等额外上下文，使历史搜索比传统的 Ctrl+R 更强大。

# PARAMETERS

**search** [_query_]
> 交互式历史搜索。支持按目录、会话、主机过滤或全局搜索。

**import** _source_
> 导入现有历史（auto、bash、zsh、fish、nu、xonsh、resh 等）。

**sync**
> 与 Atuin 服务器同步历史（上传和下载）。

**login**
> 登录同步服务器进行身份认证。

**register**
> 在 Atuin 同步服务器上注册新账户。

**logout**
> 移除认证信息。

**key**
> 显示或设置用于端到端加密同步的加密密钥。

**stats**
> 显示使用统计和命令频率。

**history** _subcommand_
> 历史管理（list、delete 等）。

**init** _shell_
> 输出 bash、zsh、fish 或 nu 的 Shell 初始化代码。

**doctor**
> 运行诊断，检查安装中的常见问题。

**info**
> 显示系统与配置信息。

**dotfiles**
> 管理并同步 Shell 别名和环境变量。

# SHELL INTEGRATION

添加到 Shell 的 rc 文件中：
```bash
eval "$(atuin init bash)"  # or zsh, fish
```

可选择禁用特定按键绑定：
```bash
eval "$(atuin init zsh --disable-up-arrow)"
```

# CONFIGURATION

**~/.config/atuin/config.toml**
> 主配置文件，涵盖搜索设置、同步选项、数据库路径、过滤模式、搜索模式和界面偏好。

# CAVEATS

需要在 Shell 中加载初始化代码。同步功能是可选的（完全可以离线使用）。数据库会随时间增长变大。某些 Shell 需要特定配置才能正确集成。

# HISTORY

**atuin** 由 Ellie Huxtable 创建，于 **2021** 年发布，提供了带端到端加密同步、统计功能和改进搜索的现代 Shell 历史方案。

# INSTALL

```apt: sudo apt install atuin```

```dnf: sudo dnf install atuin```

```pacman: sudo pacman -S atuin```

```apk: sudo apk add atuin```

```zypper: sudo zypper install atuin```

```brew: brew install atuin```

```nix: nix profile install nixpkgs#atuin```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[history](/man/history)(1), [mcfly](/man/mcfly)(1), [hstr](/man/hstr)(1), [fzf](/man/fzf)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1)
