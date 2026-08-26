# TAGLINE

管理 apx 子系统的栈配置

# TLDR

交互式**创建**新的栈配置

```apx stacks new```

交互式**更新**栈配置

```apx stacks update [name]```

**列出**所有可用的栈配置

```apx stacks list```

**查看**特定栈的信息

```apx stacks show [name]```

**删除**指定的栈配置

```apx stacks rm --name [name]```

从文件**导入**栈配置

```apx stacks import --input [path/to/stack.yml]```

将栈配置**导出**到文件

```apx stacks export --name [name] --output [path/to/output_file]```

# SYNOPSIS

**apx stacks** _command_ [_options_]

# DESCRIPTION

**apx stacks** 管理 apx 中的栈配置。栈定义了基础容器镜像与软件包管理器的组合，是子系统的基础。

用户创建的栈配置存储在 **~/.local/share/apx/stacks**。通过导出和导入 YAML 配置文件，可以在不同系统之间共享栈。

# SUBCOMMANDS

**new**
> 交互式创建新的栈配置

**update**
> 修改现有的栈配置

**list**
> 显示所有可用的栈配置

**show**
> 显示特定栈的信息

**rm**
> 删除栈配置

**import**
> 从 YAML 文件导入栈

**export**
> 将栈导出为 YAML 文件

# PARAMETERS

**-n, --name** _string_
> 指定栈名称

**-b, --base** _string_
> 栈的基础容器镜像（供 new 和 update 使用）

**-p, --packages** _string_
> 预装的软件包（供 new 和 update 使用）

**-k, --pkg-manager** _string_
> 要使用的软件包管理器（供 new 和 update 使用）

**-y, --no-prompt** _string_
> 采用默认答案，不进行交互式提示

**-f, --force**
> 删除栈时不要求确认（供 rm 使用）

**-i, --input** _path_
> 要导入的栈配置文件路径

**-o, --output** _path_
> 导出的栈文件路径（默认为当前目录）

# INSTALL

```dnf: sudo dnf install apx```

```aur: yay -S apx```

```nix: nix profile install nixpkgs#apx```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apx](/man/apx)(1), [apx-pkgmanagers](/man/apx-pkgmanagers)(1), [apx-subsystems](/man/apx-subsystems)(1)

# RESOURCES

```[Source code](https://github.com/Vanilla-OS/apx)```

```[Homepage](https://vanillaos.org)```

```[Documentation](https://docs.vanillaos.org/apx/en/working-w-stacks)```

<!-- verified: 2026-06-11 -->
