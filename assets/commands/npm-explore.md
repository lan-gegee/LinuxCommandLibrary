# TAGLINE

在软件包目录中打开一个子 shell

# TLDR

**浏览软件包目录**

```npm explore [package-name]```

**在软件包中运行命令**

```npm explore [package-name] -- [ls]```

**浏览并运行脚本**

```npm explore [package-name] -- npm run build```

# SYNOPSIS

**npm** **explore** _package_ [-- _command_]

# PARAMETERS

_PACKAGE_
> 要进入的已安装软件包（在 **node_modules** 中查找）。

_COMMAND_
> 要在软件包目录中运行的命令。提供该参数时，命令一结束子 shell 便会退出。

**--shell** _PATH_
> 要调用的 shell。默认：**$SHELL**，POSIX 上为 **bash**，Windows 上为 **cmd.exe**。

# DESCRIPTION

**npm explore** 在已安装软件包（通常位于 **node_modules** 下）的目录内启动一个子 shell。它适合用来查看已安装的软件包、操作其中的 git 子模块，或在软件包上下文中运行 **npm run** 脚本等临时命令。

如果在浏览期间修改了该软件包，它**不会**自动重新构建——之后请运行 **npm rebuild** _pkg_ 来重新编译原生组件并重新链接可执行文件。

# CAVEATS

会打开交互式子 shell——输入 **exit** 返回父 shell。对 **node_modules** 下内容的修改会在下一次 **npm install** 时被清除，因此应尽量将修改持久化到上游。建议在命令前加 **--**，以免 npm 把末尾的参数当作自己的标志解析。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-ls](/man/npm-ls)(1), [npm-edit](/man/npm-edit)(1)
