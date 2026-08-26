# TAGLINE

在 Bash 中设置 Readline 按键绑定和变量

# TLDR

**列出所有 Readline 按键绑定**

```bind -P```

**以可复用格式列出按键绑定**

```bind -p```

**将按键序列绑定到 Readline 函数**

```bind '"\e[24~": end-of-line'```

**将按键序列绑定到 shell 命令**

```bind -x '"\C-l": clear'```

**移除按键序列的绑定**

```bind -r '\e[24~'```

**从文件读取按键绑定**

```bind -f [~/.inputrc]```

**查询哪些键调用指定函数**

```bind -q [complete]```

# SYNOPSIS

**bind** [**-lpsvPSVX**] [**-m** _keymap_] [**-f** _filename_] [**-q** _name_] [**-u** _name_] [**-r** _keyseq_] [**-x** _keyseq:shell-command_] [_keyseq:readline-function_]

# DESCRIPTION

**bind** 是 Bash 的内建命令，用于设置 Readline 按键绑定和变量。它通过将按键序列映射到 Readline 函数、宏或 shell 命令，控制 Bash 对键盘输入的响应方式。

默认情况下 Bash 使用 Emacs 风格的按键绑定，但 bind 允许自定义成任何偏好的方案。按键绑定可以交互式设置，也可以从 **~/.inputrc** 等配置文件加载。

要查看某个键的转义序列，可在命令行先按 **Ctrl+v** 再按该键，或使用 **read** 内建命令并按下想要的组合键。

# PARAMETERS

**-l**
> 列出所有 Readline 函数的名称

**-P**
> 列出函数名及其当前绑定

**-p**
> 以适合作为输入复用的格式列出绑定

**-S**
> 列出调用宏的按键序列及其值

**-s**
> 以可复用格式列出宏绑定

**-V**
> 列出 Readline 变量名及其值

**-v**
> 以可复用格式列出 Readline 变量

**-X**
> 以可复用格式列出绑定到 shell 命令的按键序列

**-m** _keymap_
> 使用指定的 keymap：emacs、emacs-standard、emacs-meta、emacs-ctlx、vi、vi-move、vi-command、vi-insert

**-f** _filename_
> 从文件读取按键绑定

**-q** _function_
> 查询哪些键调用了指定函数

**-u** _function_
> 解除所有绑定到该函数的键

**-r** _keyseq_
> 移除按键序列的绑定

**-x** _keyseq:shell-command_
> 输入该按键序列时执行 shell 命令

# CAVEATS

使用 **-x** 绑定 shell 命令时，Shell 会把 **READLINE_LINE** 和 **READLINE_POINT** 变量设为当前行缓冲区内容和光标位置。在该命令中修改这些变量会影响编辑状态。

按键绑定语法必须作为单个参数传入，与 **~/.inputrc** 中使用的格式一致。

# INSTALL

```dnf: sudo dnf install bind```

```pacman: sudo pacman -S bind```

```zypper: sudo zypper install bind```

```brew: brew install bind```

```nix: nix profile install nixpkgs#bind```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [readline](/man/readline)(3)

# RESOURCES

```[Homepage](https://www.gnu.org/software/bash/)```

```[Documentation](https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins)```

<!-- verified: 2026-06-19 -->
