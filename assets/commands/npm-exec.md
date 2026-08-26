# TAGLINE

运行来自本地或远程 npm 软件包的命令

# TLDR

**运行本地软件包的可执行文件**

```npm exec [command]```

**带参数运行命令**

```npm exec -- [command] [args]```

**运行来自 registry 的软件包**

```npm exec -p [package] -- [command]```

**运行指定版本的软件包**

```npm exec -p [package]@[version] -- [command]```

**在多个软件包可用的环境中运行**

```npm exec -p [pkg1] -p [pkg2] -- [command]```

**在软件包环境中运行 shell 命令字符串**

```npm exec -c '[shell_command]'```

**自动确认远程软件包的安装提示**

```npm exec -y -p [package] -- [command]```

# SYNOPSIS

**npm exec** [_options_] [-- _command_ [_args_...]]

# PARAMETERS

**-p**, **--package** _pkg_
> 要安装的软件包（可多次指定）。

**-c**, **--call** _cmd_
> 在软件包环境中运行的 shell 命令字符串。

**-y**, **--yes**
> 下载远程软件包时跳过确认提示。

**--no**
> 拒绝安装本地尚不存在的软件包。

**-w**, **--workspace** _name_
> 在指定工作区的上下文中运行。

**--workspaces**
> 在所有已配置工作区的上下文中运行。

**--include-workspace-root**
> 使用 --workspaces 时包含工作区根目录。

# DESCRIPTION

**npm exec** 运行来自本地或远程 npm 软件包的命令。它与 **npx** 类似，但直接集成在 npm CLI 中。该命令可以运行本地安装的软件包，也可以临时下载并执行 npm registry 中的软件包。

双横线（**--**）用于分隔 npm exec 的选项与命令及其参数。若不写 **--**，npm 可能把参数当作自己的选项来解析。在不带位置参数也不带 **--call** 的情况下运行时，它会打开一个交互式 shell，并将软件包环境配置到 PATH 中。

未指定 **--package** 时，npm exec 会尝试从第一个位置参数推断要用的可执行文件，并在本地项目或 npm registry 中匹配相应的软件包。

# CAVEATS

与 **npx** 不同，npm exec 在传递参数时要求命令前有 **--**。下载远程软件包时可能会提示确认，除非指定 **-y** 或 **--no**。**--call** 选项会在 shell 中运行命令，因此支持管道和重定向等 shell 语法。

# HISTORY

npm exec 于 **npm 7** 加入，作为 npx 的内置替代品，提供类似的功能，同时与 npm 集成更紧密并支持工作区。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npx](/man/npx)(1), [npm-run-script](/man/npm-run-script)(1), [npm-init](/man/npm-init)(1), [npm-install](/man/npm-install)(1)
