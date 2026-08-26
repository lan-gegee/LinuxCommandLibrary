# TAGLINE

管理 Zsh 配置的框架

# TLDR

**安装 Oh My Zsh**

```sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"```

**更新 Oh My Zsh**

```omz update```

**更换主题**

```omz theme set [robbyrussell]```

**列出已安装的插件**

```omz plugin list```

**启用插件**

```omz plugin enable [git]```

**禁用插件**

```omz plugin disable [git]```

**列出可用主题**

```omz theme list```

**重新加载 Oh My Zsh 配置**

```omz reload```

# SYNOPSIS

**omz** _command_ [_args_]

# PARAMETERS

**update**
> 更新 Oh My Zsh。

**theme set** _name_
> 设置主题。

**theme list**
> 列出主题。

**plugin enable** _name_
> 启用插件。

**plugin disable** _name_
> 禁用插件。

**plugin list**
> 列出插件。

**plugin info** _name_
> 显示某个插件的信息。

**reload**
> 重新加载 Oh My Zsh 配置。

**changelog**
> 显示更新日志。

**version**
> 显示当前版本。

**doctor**
> 诊断常见问题。

# DESCRIPTION

**Oh My Zsh** 是一个管理 Zsh 配置的框架。它提供主题、插件和辅助函数，以增强 Zsh 的使用体验。

配置位于 ~/.zshrc，插件和主题位于 ~/.oh-my-zsh。

# CONFIGURATION

```bash
# ~/.zshrc
ZSH_THEME="robbyrussell"
plugins=(git docker kubectl node)
ZSH_CUSTOM="$ZSH/custom"
HIST_STAMPS="yyyy-mm-dd"
COMPLETION_WAITING_DOTS="true"
source $ZSH/oh-my-zsh.sh
```

# CAVEATS

插件过多可能拖慢 Shell 启动速度。需要 Zsh 作为默认 Shell。自定义主题放在 ~/.oh-my-zsh/custom/themes。

# HISTORY

Oh My Zsh 由 **Robby Russell** 于 **2009** 年创建，如今已是最流行的 Zsh 框架，拥有数千名贡献者。

# INSTALL

```nix: nix profile install nixpkgs#oh-my-zsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zsh](/man/zsh)(1), [bash](/man/bash)(1), [p10k](/man/p10k)(1), [starship](/man/starship)(1), [antigen](/man/antigen)(1), [zinit](/man/zinit)(1), [fish](/man/fish)(1)
