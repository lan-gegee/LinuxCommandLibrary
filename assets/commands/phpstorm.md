# TAGLINE

启动 PhpStorm IDE

# TLDR

**打开项目**

```phpstorm [path/to/project]```

**打开文件并定位到某行**

```phpstorm --line [42] [file.php]```

**比较文件**

```phpstorm diff [file1.php] [file2.php]```

**在新窗口中打开**

```phpstorm --new-window [path/to/project]```

**等待关闭**

```phpstorm --wait [file.php]```

**检查代码**

```phpstorm inspect [project] [output] -v2```

# SYNOPSIS

**phpstorm** [_--line n_] [_--new-window_] [_options_] [_path_]

# PARAMETERS

**--line** _N_
> 打开时定位到指定行号。

**--column** _N_
> 打开时定位到指定列。

**--new-window**
> 强制在新窗口中打开。

**--wait**
> 等待窗口关闭。

**diff**
> 比较两个文件。

**inspect**
> 运行代码检查。

**--help**
> 显示帮助。

# DESCRIPTION

**phpstorm** 启动 PhpStorm IDE。它可以打开项目和文件。

这是 JetBrains 出品的 PHP IDE，提供专业的开发环境。

命令行启动器实现了集成，可以从终端直接打开。

diff 模式用于比较文件，基于内置的比较工具。

# CAVEATS

需要安装 PhpStorm。商业软件。启动器脚本的位置因环境而异。

# HISTORY

**PhpStorm** 由 **JetBrains** 开发。它凭借智能编码辅助提供了专业的 PHP 开发工具。

# INSTALL

```aur: yay -S phpstorm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[idea](/man/idea)(1), [webstorm](/man/webstorm)(1), [code](/man/code)(1)
