# TAGLINE

面向 shell 和编辑器的状态栏插件

# TLDR

**启动守护进程**

```powerline-daemon --replace```

**在 bash 中使用**

```powerline-daemon -q && PROMPT_COMMAND="powerline-bash-prompt"```

**检查配置**

```powerline-lint```

**重新加载配置**

```powerline-daemon --kill && powerline-daemon```

# SYNOPSIS

**powerline** _ext_ _side_ [_options_]

**powerline-daemon** [_options_]

# PARAMETERS

**-q**, **--quiet**
> 抑制输出。

**--replace**
> 替换正在运行的守护进程。

**--kill**
> 终止守护进程。

**-p**, **--config-path** _path_
> 配置路径。

# DESCRIPTION

**Powerline** 是一款面向 vim、tmux、zsh、bash 等应用的状态栏插件。它提供信息丰富、美观大方的状态显示，展示诸如 Git 分支与状态、Python virtualenv、当前工作目录、主机名和电池电量等上下文信息。

出于性能考虑，它以守护进程方式运行，通过客户端与 shell 提示符和编辑器插件通信。**~/.config/powerline/** 中的配置文件控制主题、配色方案以及每种上下文中出现的段（segment）。状态栏分隔符使用的特殊字形需要 powerline 兼容字体。

# EXAMPLES

```bash
# Start daemon
powerline-daemon -q

# Check config
powerline-lint

# Test shell prompt
powerline shell left

# Install for bash (in .bashrc)
powerline-daemon -q
PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
```

# SHELL SETUP (bash)

```bash
# In ~/.bashrc
if [ -f /usr/share/powerline/bindings/bash/powerline.sh ]; then
    source /usr/share/powerline/bindings/bash/powerline.sh
fi
```

# TMUX SETUP

```
# In ~/.tmux.conf
source /usr/share/powerline/bindings/tmux/powerline.conf
```

# CONFIGURATION

**~/.config/powerline/config.json**
> 主配置文件，定义默认主题、配色方案，以及针对 shell、tmux、vim 等上下文的各扩展覆盖设置。

**~/.config/powerline/themes/**
> 主题文件，控制每种状态栏上下文（shell 提示符、tmux 状态栏、vim 状态栏）中出现哪些段。

**~/.config/powerline/colorschemes/**
> 配色方案文件，将段的高亮组映射到终端颜色。

# CAVEATS

需要 powerline 兼容字体。配置位于 ~/.config/powerline/。守护进程模式可提升性能。

# HISTORY

Powerline 由 **Kim Silkebækken** 创建，最初是一个 vim 插件，后来扩展到 shell 和 tmux。

# INSTALL

```apt: sudo apt install powerline```

```dnf: sudo dnf install powerline```

```pacman: sudo pacman -S powerline```

```zypper: sudo zypper install powerline```

```nix: nix profile install nixpkgs#powerline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[starship](/man/starship)(1), [oh-my-zsh](/man/oh-my-zsh)(1), [tmux](/man/tmux)(1)
