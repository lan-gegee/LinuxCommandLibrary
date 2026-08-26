# TAGLINE

先运行 npm install 再运行 npm test

# TLDR

**安装依赖并运行测试**

```npm it```

**在干净的 CI 环境中安装并测试**

```npm cit```

**显示 install-test 的帮助**

```npm it --help```

# SYNOPSIS

**npm** **it** [_options_]

**npm** **install-test** [_options_]

# PARAMETERS

**--help**
> 显示帮助信息。

任何 **npm install** 接受的标志都可以传入，并会被转发给安装步骤。

# DESCRIPTION

**npm it** 是一个快捷方式，先运行 **npm install** 再运行 **npm test**。它是 **npm install-test** 的别名，用于快速验证项目能否干净地安装、测试套件能否通过。

相关命令 **npm cit**（**npm clean-install-test** 的别名）先执行 **npm ci**（全新安装）再执行 **npm test**，适合需要从 lockfile 进行可重现安装的 CI 流水线。

# CAVEATS

两个步骤都必须成功；若安装失败则不会运行测试。若测试失败，退出码为非零。在 CI 中请使用 **npm cit** 以获得干净、基于 lockfile 的安装。

# HISTORY

npm it 是组合安装与测试操作的**简写别名**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [npm-test](/man/npm-test)(1)
