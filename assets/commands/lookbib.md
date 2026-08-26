# TAGLINE

交互式检索文献数据库，供 groff/troff 的 refer 使用

# TLDR

**检索文献数据库**

```lookbib [database]```

**以特定关键词检索**

```lookbib [database] <<< "[search terms]"```

**检索多个数据库**

```lookbib [database1] [database2]```

# SYNOPSIS

**lookbib** [_options_] _database_...

# PARAMETERS

**-i** _string_
> 索引文件后缀。

**-t** _n_
> 将关键字截断为 n 个字符。

# DESCRIPTION

**lookbib** 以交互方式检索文献数据库，服务于 groff/troff 的 refer 预处理流程。它会提示输入关键字，并显示匹配的文献条目。

该工具使用由 indxbib 创建的索引文件实现快速检索。在提示符处输入关键字即可查找文献；输入空行则退出。

# EXAMPLE SESSION

```
$ lookbib refs.bib
> knuth algorithms
%A Donald E. Knuth
%T The Art of Computer Programming
%D 1997
>
```

# DATABASE FORMAT

```
%A Author Name
%T Title of Work
%J Journal Name
%D Date
%V Volume
%P Pages
```

# CAVEATS

需要先用 indxbib 创建索引。属于 groff refer 体系的一部分。仅支持交互式使用；文档处理请使用 refer。

# HISTORY

lookbib 起源于贝尔实验室的 **troff** 文档排版系统，是 20 世纪 70 年代开发的 **refer** 文献管理系统的组成部分。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[refer](/man/refer)(1), [indxbib](/man/indxbib)(1), [lkbib](/man/lkbib)(1), [groff](/man/groff)(1)
