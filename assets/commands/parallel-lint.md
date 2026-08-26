# TAGLINE

并行检查 PHP 文件的语法错误

# TLDR

**检查目录中的 PHP 文件**

```parallel-lint [src/]```

**检查时排除指定路径**

```parallel-lint --exclude [vendor] [.]```

**使用指定的 PHP 可执行文件检查**

```parallel-lint -p [/usr/bin/php8.1] [src/]```

**检查并为错误显示 git blame**

```parallel-lint --blame [src/]```

**以 JSON 输出结果**

```parallel-lint --json [src/]```

# SYNOPSIS

**parallel-lint** [_options_] _paths_...

# PARAMETERS

**--exclude** _path_
> 将文件或目录排除在检查之外。可多次使用以排除多个路径。

**-p** _php_
> 指定要运行的 PHP 可执行文件（默认为 php）。

**-s**, **--short**
> 将 short_open_tag 设为 On（默认为 Off）。

**-e** _ext_
> 只检查具有所选扩展名的文件，扩展名之间用逗号分隔（默认为 php,php3,php4,php5,phtml,phpt）。

**-j** _num_
> 并行任务数（默认为 10）。

**--blame**
> 尝试为出错的行显示 git blame。

**--git** _git_
> 用于 blame 信息的 Git 可执行文件路径（默认为 git）。

**--colors**
> 启用彩色控制台输出。

**--no-colors**
> 禁用彩色控制台输出。

**--no-progress**
> 禁用进度输出。

**--checkstyle**
> 以 Checkstyle XML 输出结果。

**--json**
> 以 JSON 字符串输出结果。

**--show-deprecated**
> 显示 PHP 弃用警告。

**-h**, **--help**
> 打印帮助。

**-V**, **--version**
> 显示应用程序版本。

# DESCRIPTION

**parallel-lint** 并行检查 PHP 文件中的语法错误。它可以跨多个文件和目录快速完成语法检查。它不检查代码风格，只检查语法是否有效。默认运行 10 个并行任务，并检查常见的 PHP 文件扩展名。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add parallel```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[php](/man/php)(1), [phpcs](/man/phpcs)(1)
