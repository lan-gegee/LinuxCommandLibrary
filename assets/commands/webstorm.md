# TAGLINE

JetBrains JavaScript IDE 启动器

# TLDR

**打开项目**

```webstorm [path/to/project]```

**打开文件并定位到某行**

```webstorm --line [42] [file.js]```

**比较文件**

```webstorm diff [file1.js] [file2.js]```

**在新窗口中打开**

```webstorm --new-window [path/to/project]```

**等待关闭后再返回**

```webstorm --wait [file.js]```

# SYNOPSIS

**webstorm** [_--line n_] [_--new-window_] [_options_] [_path_]

# PARAMETERS

**--line** _N_
> 打开并定位到指定行。

**--column** _N_
> 打开并定位到指定列。

**--new-window**
> 强制在新窗口打开。

**--wait**
> 等待文件关闭后才返回。

**diff**
> 比较文件。

# DESCRIPTION

**webstorm** 是 JetBrains WebStorm 的命令行启动器，WebStorm 是一款面向 JavaScript 和 Web 开发的专业 IDE。它可以直接从终端打开项目、文件和目录，并提供指定行列位置的选项以精确定位光标。

该启动器支持在已有的 WebStorm 实例中打开文件，或强制新建窗口，还包含用于并排比较文件的 diff 模式。--wait 选项会阻塞终端直到文件被关闭，因此适合用作 Git 编辑器或合并工具。

该命令通常通过 WebStorm 工具菜单中的 "Create Command-line Launcher" 选项安装，安装后会放入系统 PATH。

# CAVEATS

需要安装 WebStorm。商业软件。启动器的位置因安装方式而异。

# HISTORY

**WebStorm** 由 **JetBrains** 开发，是一款面向 JavaScript 和 Web 开发的专业 IDE。

# INSTALL

```aur: yay -S webstorm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpstorm](/man/phpstorm)(1), [idea](/man/idea)(1), [code](/man/code)(1)
