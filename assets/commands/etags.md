# TAGLINE

Emacs 标签文件生成器

# TLDR

**生成 TAGS 文件**

```etags [*.c] [*.h]```

**追加到现有 TAGS**

```etags -a [newfile.c]```

**输出到指定文件**

```etags -o [MYTAGS] [*.c]```

**处理文件列表中的文件**

```etags - < [filelist.txt]```

**按指定语言处理**

```etags --language=[c++] [*.cpp]```

**递归处理目录**

```find . -name "*.py" | etags -```

# SYNOPSIS

**etags** [_options_] _files_...

# DESCRIPTION

**etags** 为 Emacs 生成标签文件。标签支持在源文件之间跳转到函数定义、变量声明和其他符号。

该工具解析源文件并创建包含符号位置的 TAGS 文件。Emacs 借助它配合 M-.（find-tag）及相关命令进行代码导航。

# PARAMETERS

**-a**, **--append**
> 追加到现有的 TAGS 文件。

**-o** _file_
> 输出到指定文件。

**-l** _lang_, **--language=** _lang_
> 强制指定后续文件的语言。

**-I**, **--include=** _file_
> 包含另一个标签文件。

**-r** _regex_, **--regex=** _regex_
> 为匹配正则表达式的行生成标签。

**-**
> 从标准输入读取文件名。

**--help**
> 显示帮助。

# SUPPORTED LANGUAGES

C、C++、Java、Python、Perl、Ruby、Lisp、Scheme、Fortran、Pascal、PHP、Lua、Erlang 等众多语言。

# CAVEATS

与 ctags（Vim 标签）不同。TAGS 文件可能变得很大。代码更改后需要重新生成。部分语言的支持有限。

# HISTORY

**etags** 自早期版本起就是 **GNU Emacs** 的一部分，提供与 ctags 对应的 Emacs 版工具。该工具在保持与 Emacs 标签导航兼容的同时，已发展为支持多种编程语言。

# INSTALL

```dnf: sudo dnf install emacs```

```pacman: sudo pacman -S emacs```

```apk: sudo apk add emacs```

```zypper: sudo zypper install emacs```

```brew: brew install emacs```

```nix: nix profile install nixpkgs#emacs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ctags](/man/ctags)(1), [emacs](/man/emacs)(1), [cscope](/man/cscope)(1)
