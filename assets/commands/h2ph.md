# TAGLINE

将 C 头文件转换为 Perl 头文件

# TLDR

**将 C 头文件转换为 Perl**

```h2ph [header.h]```

**递归处理所有系统头文件**

```cd /usr/include && h2ph -r -l *.h```

**输出到指定目录**

```h2ph -d [/usr/lib/perl5] [header.h]```

**转换某个头文件及其包含的所有头文件**

```h2ph -a [sys/types.h]```

# SYNOPSIS

**h2ph** [_options_] [_headerfiles_...]

# PARAMETERS

_HEADERFILES_
> 要转换为 Perl 头文件（.ph）的 C 头文件（.h）。

**-d** _DIR_
> 将生成的 .ph 文件放在指定目录之下，而非默认的 Perl 库位置。

**-r**
> 递归运行，转换指定目录及其子目录中的所有 .h 文件。

**-a**
> 自动运行；转换指定的头文件以及它们包含的所有 .h 文件。

**-l**
> 为重复的输出文件创建符号链接，而非生成独立副本。

**-D** _DIR_
> 在指定目录中搜索被包含的头文件。

**-e**
> 转换过程中遇到错误时，输出文件名并继续解析。

**-Q**
> 静默模式。不打印已转换文件的名称。

# DESCRIPTION

**h2ph** 将 C 头文件（.h）转换为 Perl 头文件（.ph）。它把 **#define** 宏和常量定义翻译成可用 **require** 加载的 Perl 等价物。

该工具最好在 **/usr/include** 下运行以转换系统头文件。它将定义包裹在 **eval** 块中，即使部分定义转换失败，你仍能访问成功转换的部分。默认情况下，输出的 .ph 文件放置在 Perl 的体系结构相关库目录中。

# CAVEATS

只能处理简单的 **#define** 常量和宏。复杂的 C 宏、函数式宏和 typedef 不会被翻译。输出可能需要手动修正。从 C 头文件创建 Perl 扩展时通常更推荐使用 **h2xs** 工具。

# HISTORY

h2ph 自早期版本起就是 **Perl** 发行版的一部分，在 XS 和 h2xs 成为首选方案之前，为 Perl 程序访问系统常量提供了一种快捷方式。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[h2xs](/man/h2xs)(1), [perl](/man/perl)(1)
