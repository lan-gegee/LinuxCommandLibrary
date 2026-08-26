# TAGLINE

从电子邮件中提取 MIME 附件

# TLDR

将附件提取到**当前目录**

```ripmime -i path/to/file```

将附件提取到**指定目录**

```ripmime -i path/to/file -d path/to/directory```

以**详细输出**方式提取

```ripmime -i path/to/file -v```

获取解码的**调试信息**

```ripmime -i path/to/file --debug```

# SYNOPSIS

**ripmime** [_options_] -i _file_

# PARAMETERS

**-i** _file_
> 输入的 MIME 编码文件。

**-d** _directory_
> 提取附件的输出目录。

**-v**
> 启用详细输出。

**--debug**
> 显示详细的解码信息。

# DESCRIPTION

**ripmime** 从 MIME 编码的邮件包中提取附件。它解析邮件文件，并将内嵌的附件保存到磁盘。

该工具支持多种 MIME 编码类型，可以处理包含多个附件或嵌套结构的邮件。

# CAVEATS

从不可信的邮件中提取附件时要格外小心，因为它们可能包含恶意软件。打开附件前请先确认其安全性。

# HISTORY

为自动化邮件处理和附件提取而开发。常用于邮件过滤和归档系统。

# INSTALL

```apt: sudo apt install ripmime```

```dnf: sudo dnf install ripmime```

```apk: sudo apk add ripmime```

```brew: brew install ripmime```

```nix: nix profile install nixpkgs#ripmime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[munpack](/man/munpack)(1), [mpack](/man/mpack)(1)
