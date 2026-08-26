# TAGLINE

interactive Ruby shell

# TLDR

**启动交互式 Ruby**

```irb```

**启动时不显示提示符**

```irb --noprompt```

**启动前加载文件**

```irb -r [library]```

**求值表达式**

```irb -e "[puts 'hello']"```

**使用指定的 Ruby 启动**

```irb --version```

**简单提示符**

```irb --simple-prompt```

# SYNOPSIS

**irb** [_options_] [_file_]

# PARAMETERS

**-r** _LIBRARY_
> 启动前加载库。

**-e** _EXPR_
> 求值表达式。

**--noprompt**
> 不显示提示符。

**--simple-prompt**
> 使用简单提示符。

**--inf-ruby-mode**
> Emacs inf-ruby 兼容模式。

**-I** _PATH_
> 添加到加载路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**irb** 是交互式 Ruby shell。它提供一个 REPL，用于求值 Ruby 表达式和探索代码。

该 shell 支持制表符补全、历史记录和多行输入。它是进行 Ruby 实验的标准工具。

# CAVEATS

需要已安装 Ruby。无持久化状态。高级功能可考虑使用 pry。

# HISTORY

irb 自 **Ruby** 早期版本起就是其组成部分，由 **Keiju Ishitsuka** 创建，是标准的 Ruby REPL。

# INSTALL

```apt: sudo apt install ruby```

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [gem](/man/gem)(1), [bundle](/man/bundle)(1)
