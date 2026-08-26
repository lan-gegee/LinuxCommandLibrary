# TAGLINE

在 PDF 文件中搜索文本模式，类似于面向 PDF 的 grep

# TLDR

**在 PDF 中搜索模式**

```pdfgrep "[pattern]" [file.pdf]```

**不区分大小写地搜索并显示页码**

```pdfgrep -in "[pattern]" [file.pdf]```

**在目录中递归搜索**

```pdfgrep -r "[pattern]" [/path/to/pdfs/]```

**统计每个文件的匹配数**

```pdfgrep -c "[pattern]" [*.pdf]```

**只打印有匹配的文件名**

```pdfgrep -l "[pattern]" [*.pdf]```

**使用多个模式搜索**

```pdfgrep -e "[pattern1]" -e "[pattern2]" [file.pdf]```

**将搜索限制在页面范围内**

```pdfgrep --page-range=[1-10] "[pattern]" [file.pdf]```

**只打印匹配到的文本**

```pdfgrep -o "[pattern]" [file.pdf]```

# SYNOPSIS

**pdfgrep** [_OPTIONS_] _PATTERN_ _FILE_...

**pdfgrep** [_OPTIONS_] {**-e** _PATTERN_|**-f** _FILE_}... _FILE_...

**pdfgrep** [_OPTIONS_] **-r**|**-R** _PATTERN_ [_FILE_|_DIR_...]

# PARAMETERS

**-e** _PATTERN_, **--regexp**=_PATTERN_
> 指定搜索模式。可多次使用以匹配多个模式中的任意一个。

**-f** _FILE_, **--file**=_FILE_
> 从文件读取模式，每行一个。

**-i**, **--ignore-case**
> 不区分大小写匹配。

**-F**, **--fixed-strings**
> 将模式视为固定字符串（不按正则表达式解释）。

**-P**, **--perl-regexp**
> 使用 Perl 兼容正则表达式（PCRE2）。

**-n**, **--page-number**[=_TYPE_]
> 在每个匹配前加上其页码。_TYPE_ 为 `index`（默认）或 `label`。

**-c**, **--count**
> 打印每个文件的匹配数而非匹配行。

**-p**, **--page-count**
> 打印每页的匹配数（隐含 **-n**）。

**-l**, **--files-with-matches**
> 只打印含有匹配的文件名。

**-L**, **--files-without-match**
> 只打印不含匹配的文件名。

**-o**, **--only-matching**
> 只打印每行中匹配的部分。

**-H**, **--with-filename**
> 在每个匹配前打印文件名（搜索多个文件时默认启用）。

**-h**, **--no-filename**
> 在输出中不显示文件名前缀。

**-Z**, **--null**
> 用空字节代替冒号来分隔文件名与输出行的其余部分。适用于包含冒号或空格的文件名。

**--match-prefix-separator** _SEP_
> 使用 _SEP_ 作为匹配前缀（文件名、页码）与匹配行之间的分隔符，代替默认的冒号。

**-r**, **--recursive**
> 递归搜索每个目录下的所有 PDF 文件。仅当符号链接在命令行上显式给出时才会跟随。

**-R**, **--dereference-recursive**
> 与 **-r** 类似，但跟随所有符号链接。

**--include**=_GLOB_
> 只搜索文件名匹配 _GLOB_ 的文件（默认：`*.pdf`）。

**--exclude**=_GLOB_
> 跳过文件名匹配 _GLOB_ 的文件。

**-A** _NUM_, **--after-context**=_NUM_
> 打印每个匹配之后的 _NUM_ 行上下文。

**-B** _NUM_, **--before-context**=_NUM_
> 打印每个匹配之前的 _NUM_ 行上下文。

**-C** _NUM_, **--context**=_NUM_
> 打印每个匹配前后的 _NUM_ 行上下文。

**--page-range**=_RANGE_
> 将搜索限制在指定的页面范围内（例如 `1-10,15`）。

**-m** _NUM_, **--max-count**=_NUM_
> 每个文件在匹配 _NUM_ 次后停止。

**--password**=_PASSWORD_
> 使用 _PASSWORD_ 解密受密码保护的 PDF。

**--color** _WHEN_
> 输出着色：`auto`（默认）、`always` 或 `never`。

**--cache**
> 缓存渲染后的页面文本，加速对相同文件的重复搜索。

**--unac**
> 从搜索模式和文档文本中去除重音符号和连字。有助于让 "ae" 之类的词匹配连字 "æ"。

**--warn-empty**
> 当 PDF 不含可搜索文本时发出警告（例如未经 OCR 的扫描图像）。

**-q**, **--quiet**
> 抑制全部输出。退出状态表明是否找到匹配。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**pdfgrep** 使用 Poppler 库提取文本，在 PDF 文件中搜索文本模式。它为 PDF 文档提供了类似 grep 的熟悉界面。

文本会从每一页中提取并与给定正则表达式进行匹配。默认情况下 pdfgrep 使用 PCRE2 进行模式匹配。固定字符串匹配可通过 **-F** 启用。

页码输出（**-n**）有助于定位文档中的匹配位置。将搜索限制在页面范围内（**--page-range**）可加快大文件的搜索速度。上下文行（**-C**）显示周围的文本，帮助理解匹配内容。

递归搜索（**-r**）会处理整个目录树。结合 **--include** 和 **--exclude** 可对文档集合进行有针对性的搜索。可用重复的 **-e** 选项指定多个模式，也可用 **-f** 从文件读取。

当 PDF 使用了与搜索词不同的排版连字或带重音字符时，**--unac** 选项很有用。**--cache** 选项存储已提取的文本，加速重复搜索。

# EXIT STATUS

**0**
> 找到一个或多个匹配。

**1**
> 未找到匹配。

**2**
> 发生错误。

# CAVEATS

文本提取质量取决于 PDF 的内部结构。没有内嵌文本的扫描版 PDF 需要先做 OCR 预处理才能被 pdfgrep 搜索（可用 **--warn-empty** 检测这类文件）。复杂的多栏版式可能无法按阅读顺序提取。加密的 PDF 需要正确的 **--password**。

# HISTORY

**pdfgrep** 由 **Hans-Peter Deifel** 自约 **2010** 年起编写。它使用 Poppler 库解析 PDF，并为搜索 PDF 文本内容提供 grep 兼容的界面。

# INSTALL

```apt: sudo apt install pdfgrep```

```dnf: sudo dnf install pdfgrep```

```pacman: sudo pacman -S pdfgrep```

```apk: sudo apk add pdfgrep```

```zypper: sudo zypper install pdfgrep```

```brew: brew install pdfgrep```

```nix: nix profile install nixpkgs#pdfgrep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [pdftotext](/man/pdftotext)(1), [ripgrep](/man/ripgrep)(1), [pdfinfo](/man/pdfinfo)(1)
