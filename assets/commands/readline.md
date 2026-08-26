# TAGLINE

行编辑与输入历史库

# TLDR

**查看 readline 键绑定**

```bind -P```

**编辑 inputrc**

```vi ~/.inputrc```

**设置 vi 模式**

```set -o vi```

**设置 emacs 模式**

```set -o emacs```

# SYNOPSIS

GNU Readline library and configuration

# DESCRIPTION

**Readline** 是一个提供命令行编辑、历史记录和 Tab 补全功能的库。bash、gdb、python 以及许多其他程序都在使用它。配置通过 ~/.inputrc 进行。

# INPUTRC CONFIGURATION

```bash
# ~/.inputrc

# Case insensitive completion
set completion-ignore-case on

# Show all completions on first tab
set show-all-if-ambiguous on

# Vi mode
set editing-mode vi

# Key bindings
"\e[A": history-search-backward
"\e[B": history-search-forward
"\C-p": history-search-backward
```

# COMMON KEYBINDINGS (Emacs mode)

```
Ctrl+a    - Beginning of line
Ctrl+e    - End of line
Ctrl+k    - Kill to end of line
Ctrl+u    - Kill to beginning
Ctrl+w    - Kill word backward
Ctrl+y    - Yank (paste)
Ctrl+r    - Reverse search history
Ctrl+l    - Clear screen
Alt+f     - Forward word
Alt+b     - Backward word
```

# EXAMPLES

```bash
# List current bindings
bind -P | grep search

# Bind key in session
bind '"\e[A": history-search-backward'

# Check editing mode
echo $SHELLOPTS | tr ':' '\n' | grep -E 'vi|emacs'
```

# CAVEATS

配置因应用程序而异。有些程序改用 libedit。重新加载：source ~/.inputrc 或按 Ctrl+x Ctrl+r。

# HISTORY

GNU Readline 由 **Brian Fox** 为 GNU 项目编写，成为标准的行编辑库。

# INSTALL

```dnf: sudo dnf install readline```

```pacman: sudo pacman -S readline```

```brew: brew install readline```

```nix: nix profile install nixpkgs#readline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [bind](/man/bind)(1)
