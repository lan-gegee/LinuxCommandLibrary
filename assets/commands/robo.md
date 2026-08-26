# TAGLINE

PHP 任务运行框架

# TLDR

**列出任务**

```robo```

**运行任务**

```robo [task-name]```

**带参数运行**

```robo [task-name] [--arg=value]```

**使用指定文件**

```robo -f [RoboFile.php] [task]```

**详细输出**

```robo [task] -v```

**试运行**

```robo [task] --simulate```

# SYNOPSIS

**robo** [_-f file_] [_options_] [_task_] [_args_]

# PARAMETERS

**-f** _FILE_
> RoboFile 路径。

**-v**
> 详细输出。

**--simulate**
> 试运行模式。

**--load-from** _DIR_
> 从指定目录加载。

**-n**
> 无交互。

**--help**
> 显示帮助。

# DESCRIPTION

**robo** 是一个 PHP 任务运行框架，采用面向对象方式定义自动化任务。任务以 PHP 类方法的形式写在 **RoboFile.php** 中，可以充分利用 PHP 的语言特性和生态系统来实现构建自动化、部署和开发工作流。

该框架内置了常见操作的任务，例如文件操作（复制、移动、监视）、运行 shell 命令、SSH 远程执行和并行任务执行。**--simulate** 标志启用试运行模式，可预览将要执行的命令而不实际运行，这对测试复杂的任务序列很有用。

Robo 与基于 Composer 的 PHP 项目自然集成，在 PHP 生态中扮演着类似 Make、Rake 或 Gulp 的角色。

# CAVEATS

需要 PHP。必须有 RoboFile.php。建议配合 Composer 使用。

# HISTORY

**Robo** 作为一款现代的 PHP 任务运行器而创建，为 PHP 项目中的自动化任务提供了简洁的 API。

# INSTALL

```nix: nix profile install nixpkgs#robo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [make](/man/make)(1), [rake](/man/rake)(1)
