# TAGLINE

增强的 Shell 历史浏览器

# TLDR

**启动 hstr**

```hstr```

**搜索命令历史**

```hstr [pattern]```

**显示收藏**

```hstr -f```

**非交互式搜索**

```hstr -n [pattern]```

**添加当前按键绑定**

```hstr --show-configuration >> ~/.bashrc```

# SYNOPSIS

**hstr** [_options_] [_pattern_]

# DESCRIPTION

**hstr**（HiSToRy）是一个增强的 Shell 历史浏览器。它提供可视化界面，用于从历史中搜索和选择命令，并按使用频率和最近时间排序。

该工具与 bash 和 zsh 集成，用更强大的搜索界面取代或增强 Ctrl+R。

# PARAMETERS

**-f**, **--favorites**
> 显示收藏的命令。

**-n**, **--non-interactive**
> 非交互模式。

**-s**, **--show-configuration**
> 显示 Shell 配置。

**-b**, **--show-blacklist**
> 显示被列入黑名单的命令。

**--show-zsh-configuration**
> 显示用于集成的 zsh 配置。

**-V**, **--version**
> 显示版本。

# ENVIRONMENT

**HSTR_CONFIG**
> 逗号分隔的配置选项：hicolor、monochromatic、case-sensitive、raw-history-view、favorites-view、duplicates、verbose-kill、blacklist、keywords-matching、static-favorites、skip-favorites-comments。

# KEYBOARD SHORTCUTS

**Ctrl+R**: 搜索历史
**Tab** / **Right**: 确认选择
**Ctrl+F**: 加入收藏
**Ctrl+/** / **Ctrl+7**: 轮换视图（历史/收藏/排序）
**Ctrl+E**: 切换正则表达式模式
**Ctrl+L**: 切换大小写敏感
**Del**: 从历史中删除命令

# CAVEATS

需要配置 Shell。历史记录很大时初次加载可能较慢。收藏单独存储。在较大的历史记录上限下效果最佳。

# HISTORY

**hstr** 由 **Martin Dvorak** 创建，旨在改善命令行历史导航。它通过提供可视反馈和更好的排序算法，解决了基础 Ctrl+R 搜索的局限。

# INSTALL

```apt: sudo apt install hstr```

```dnf: sudo dnf install hstr```

```apk: sudo apk add hstr```

```brew: brew install hstr```

```nix: nix profile install nixpkgs#hstr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [mcfly](/man/mcfly)(1), [history](/man/history)(1), [bash](/man/bash)(1)
