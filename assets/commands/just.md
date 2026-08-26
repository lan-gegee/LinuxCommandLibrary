# TAGLINE

类似 make 但专注于执行项目专属命令的命令运行器

# TLDR

**列出可用配方**

```just --list```

**运行默认配方**

```just```

**运行指定配方**

```just [recipe_name]```

**带参数运行**

```just [recipe_name] [arg1] [arg2]```

**从指定的 justfile 运行**

```just --justfile [path/to/justfile] [recipe]```

**只显示将要运行的命令**而不实际执行

```just --dry-run [recipe]```

**求值并打印所有变量**

```just --evaluate```

**在指定目录中运行配方**

```just --working-directory [path] [recipe]```

# SYNOPSIS

**just** [_options_] [_recipe_] [_arguments ..._]

# PARAMETERS

**-l**, **--list**
> 列出可用配方。

**-n**, **--dry-run**
> 打印将要执行的命令但不运行。

**--evaluate**
> 求值并打印所有变量。

**-f**, **--justfile** _path_
> 使用指定的 justfile。

**-d**, **--working-directory** _path_
> 从指定目录运行。

**--set** _var value_
> 覆盖变量值。

**--chooser** _program_
> 使用指定程序交互式选择配方。

**--choose**
> 用选择器选取配方。

**-s**, **--show** _recipe_
> 显示配方定义。

**--summary**
> 每行列出一个配方。

**--dump**
> 以规范形式打印 justfile。

**--fmt**
> 格式化 justfile。

**--check**
> 检查 justfile 是否有错误。

**-q**, **--quiet**
> 不回显配方行。

**-v**, **--verbose**
> 详细输出。

**--color** _when_
> 彩色输出：auto、always、never。

**--shell** _shell_
> 配方使用的 shell。

# DESCRIPTION

**just** 是一个类似 make 的命令运行器，但它专注于运行项目专属命令，而不是构建目标。它使用 **justfile**（类似于 Makefile）来定义配方——即命名的命令集合。

每个配方由名称、可选参数和 shell 命令体组成。与 make 不同，just 不追踪文件依赖或时间戳，只是简单地运行指定命令。这使它非常适合任务自动化、开发工作流和项目脚本。

变量可以定义并通过 **{{variable}}** 语法引用。环境变量可以直接访问，配方也可以导出变量。此外还支持条件语句、默认值和错误处理。

Just 通过类 shebang 语法让每个配方可以使用不同的 shell（sh、bash、powershell、python 等）。配方可以有依赖（先运行的其他配方），以 _ 为前缀的私有配方则不会出现在 --list 中。

得益于跨平台支持，同一份 justfile 可以在 Linux、macOS 和 Windows 上工作。该工具速度很快（用 Rust 编写）且没有任何依赖。

# CAVEATS

不是构建系统——没有增量构建和依赖追踪。虽然语法相似，但与 make 并不相同。shell 差异可能影响跨平台配方。变量作用域规则与 make 不同。注释使用 #（并非在配方的所有位置都支持）。

# HISTORY

**just** 由 Casey Rodarmor 自 **2016 年**前后开始开发，作为比 make 更简单的命令运行替代品。由于不满 make 的复杂性及其对构建（而非运行命令）的偏重，他为"运行项目专属任务"这一常见场景设计了 just。该工具已在 Rust 社区乃至更广的范围流行开来。

# INSTALL

```apt: sudo apt install just```

```dnf: sudo dnf install just```

```pacman: sudo pacman -S just```

```apk: sudo apk add just```

```zypper: sudo zypper install just```

```brew: brew install just```

```nix: nix profile install nixpkgs#just```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [task](/man/task)(1), [rake](/man/rake)(1), [npm-run-script](/man/npm-run-script)(1)
