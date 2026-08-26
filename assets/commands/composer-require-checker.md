# TAGLINE

校验所有 PHP 依赖是否都已显式声明

# TLDR

**检查缺失的 composer 依赖声明**

```composer-require-checker check```

**检查指定的 composer.json**

```composer-require-checker check [/path/to/composer.json]```

**以 JSON 格式输出**

```composer-require-checker check --output=json```

# SYNOPSIS

**composer-require-checker** **check** [_options_] [_composer-json_]

# PARAMETERS

**--output** _format_
> 输出格式：text、json。

**--config-file** _file_
> 配置文件路径。默认：若存在则使用 composer-require-checker.json。

**--composer-vendor-dir** _dir_
> Composer vendor 目录路径。默认：./vendor。

**--exclude** _path_
> 将文件或目录排除出分析范围。可多次使用。

**--dump-configuration**
> 将默认配置转储到标准输出。

**-v**, **--verbose**
> 提高输出详细程度。需要更多细节可用 -vv 或 -vvv。

# DESCRIPTION

**composer-require-checker** 是一个静态分析工具，用于扫描 PHP 代码库，找出代码中使用但未在 composer.json 中显式声明为依赖的符号（类、函数、常量）。它能防止传递依赖带来的常见问题：包 A 依赖包 B，而你的代码直接使用了包 B 却未显式声明它，从而形成脆弱的依赖关系图。

该工具对整个代码库进行符号表分析，将发现的符号与 composer.json 中声明的 require 和 require-dev 部分交叉比对。发现未声明的依赖时，它会报告缺失哪些符号及其来源软件包，让开发者能够补充正确的依赖声明。

这对库的维护者尤为重要——他们必须确保自己的软件包可以被独立安装，而不依赖隐式依赖。它还能避免"在我机器上能跑"的情况：某个依赖碰巧通过本地另一个包间接可用，但在其他环境中或依赖版本变化时就会失败。

# CAVEATS

需要对 PHP 代码进行静态分析。对于动态加载的类可能产生误报。

# INSTALL

```nix: nix profile install nixpkgs#composer-require-checker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [composer-audit](/man/composer-audit)(1), [php](/man/php)(1), [phpstan](/man/phpstan)(1)
