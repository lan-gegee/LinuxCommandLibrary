# TAGLINE

将 DOS/Windows 换行符转换为 Unix 格式

# TLDR

**转换**文件换行符

```dos2unix [path/to/file]```

创建保留 Unix 换行符的**副本**

```dos2unix -n [path/to/file] [path/to/new_file]```

显示**文件信息**

```dos2unix -i [path/to/file]```

处理 **BOM**（保留/添加/移除）

```dos2unix --[keep-bom|add-bom|remove-bom] [path/to/file]```

**原地转换并保留时间戳**

```dos2unix -k [path/to/file]```

**一次转换多个文件**

```dos2unix [file1] [file2] [file3]```

强制转换**被检测为二进制**的文件

```dos2unix -f [path/to/file]```

# SYNOPSIS

**dos2unix** [_options_] [_file_...]

**dos2unix** [_options_] **-n** _infile_ _outfile_ ...

# DESCRIPTION

**dos2unix** 将文本文件从 DOS/Windows 格式（CRLF 换行符）转换为 Unix 格式（LF 换行符）。DOS/Windows 系统使用回车加换行（\r\n）标记行尾，而类 Unix 系统只使用换行符（\n）。

换行符不匹配会导致脚本出错、编译失败或文本编辑器显示异常。该工具通过将换行符规范化为 Unix 标准来解决这些问题。它还能处理来自 Windows 的 UTF-8 文件中常见的字节顺序标记（BOM）。

默认情况下该工具就地操作，直接修改原文件，但也可以创建新输出文件并保留原文件。它能智能检测文件格式，并在转换前提供文件当前换行符格式的相关信息。

# PARAMETERS

**-o**, **--oldfile** _file_...
> 旧文件模式：转换每个文件并覆盖原文件。这是默认行为。

**-n**, **--newfile** _infile_ _outfile_...
> 新文件模式：转换 _infile_ 并把结果写入 _outfile_，原文件保持不变。

**-i**[_FLAGS_], **--info**[=_FLAGS_] _file_...
> 报告每个文件的换行符数量、BOM 以及文本/二进制状态。不做任何转换。

**-c**, **--convmode** _mode_
> 转换模式：**ascii**（默认）、**7bit**、**iso** 或 **mac**。

**-k**, **--keepdate**
> 让输出文件的时间戳与输入文件相同。

**-s**, **--safe**
> 跳过二进制文件。这是默认行为。

**-f**, **--force**
> 即使文件看起来是二进制也进行转换。

**-F**, **--follow-symlink**
> 跟随符号链接并转换其目标文件。

**-b**, **--keep-bom**
> 保留字节顺序标记：若输入含有 BOM，则输出中也写入 BOM。

**-m**, **--add-bom**
> 向输出写入字节顺序标记（默认为 UTF-8）。

**-r**, **--remove-bom**
> 不向输出写入字节顺序标记。

**-e**, **--add-eol**
> 若最后一行缺少换行符则补上。

**-l**, **--newline**
> 额外添加一个换行符，把每个单换行变成双换行。

**-u**, **--keep-utf16**
> 保留输入文件原有的 UTF-16 编码，而不转换为 UTF-8。

**-ul**, **--assume-utf16le** / **-ub**, **--assume-utf16be**
> 当没有 BOM 表明编码时，假定输入为 UTF-16 小端序或大端序。

**-q**, **--quiet**
> 安静模式：抑制所有警告和消息。

**-v**, **--verbose**
> 报告关于字节顺序标记和所执行转换的额外细节。

**--allow-chown**
> 允许在旧文件模式下发生文件所有者变更。

**-V**, **--version**
> 显示版本信息并退出。

# CAVEATS

默认行为是就地修改文件，因此如果原文件很重要，请保留副本或使用 **-n**。在旧文件模式下，dos2unix 会先写一个新文件再将其重命名覆盖旧文件，因此以其他用户身份运行时目标文件的所有者可能改变，这也是必须显式给出 **--allow-chown** 的原因。二进制文件默认被跳过（**-s**），对真正的二进制文件用 **-f** 强制转换会损坏它，所以不确定时先用 **-i** 检查。注意 ASCII 转换模式只重写换行符，不做字符集转码，而 **iso** 模式假定的特定 DOS 代码页可能与你的文件不匹配。

# HISTORY

自 20 世纪 80 年代末起，dos2unix 就以各种形式存在，当时在 DOS 与 Unix 之间移动文本是日常操作。如今每个 Linux 发行版附带的版本都是 **Erwin Waterlander** 于 **2009 年**开始的重写版，它为这个原本非常小的工具增加了 Unicode 和 UTF-16 支持、BOM 处理以及 mac 转换模式。它与执行反向转换的 **unix2dos** 一同发布，两者通常是同一个二进制文件以不同名称调用。

# INSTALL

```apt: sudo apt install dos2unix```

```dnf: sudo dnf install dos2unix```

```pacman: sudo pacman -S dos2unix```

```apk: sudo apk add dos2unix```

```zypper: sudo zypper install dos2unix```

```brew: brew install dos2unix```

```nix: nix profile install nixpkgs#dos2unix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unix2dos](/man/unix2dos)(1), [unix2mac](/man/unix2mac)(1), [file](/man/file)(1), [iconv](/man/iconv)(1), [tr](/man/tr)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/dos2unix/)```

```[Homepage](https://dos2unix.sourceforge.io/)```

<!-- verified: 2026-07-14 -->
