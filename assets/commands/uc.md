# TAGLINE

支持 Unicode 的大写转换过滤器

# TLDR

**将字符串转为大写**

```echo "[straße]" | uc```

**将文件内容转为大写**

```uc < [input.txt] > [output.txt]```

**转小写再转回来做往返测试**

```cat [file.txt] | uc | lc```

**正确处理连字的大写转换**

```printf "[ﬃ]\n" | uc```

# SYNOPSIS

**uc** [_file_ ...]

# DESCRIPTION

**uc** 从标准输入（或指定文件）读取文本，应用完整的 Unicode **toUpper** 大小写映射，并将结果写到标准输出。与朴素的 **tr 'a-z' 'A-Z'** 不同，它能处理会改变长度的折叠情况（德语 **ß** → **SS**、连字 **ﬃ** → **FFI**），并遵守希腊语、西里尔文、亚美尼亚文等其他文字的语言特定规则。

它是 **Tom Christiansen 的 Unicode::Tussle** Perl 发行版中约三十个小过滤器脚本之一，同类的还有 **lc**（小写）、**tc**（标题大小写）、**nfd**/**nfc**/**nfkd**/**nfkc**（规范化）、**ucsort**、**uniwc** 和 **tcgrep**——它们共同构成了许多 GNU coreutils 工具的 Unicode 正确替代品。

# CAVEATS

**uc** 这个名字有歧义，与 Perl 内置的 **uc()** 函数以及其他平台上一些不相关的工具重名。该脚本在大多数发行版上默认不安装；使用 **cpanm Unicode::Tussle** 可安装整套工具。由于其大小写映射与 locale 无关，针对特定语言的规则（例如土耳其语的带点/不带点 **I**）不会被应用。

# HISTORY

**Unicode::Tussle** 由 **Tom Christiansen** 在 **OSCON 2011** 上展示的一次性脚本集合发展而来，现由 **brian d foy** 打包发布在 **CPAN** 上。该发行版是 Perl 领域 "Unicode coreutils" 的标准参考实现。

# SEE ALSO

[tc](/man/tc)(1), [tr](/man/tr)(1), [iconv](/man/iconv)(1)
