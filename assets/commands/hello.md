# TAGLINE

友好的问候程序

# TLDR

**输出 hello world**

```hello```

**传统问候语**

```hello -t```

**指定问候语**

```hello -g "Custom greeting"```

**显示版本**

```hello -v```

# SYNOPSIS

**hello** [_options_]

# PARAMETERS

**-g**, **--greeting** _TEXT_
> 自定义问候语文本。

**-t**, **--traditional**
> 使用传统的 "hello, world" 问候语。

**-h**, **--help**
> 显示帮助信息并退出。

**-v**, **--version**
> 显示版本和许可信息并退出。

# DESCRIPTION

**GNU Hello** 是一个友好的问候程序。它是 GNU 编码规范的一个示例，也是新 GNU 软件包的模板。

该程序演示了 gettext、autoconf 及其他 GNU 基础设施的正确用法，适合用于测试和学习。

# CAVEATS

示例程序，不适用于生产环境，仅用于演示 GNU 规范。

# HISTORY

GNU Hello 作为 **GNU 计划**的一部分而创建，用作演示 GNU 软件包规范的示例程序。

# INSTALL

```apt: sudo apt install hello```

```dnf: sudo dnf install hello```

```apk: sudo apk add mbedtls2-utils```

```zypper: sudo zypper install hello```

```brew: brew install hello```

```nix: nix profile install nixpkgs#hello```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[echo](/man/echo)(1), [printf](/man/printf)(1), [cowsay](/man/cowsay)(6)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/hello.git)```

```[Homepage](https://www.gnu.org/software/hello/)```

```[Documentation](https://www.gnu.org/software/hello/manual/)```

<!-- verified: 2026-07-19 -->
