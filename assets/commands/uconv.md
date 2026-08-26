# TAGLINE

ICU 字符编码转换器与音译器

# TLDR

**将文件从一种编码转换为另一种**

```uconv -f [ISO-8859-1] -t [UTF-8] [input.txt] -o [output.txt]```

**列出所有可用编码**

```uconv -l```

**转换并音译为 ASCII**

```uconv -f [UTF-8] -t [US-ASCII] -x [Any-Latin; Latin-ASCII] [input.txt]```

**列出可用的音译器**

```uconv -L```

**显示默认编码**

```uconv --default-code```

**对无法映射的字符使用替代回调进行转换**

```uconv -f [UTF-8] -t [ISO-8859-1] --callback substitute [input.txt]```

# SYNOPSIS

**uconv** [_options_] [-f _from_] [-t _to_] [_file_...]

# PARAMETERS

**-f**, **--from-code** _encoding_
> 源编码。

**-t**, **--to-code** _encoding_
> 目标编码。

**-o**, **--output** _file_
> 将输出写入文件而不是标准输出。

**-x** _transliteration_
> 应用音译规则。

**-l**, **--list**
> 列出所有可用编码。

**-L**, **--list-transliterators**
> 列出可用的音译器。

**--default-code**
> 显示默认系统编码。

**--from-callback** _name_
> 从源编码转换到 Unicode 时处理错误的回调。

**--to-callback** _name_
> 从 Unicode 转换到目标编码时处理错误的回调。

**--callback** _name_
> 将 --from-callback 和 --to-callback 同时设为相同值。取值：substitute、skip、stop、escape-unicode。

**-c**
> 从输出中省略无效字符（--to-callback skip 的简写）。

**--add-signature**
> 若目标编码支持，则在输出中添加 U+FEFF BOM。

**--remove-signature**
> 从输入中移除 U+FEFF BOM。

**-s**, **--silent**
> 执行期间不输出消息。

**-v**, **--verbose**
> 执行期间显示额外的提示信息。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**uconv** 使用 ICU（International Components for Unicode）库在字符编码之间转换文本。它支持 200 多种编码和 1000 多个别名，适合复杂的国际化任务。

除了简单的转码之外，uconv 还提供音译能力，可以在不同文字系统之间转换文本（例如西里尔文转拉丁文），而不做翻译。多个音译器可以用分号串联。

错误回调控制无法映射的字符的处理方式。回调可以分别为源编码步骤（--from-callback）和目标编码步骤（--to-callback）单独设置，也可以用 --callback 一次设定两者。选项包括 substitute（替换字符）、skip、stop（默认）和 escape-unicode。

# CAVEATS

属于 ICU 开发者工具的一部分，并非所有系统都默认安装。音译规则使用 ICU 格式语法。某些编码转换可能丢失信息。大文件会在内存中处理。

# HISTORY

**uconv** 是 ICU（International Components for Unicode）项目的一部分，该项目最初由 IBM 开发，现由 Unicode 联盟维护。ICU 为软件国际化提供全面的 Unicode 支持，而 uconv 则以命令行方式开放其转换能力。

# INSTALL

```apt: sudo apt install icu-devtools```

```dnf: sudo dnf install icu```

```pacman: sudo pacman -S icu```

```apk: sudo apk add icu```

```zypper: sudo zypper install icu```

```nix: nix profile install nixpkgs#icu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iconv](/man/iconv)(1), [recode](/man/recode)(1), [file](/man/file)(1), [locale](/man/locale)(1)
