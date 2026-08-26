# TAGLINE

将 Perl POD 文档转换为 man page

# TLDR

**将 POD 转换为 man page**

```pod2man [file.pod] > [file.1]```

**指定节**

```pod2man --section=[1] [file.pod] > [file.1]```

**设置名称和发行版本**

```pod2man --name="[NAME]" --release="[1.0]" [file.pod] > [file.1]```

# SYNOPSIS

**pod2man** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 POD 文件。

**--section** _N_
> Man page 的节。

**--name** _NAME_
> Man page 名称。

**--release** _VERSION_
> 发行版本字符串。

**--center** _TEXT_
> 居中页眉文本。

**--date** _DATE_
> 左侧页脚中的日期（默认：输入文件的修改日期）。

**--utf8**
> 假定输入为 UTF-8 编码。

**--stderr**
> 将错误打印到 stderr。

**--fixed** _FONT_
> 用于等宽文本的等宽字体。

# DESCRIPTION

**pod2man** 是 Pod::Man 的前端，将 Perl POD（Plain Old Documentation）转换为 Unix 手册页格式（*roff）。输出可以通过 **man** 使用 **nroff** 显示，或用 **troff** 打印。

如果不提供输入文件，它会从 STDIN 读取。如果不提供输出文件，它会写入 STDOUT。默认的居中页眉是 "User Contributed Perl Documentation"。它是标准 Perl 发行版的一部分，常用于模块构建系统。

# CAVEATS

Perl 特有格式。标准的 Perl 工具。

# HISTORY

pod2man 是为了从 Perl 文档**生成 man page**而创建的。

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

[pod2html](/man/pod2html)(1), [pod2text](/man/pod2text)(1), [man](/man/man)(1), [nroff](/man/nroff)(1)
