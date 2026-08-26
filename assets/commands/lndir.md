# TAGLINE

创建由指向另一目录树的符号链接组成的影子目录树

# TLDR

创建符号链接构成的**影子目录**

```lndir [path/to/source]```

# SYNOPSIS

**lndir** [_options_] _fromdir_ [_todir_]

# DESCRIPTION

**lndir** 创建一个影子目录树，其中的条目是指向另一棵目录树的符号链接。这适用于在独立目录中构建软件，同时保持源码树干净。

# PARAMETERS

**fromdir**
> 作为链接来源的源目录

**todir**
> 目标目录（默认为当前目录）

**-silent**
> 抑制诊断消息

**-ignorelinks**
> 忽略源目录中的符号链接

# CAVEATS

最初是为 X Window System 构建而开发的。默认不跟随源目录中的符号链接。

# INSTALL

```apt: sudo apt install xutils-dev```

```apk: sudo apk add outils-lndir```

```zypper: sudo zypper install lndir```

```brew: brew install lndir```

```nix: nix profile install nixpkgs#lndir```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ln](/man/ln)(1), [cp](/man/cp)(1)
