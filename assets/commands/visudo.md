# TAGLINE

安全编辑 sudoers 配置

# TLDR

**编辑 sudoers 文件**

```sudo visudo```

**编辑指定文件**

```sudo visudo -f [/etc/sudoers.d/custom]```

**仅检查语法**

```sudo visudo -c```

**检查指定文件**

```sudo visudo -c -f [/etc/sudoers.d/custom]```

**严格模式**

```sudo visudo -s```

# SYNOPSIS

**visudo** [_-c_] [_-f file_] [_-s_] [_options_]

# PARAMETERS

**-c**
> 启用仅检查模式。检查现有 sudoers 文件的语法错误、所有者和权限模式。

**-f** _FILE_
> 指定要编辑或检查的其他 sudoers 文件，而不是默认的 /etc/sudoers。

**-s**
> 启用严格检查。如果别名在定义之前被使用，visudo 会将其视为解析错误。

**-q**
> 启用安静模式。不打印语法错误的详细信息。仅与 -c 组合使用时才有意义。

**-O**
> 强制使用 sudoers 文件的默认所有者（用户和组）。

**-P**
> 强制使用 sudoers 文件的默认权限模式。

**-h**
> 显示简短帮助信息并退出。

**-V**
> 显示版本号并退出。

# DESCRIPTION

**visudo** 安全地编辑 sudoers 文件。它会锁定文件、校验语法，并防止保存无效配置。

语法校验至关重要。sudoers 中的语法错误可能导致所有 sudo 访问被锁死。visudo 会在保存前捕获这些错误。

所使用的编辑器由 SUDO_EDITOR、VISUAL 或 EDITOR 环境变量决定。默认为 vi。

该工具会处理文件锁定，防止多人同时编辑，避免并发更改造成损坏。

/etc/sudoers.d/ 目录下的插入式文件可以用 -f 编辑。它们由主 sudoers 文件引入。

检查模式在不编辑的情况下校验现有文件。适合在部署前验证配置。

# CAVEATS

需要 root 权限。编辑器必须可信。语法错误会被捕获，但逻辑错误不会。编辑期间保持一个 root shell 开着。

# HISTORY

**visudo** 自 **Todd Miller** 开发 **sudo** 的早期起就是其组成部分。它为编辑安全关键的 sudoers 文件提供了必要的安全保障。

# INSTALL

```apt: sudo apt install sudo```

```dnf: sudo dnf install sudo```

```pacman: sudo pacman -S sudo```

```apk: sudo apk add sudo```

```zypper: sudo zypper install sudo```

```nix: nix profile install nixpkgs#sudo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [su](/man/su)(1), [vi](/man/vi)(1)
