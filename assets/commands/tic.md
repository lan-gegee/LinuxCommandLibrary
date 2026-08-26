# TAGLINE

编译 terminfo 终端描述文件

# TLDR

**编译**并安装 terminfo

```tic -xe [terminal] [path/to/terminal.info]```

**检查** terminfo 的错误

```tic -c [path/to/terminal.info]```

打印数据库**位置**

```tic -D```

# SYNOPSIS

**tic** [_OPTIONS_] _FILE_

# PARAMETERS

**-c**
> 检查 terminfo 文件的错误但不安装

**-x**
> 编译时将未知的能力项视为用户自定义能力

**-e** _NAMES_
> 只编译指定的终端名称

**-D**
> 打印数据库位置

**-o** _DIR_
> 将编译后的文件写入指定目录

**-v** _N_
> 详细输出（0-10）

# DESCRIPTION

**tic** 将 terminfo 源文件编译为 ncurses 及其他终端处理库使用的二进制格式。编译后的描述会安装到 terminfo 数据库中，供程序查询使用。

terminfo 描述终端的各种能力，如光标移动、颜色支持和特殊按键。

# CAVEATS

安装到系统目录需要 root 权限。源文件中的语法错误会导致编译失败。可在安装前先用 -c 进行校验。

# HISTORY

**tic** 是 **ncurses** 库的一部分，后者是类 Unix 系统的标准终端处理库。terminfo 取代了较旧的 termcap 格式来描述终端能力。

# INSTALL

```apt: sudo apt install ncurses-bin```

```dnf: sudo dnf install ncurses```

```pacman: sudo pacman -S ncurses```

```apk: sudo apk add ncurses```

```brew: brew install ncurses```

```nix: nix profile install nixpkgs#ncurses```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[infocmp](/man/infocmp)(1), [toe](/man/toe)(1)
