# TAGLINE

Google C++ 风格指南检查器

# TLDR

**检查单个文件**

```cpplint [file.cpp]```

**检查多个文件**

```cpplint [file1.cpp] [file2.cpp]```

**递归检查目录**

```cpplint --recursive [src/]```

**过滤特定类别**

```cpplint --filter=-whitespace,+build [file.cpp]```

**设置行长度**

```cpplint --linelength=[120] [file.cpp]```

**以其他格式输出**

```cpplint --output=[vs7] [file.cpp]```

# SYNOPSIS

**cpplint** [_options_] _files_

# DESCRIPTION

**cpplint** 是一个 C++ 静态代码检查器，依据 Google 的 C++ 风格指南验证代码。它检查风格错误、格式问题以及常见编程失误，在项目内强制执行一致的代码标准。

该工具检查源文件是否符合命名约定、空格规则、注释格式、头文件保护宏模式等众多风格要求。它帮助团队保持统一的代码风格，并在代码评审之前发现常见错误。

cpplint 最初由 Google 为内部使用而开发，现在作为开源项目维护。虽然专为 Google 风格指南设计，但其规则可以通过过滤和自定义来适配采用不同约定的项目。

# PARAMETERS

**--recursive**
> 递归检查子目录中的文件

**--filter**=_-/+categories_
> 启用/禁用特定的警告类别

**--linelength**=_length_
> 最大行长度（默认 80）

**--extensions**=_list_
> 要处理的文件扩展名

**--headers**=_list_
> 头文件的扩展名

**--output**=_format_
> 输出格式：emacs、vs7、eclipse、junit、sed、gsed

**--counting**=_type_
> 错误统计方式：total、toplevel、detailed

**--root**=_dir_
> 项目根目录，用于生成头文件保护宏路径

**--exclude**=_pattern_
> 排除匹配模式的文件

# FILTER CATEGORIES

- **build**: 构建相关问题
- **legal**: 版权/许可证问题
- **readability**: 代码可读性
- **runtime**: 运行时问题
- **whitespace**: 空格与排版

前缀 - 表示禁用，+ 表示启用。

# CONFIGURATION

**CPPLINT.cfg**
> 项目级配置文件，用于设置过滤器、行长度、根目录和排除路径。

# CAVEATS

专为符合 Google 风格指南而设计。某些规则未必适用于所有项目。项目级配置请使用 CPPLINT.cfg 文件。

# INSTALL

```brew: brew install cpplint```

```nix: nix profile install nixpkgs#cpplint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang-format](/man/clang-format)(1), [clang-tidy](/man/clang-tidy)(1), [cppcheck](/man/cppcheck)(1)

# RESOURCES

```[Source code](https://github.com/cpplint/cpplint)```

<!-- verified: 2026-06-23 -->
