# TAGLINE

校验 Perl POD 文档语法

# TLDR

**检查 POD 语法**

```podchecker [file.pod]```

**检查多个文件**

```podchecker [*.pod]```

**仅显示警告**

```podchecker -warnings [file.pod]```

# SYNOPSIS

**podchecker** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要检查的 POD 文件。

**-warnings**
> 显示警告。可多次指定以提高警告级别（最多 **-warnings -warnings**）。

**-nowarnings**
> 抑制警告（默认显示警告）。

**-help**
> 打印用法信息并退出。

**-man**
> 打印手册页并退出。

# DESCRIPTION

**podchecker** 校验 Perl POD（Plain Old Documentation）文件的语法，报告诸如未知格式代码、begin/end 块不匹配、标题格式错误等问题。

它既检查会导致错误渲染的严重错误，也报告关于可疑结构的警告。使用 **-warnings** 控制警告输出的级别。它是标准 Perl 发行版的一部分。

# CAVEATS

Perl 特有格式。标准的 Perl 工具。

# HISTORY

podchecker 是为了**校验 POD** 文档语法而创建的。

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

[pod2man](/man/pod2man)(1), [pod2html](/man/pod2html)(1), [pod2text](/man/pod2text)(1), [podselect](/man/podselect)(1), [perldoc](/man/perldoc)(1)
