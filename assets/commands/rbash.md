# TAGLINE

Bash shell 的受限模式

# TLDR

**启动受限 shell**

```rbash```

**在受限模式下运行命令**

```rbash -c "[command]"```

**以受限方式运行脚本**

```rbash [script.sh]```

# SYNOPSIS

**rbash** [_options_] [_script_]

# PARAMETERS

**-c** _STRING_
> 执行命令字符串。

**-i**
> 交互模式。

**-l**
> 登录 shell。

**-r**
> 受限模式（默认）。

# DESCRIPTION

**rbash** 是 Bash shell 的一种受限模式，它限制用户操作以防止未经授权的系统访问。当以 rbash 方式调用（或通过 **bash -r**）时，它会禁用 cd 更改目录、阻止修改 PATH、SHELL、ENV 和 BASH_ENV 变量，并禁止使用 >、>> 及相关运算符进行输出重定向。

这些限制还会阻止执行包含斜杠的命令（从而封堵 /bin/command 这类直接路径）、阻止使用 exec 内建命令，以及阻止从环境中导入函数。这使得它在配合只包含受批准命令的严格受控 PATH 时，可用于向不受信任的用户提供有限的 shell 访问。

# RESTRICTIONS

- 不能使用 cd 命令
- 不能修改 PATH
- 不能进行输出重定向
- 不能使用 exec 命令
- 不能通过命令替换赋值

# CAVEATS

可通过脚本绕过限制。它不是安全边界，请与其他控制手段配合使用。

# HISTORY

**rbash** 就是以受限 shell 方式启动的 bash。它为不受信任的用户提供有限的环境。

# INSTALL

```apt: sudo apt install bash```

```dnf: sudo dnf install bash```

```pacman: sudo pacman -S bash```

```zypper: sudo zypper install bash```

```brew: brew install bash```

```nix: nix profile install nixpkgs#bash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [chroot](/man/chroot)(1), [sudo](/man/sudo)(1)
