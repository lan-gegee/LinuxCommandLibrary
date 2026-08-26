# TAGLINE

在浏览器中打开 Pulumi Web 控制台

# TLDR

**在默认浏览器中打开 Pulumi 控制台**

```pulumi console```

**在控制台中打开指定堆栈**

```pulumi console -s [stack_name]```

**从其他项目目录打开控制台**

```pulumi console -C [path/to/project]```

# SYNOPSIS

**pulumi** **console** [_options_]

# PARAMETERS

**-s**, **--stack** _string_
> 要在控制台中查看的堆栈名称。

**-C**, **--cwd** _string_
> 以 pulumi 在指定目录中启动的方式运行。

**--color** _string_
> 控制彩色输出（always、never、raw、auto）。默认为 auto。

**--non-interactive**
> 为所有命令禁用交互模式。

# DESCRIPTION

**pulumi console** 在默认浏览器中打开 Pulumi Cloud Web 控制台。它提供一个基于 Web 的管理界面，用于查看和管理堆栈、资源、部署历史和活动日志。如果使用 **-s** 指定了堆栈，控制台会直接打开该堆栈的页面。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-stack](/man/pulumi-stack)(1), [pulumi-login](/man/pulumi-login)(1)
