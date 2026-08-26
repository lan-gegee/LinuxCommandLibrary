# TAGLINE

交互式 PHP Shell 与运行时调试器

# TLDR

**启动 PHP REPL**

```psysh```

**以指定配置文件启动**

```psysh -c [config.php]```

**以指定工作目录启动**

```psysh --cwd [path/to/project]```

**从 stdin 非交互运行**

```echo "echo 'hello';" | psysh -n```

**以紧凑输出启动**

```psysh --compact```

**预热 autoload 以获得更好的制表符补全**

```psysh --warm-autoload```

# SYNOPSIS

**psysh** [_options_] [_files_...]

# PARAMETERS

**-c**, **--config** _FILE_
> 使用替代的配置文件。

**--cwd** _PATH_
> 使用替代的工作目录。

**-V**, **--version**
> 显示版本号。

**-i**, **-a**, **--interactive**
> 强制交互模式。

**-n**, **--no-interactive**
> 强制非交互模式（从 stdin 读取）。

**-r**, **--raw-output**
> 以 var_export 风格打印返回值。

**--compact**
> 以紧凑输出运行（最少空白）。

**-q**, **--quiet**
> 抑制除结果和错误之外的大部分输出。

**-v**, **-vv**, **-vvv**, **--verbose**
> 提高消息详细程度（最多三级）。

**--color**
> 强制彩色输出。

**--no-color**
> 禁用彩色输出。

**--warm-autoload**
> 预加载 Composer autoloader 中的类，以获得更好的制表符补全。

**--yolo**
> 以最少的输入校验运行（仅用于调试）。

**-u**, **--self-update**
> 安装较新版本（仅限 PHAR 安装方式）。

**--update-manual**
> 下载最新的 PHP 手册以支持内联文档。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**psysh** 是一款现代交互式 PHP shell（REPL），提供功能强大的开发者控制台，具备语法高亮、制表符补全和内联文档。它可以交互式地执行 PHP 代码、检查变量、测试代码片段，无需创建脚本文件。

PsySH 集成到应用中时还可以充当运行时调试器。开发者在代码中调用 `eval(\Psy\sh())` 即可进入交互式调试会话，访问当前作用域的变量和上下文。它是 Laravel **tinker** 命令的基础。

# CONFIGURATION

**~/.config/psysh/config.php**
> 用于自定义 REPL 行为的 PHP 配置文件，包括默认 include、readline 设置和输出分页器。

# CAVEATS

需要 PHP。可通过 Composer 安装或作为独立 PHAR 使用。

# HISTORY

PsySH 由 **Justin Hileman**（bobthecow）创建，是一款具备高级功能的**现代 PHP REPL**，包括内联文档和运行时调试。

# INSTALL

```brew: brew install psysh```

```nix: nix profile install nixpkgs#psysh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1), [artisan](/man/artisan)(1)
