# TAGLINE

从状态包重放 aptitude 状态

# TLDR

使用状态包**运行** aptitude

```aptitude-run-state-bundle [bundle.tar.bz2]```

带**指定的 aptitude 参数**运行

```aptitude-run-state-bundle [bundle.tar.bz2] -- search [pattern]```

# SYNOPSIS

**aptitude-run-state-bundle** _bundle_ [_-- aptitude-args_]

# DESCRIPTION

**aptitude-run-state-bundle** 使用先前创建的状态包中的状态运行 aptitude。这可以重现精确的软件包状态，用于调试或测试依赖解析。

该工具会解包状态包，配置 aptitude 使用解包后的状态，并带上提供的参数运行 aptitude。

# PARAMETERS

**bundle**
> 状态包文件（.tar.bz2）

**-- args**
> 传递给 aptitude 的参数

# CAVEATS

用于调试目的。状态包中的状态可能与当前软件仓库状态不一致。主要对 aptitude 开发者有用。

# HISTORY

**aptitude-run-state-bundle** 与 aptitude-create-state-bundle 配套，让开发者能够重现报告的问题。

# INSTALL

```apt: sudo apt install aptitude```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aptitude](/man/aptitude)(8), [aptitude-create-state-bundle](/man/aptitude-create-state-bundle)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/apt-team/aptitude)```

<!-- verified: 2026-06-11 -->
