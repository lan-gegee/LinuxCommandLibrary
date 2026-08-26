# TAGLINE

创建 Perl 扩展模块骨架

# TLDR

**创建不带 AutoLoader 的 XS 模块骨架**

```h2xs -A -n [Module::Name]```

**从 C 头文件创建模块骨架**

```h2xs -n [Module::Name] [header.h]```

**创建纯 Perl 模块（无 XS 代码）**

```h2xs -AX -n [Module::Name]```

**创建模块并在 Perl 绑定中去掉 C 函数名前缀**

```h2xs -n [Module::Name] -p [prefix_] [header.h]```

# SYNOPSIS

**h2xs** [_options_] [_headerfile_ ...] [_extra_libraries_]

# PARAMETERS

_HEADERFILE_
> 一个或多个用于解析 `#define` 常量和函数声明的 C 头文件。

_EXTRA_LIBRARIES_
> 需要链接的额外库，形式如 `-lm -lposix`，可选配合 `-L/path` 以添加搜索目录。

**-n**, **--name**=_MODULE_NAME_
> 指定扩展的名称，例如 `RPC::DCE`。省略时使用第一个头文件的名称（首字母大写）。

**-A**, **--omit-autoload**
> 省略所有 AutoLoader 设施。从 .pm 文件中移除 `use AutoLoader`，并隐含 `-c`。

**-X**, **--omit-XS**
> 省略 XS 部分，生成纯 Perl 模块骨架。隐含 `-c` 和 `-f`。

**-c**, **--omit-constant**
> 从 .xs 文件中省略 `constant()`，并从 .pm 文件中省略对应的 `AUTOLOAD`。

**-O**, **--overwrite-ok**
> 允许覆盖已存在的扩展目录。

**-b**, **--compat-version**=_VERSION_
> 生成的 .pm 文件向后兼容到指定的 Perl 版本（如 `5.005_03`）。低于 5.6.0 的版本会避免使用 `our` 和 `use warnings`。

**-B**, **--beta-version**
> 使用 alpha/beta 风格的版本号（`0.00_01`）而非 `0.01`。

**-C**, **--omit-changes**
> 不创建 `Changes` 文件，改为在 POD 模板中添加 `HISTORY` 一节。

**-F**, **--cpp-flags**=_FLAGS_
> 扫描头文件时传给 C 预处理器的附加标志。同时会写入生成的 `Makefile.PL` 中。

**-M**, **--func-mask**=_REGEX_
> 只选择名称匹配给定正则表达式的函数和宏。

**-P**, **--omit-pod**
> 省略自动生成的 POD 存根部分。

**-a**, **--gen-accessors**
> 为头文件中的结构体和联合体的每个元素生成访问器方法。

**-d**, **--debugging**
> 打开调试消息。

**-e**, **--omit-enums**[=_REGEX_]
> 跳过 C 枚举中定义的常量。如果给出正则表达式，则只跳过名称匹配它的枚举。

**-f**, **--force**
> 允许为标准 include 目录中找不到的头文件创建扩展。

**-g**, **--global**
> 在 .xs 文件中加入安全存储静态数据的代码。

**-k**, **--omit-const-func**
> 对声明为 `const` 的函数参数，在生成的 XS 代码中省略 `const` 属性。

**-m**, **--gen-tied-var**
> （实验性）声明与同名 C 变量魔法绑定的 Perl 变量。

**-o**, **--opaque-re**=_REGEX_
> 将被正则表达式匹配到的 C 类型视为不透明数据类型，即使它们出现在 typemap 中。与 `-x` 配合使用。

**-p**, **--remove-prefix**=_PREFIX_
> 从 Perl 函数名中去掉给定的前缀（如 `-p sec_rgy_`）。

**-s**, **--const-subs**=_SUB1_,_SUB2_
> 为指定宏（假定返回类型为 `char *`）创建 Perl 子程序，而非使用 `constant()` 机制。

**-t**, **--default-type**=_TYPE_
> `constant()` 处理宏时使用的内部类型。默认为 `IV`（有符号整数）。

**-v**, **--version**=_VERSION_
> 设置扩展的版本号。默认为 `0.01`（配合 `-B` 时为 `0.00_01`）。

**-x**, **--autogen-xsubs**
> 根据头文件中的函数声明自动生成 XSUB。需要安装 `C::Scan` 模块。

**--skip-exporter**
> 不使用 `Exporter`，也不导出任何符号。

**--skip-ppport**
> 不使用 `Devel::PPPort`（禁用向旧版 Perl 的可移植性支持）。

**--skip-autoloader**
> 不使用 `AutoLoader`，但保留常量所需的 `constant()` 函数和 `AUTOLOAD` 子程序。

**--skip-strict**
> 不向生成的模块添加 `use strict`。

**--skip-warnings**
> 不向生成的模块添加 `use warnings`。

**--use-new-tests**
> 当 `-b` 生效时，使用 `Test::More` 而非较旧的 `Test` 模块生成测试。

**--use-old-tests**
> 强制使用较旧的 `Test` 模块生成测试。

**-h**, **-?**, **--help**
> 打印用法和版本信息并退出。

# DESCRIPTION

**h2xs** 根据 C 头文件构建 Perl 扩展骨架。它会生成包装 C 库的 XS 代码，使其常量和函数可以从 Perl 中访问，同时还会生成 `Makefile.PL`、`.pm` 模块文件、`.xs` 文件以及测试存根。

如果未通过 `-n` 提供模块名，则使用第一个头文件的名称并将其首字符大写。链接时需要的额外库可以在命令行末尾追加，形式如 `-lm -lposix`，可选配合 `-L/path` 以添加库搜索目录。

该工具还可以通过 `-X` 标志创建纯 Perl 模块（无 XS）骨架。

# CAVEATS

生成的代码经常需要手动定制。复杂的 C API（函数指针、数组、非整数类型）需要对 XS 文件和 typemap 进行手工编辑。`-x` 选项要求安装 `C::Scan` CPAN 模块。

# HISTORY

**h2xs** 自 Perl 5 版本起就是 **Perl** 的一部分，提供了创建 XS 扩展模块的标准方式。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-dev```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[h2ph](/man/h2ph)(1), [perl](/man/perl)(1), [perldoc](/man/perldoc)(1)
