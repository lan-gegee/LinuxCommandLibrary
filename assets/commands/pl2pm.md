# TAGLINE

将 Perl4 库转换为 Perl5 模块

# TLDR

**将 Perl4 库转换为模块**

```pl2pm [library.pl] > [Module.pm]```

**转换多个文件**

```pl2pm [lib1.pl] [lib2.pl]```

# SYNOPSIS

**pl2pm** [_file_...]

# PARAMETERS

_FILE_
> Perl4 库文件。

输出到 stdout。

# DESCRIPTION

**pl2pm** 将 Perl 4 库文件（.pl）转换为 Perl 5 模块格式（.pm）。它会执行基本的语法变换，例如添加 package 声明、转换 require 语句，以及更新子例程定义以符合 Perl 5 模块的惯例。

它是标准 Perl 发行版的一部分；转换结果只是近似值，输出通常需要人工审查和调整才能成为功能完整的 Perl 5 模块。

# CAVEATS

属于 Perl 的一部分。仅做基础转换。需要人工审查。

# HISTORY

pl2pm 为**将 Perl4 代码迁移到 Perl5 模块**而生。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl](/man/perl)(1), [h2xs](/man/h2xs)(1)
