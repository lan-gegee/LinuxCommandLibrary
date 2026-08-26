# TAGLINE

将 Perl POD 文档转换为 HTML

# TLDR

**将 POD 文件转换为 HTML**

```pod2html --infile=[file.pod] --outfile=[file.html]```

**以自定义 HTML 标题转换**

```pod2html --title="[My Module]" --infile=[file.pod] --outfile=[file.html]```

**引入外部 CSS 样式表**

```pod2html --css=[style.css] --infile=[file.pod] --outfile=[file.html]```

**转换时不生成目录**

```pod2html --noindex --infile=[file.pod] --outfile=[file.html]```

**从标题添加返回页面顶部的反向链接**

```pod2html --backlink --infile=[file.pod] --outfile=[file.html]```

**转换前清空 pod2html 缓存**

```pod2html --flush --infile=[file.pod] --outfile=[file.html]```

# SYNOPSIS

**pod2html** [_options_]

# PARAMETERS

**--infile=**_name_
> POD 输入文件。默认为 STDIN。

**--outfile=**_name_
> HTML 输出文件。默认为 STDOUT。

**--title=**_name_
> 设置 HTML 文档标题。

**--css=**_URL_
> 链接到层叠样式表。

**--index** / **--noindex**
> 在 HTML 输出顶部包含或省略目录。默认启用。

**--backlink** / **--nobacklink**
> 从每个标题添加返回页面顶部的链接。

**--header** / **--noheader**
> 根据 POD NAME 区生成横幅页眉和页脚。

**--htmldir=**_name_
> 生成指向其他 HTML 文件的相对交叉引用时使用的目录。

**--htmlroot=**_URL_
> 绝对 HTML 交叉引用链接的基础 URL。

**--podpath=**_dirs_
> 包含 pod 文件的目录列表（以冒号分隔），用于解析 L<> 链接。

**--podroot=**_name_
> 库 pod 文件的基础目录。

**--cachedir=**_name_
> pod2html 存放缓存的目录。默认：当前目录。

**--flush**
> 处理前清空缓存。

**--recurse** / **--norecurse**
> 递归进入 **--podpath** 指定的子目录。

**--quiet** / **--verbose**
> 抑制警告或显示进度信息。

**--poderrors** / **--nopoderrors**
> 在输出中包含或省略 POD 错误部分。

# DESCRIPTION

**pod2html** 将 Perl POD（Plain Old Documentation）源码转换为 HTML，解析 L<> 超链接并将 POD 格式指令转换为 HTML 标记。它可以选择根据 =head 指令构建前置目录，并在标题与文档顶部之间插入反向链接。

该工具依赖一个缓存（默认存储在工作目录中），将 pod 名称映射到 URL，以便跨多次运行高效地解析页面间的交叉引用。移动或重命名源 pod 后应使用 **--flush**。

# CAVEATS

缓存默认创建在当前目录中，这可能会让期望该工具无状态的用户感到意外；使用 **--cachedir** 改变其位置，或用 **--flush** 重建。

# HISTORY

**pod2html** 随标准 Perl 发行版一同发布，是 Pod::Html 模块的一部分，自早期 Perl 5 版本起就已包含在内。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pod2man](/man/pod2man)(1), [pod2text](/man/pod2text)(1), [perldoc](/man/perldoc)(1), [perl](/man/perl)(1)
