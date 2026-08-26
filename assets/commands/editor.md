# TAGLINE

系统默认文本编辑器

# TLDR

**打开默认编辑器**

```editor [file.txt]```

**更改默认编辑器**

```sudo update-alternatives --config editor```

**通过环境变量设置编辑器**

```export EDITOR=vim```

**设置可视化编辑器**

```export VISUAL=nano```

# SYNOPSIS

**editor** [_file_]

# DESCRIPTION

**editor** 是指向系统默认文本编辑器的符号链接。在基于 Debian 的系统上，/usr/bin/editor 由 alternatives 系统管理，通常指向 nano、vim 或其他已安装的编辑器。它是 Debian 的一项约定而非独立程序，在大多数非 Debian 发行版上并不存在。

editor 命令为程序提供了一种调用文本编辑器的标准方式。crontab、visudo 和 git commit 等命令会使用 EDITOR 或 VISUAL 环境变量来确定要启动的编辑器，当两者都未设置时回退到 sensible-editor 或 /usr/bin/editor。

# CONFIGURATION

```bash
# Check current editor
update-alternatives --display editor

# Set default (Debian/Ubuntu)
sudo update-alternatives --config editor

# Set via environment
export EDITOR=vim
export VISUAL="code --wait"
```

# EDITOR PRIORITY

程序通常按以下顺序检查：
1. VISUAL（面向图形终端）
2. EDITOR（适用于任何终端）
3. 系统默认（editor、/usr/bin/editor）

# CAVEATS

editor 命令可能并非在所有系统上都存在。环境变量会覆盖系统设置。某些程序忽略 EDITOR 并使用自己的配置。图形化编辑器需要 --wait 或类似标志才能正确集成。

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [emacs](/man/emacs)(1), [update-alternatives](/man/update-alternatives)(8), [sensible-editor](/man/sensible-editor)(1)
