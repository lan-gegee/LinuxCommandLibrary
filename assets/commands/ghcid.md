# TAGLINE

用于快速 Haskell 开发的自动重载 GHCi 守护进程

# TLDR

在当前项目中**启动**，自动检测 ghci 或 cabal repl

```ghcid```

**使用**指定的 repl 命令

```ghcid --command="[cabal repl]"```

每次成功加载后**运行**一个表达式

```ghcid --test=[main]```

即使存在警告也**运行**测试

```ghcid --test=[:main] --warnings```

**构建**特定组件

```ghcid --target=[lib:foo]```

非 Haskell 文件变化时**重载**

```ghcid --reload=[templates] --reload=[config.yaml]```

每次重载时**清屏**

```ghcid --clear```

代码编译干净时**运行** hlint

```ghcid --lint```

# SYNOPSIS

**ghcid** [_options_] [_module_ ...]

# PARAMETERS

**-c**, **--command**=_COMMAND_
> 要运行的命令。默认为 **ghci**；检测到项目时则为 **cabal repl** / **stack ghci**。

**--target**=_TARGET_
> 要构建的组件，例如 Cabal 的 **lib:foo** 或 Stack 的 **foo:lib**。可重复使用。

**-T**, **--test**=_EXPR_
> 每次成功加载后要执行的 GHCi 表达式。

**-r**, **--run**[=_EXPR_]
> 与 **--test** 类似，但默认为 **main**。

**--test-message**=_MESSAGE_
> 运行测试前显示的消息。默认为 **Running test...**。

**-W**, **--warnings**
> 即使代码产生了警告，也允许运行测试。

**--lint**[=_COMMAND_]
> 没有错误时运行 linter。默认为 **hlint**。

**--setup**=_COMMAND_
> 启动时通过标准输入传给 ghci 的命令，通常是某个 **:set** 设置。可重复使用。

**--reload**=_PATH_
> 该文件或目录发生变化时也触发重载。默认无。

**--restart**=_PATH_
> 该路径发生变化时重启整个命令。默认监控 **.ghci** 和任何 **.cabal** 文件，除非正在使用自定义命令或 stack。

**-C**, **--directory**=_DIR_
> 设置当前目录。默认为 **.**。

**-o**, **--outputfile**=_FILE_
> 将完整输出写入文件，采用编辑器可解析的格式。

**--project**=_NAME_
> 标题中显示的项目名称。默认为当前目录。

**--clear**
> 重载时清除屏幕。

**-S**, **--no-status**
> 不显示状态消息。

**--reverse-errors**
> 反转输出顺序。与 **--no-height-limit** 搭配效果最好。

**--no-height-limit**
> 取消高度限制，打印所有消息。

**--height**=_N_
> 使用的行数。默认为控制台高度。

**-w**, **--width**=_N_
> 使用的列数。默认为控制台宽度。

**-n**, **--max-messages**=_N_
> 打印消息的数量上限。

**--colour**[=_always/never/auto_], **--color**
> 为输出着色。默认为 **auto**。

**--no-title**
> 不更新 shell 标题或图标。

**-t**, **--topmost**
> 让窗口保持置顶。仅限 Windows。

**--poll**[=_SECONDS_]
> 每 N 秒轮询一次变更，而不是使用文件系统通知。默认为 **0.1**。

**--allow-eval**
> 执行写在源码注释里的 REPL 命令。

**--ignore-loaded**
> 未加载任何文件时也继续运行。需要配合 **--reload**。

**--no-cabal-repl-rtsopts**
> 禁用自动选择的 **cabal repl** 默认附加的 **+RTS -N -RTS**。

**--server**
> 启用本地 ghcid 套接字服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ghcid** 就是"作为守护进程的 GHCi"：它会启动一个 GHCi 会话，监视你的源文件，一旦有变化就重新加载，并把错误和警告格式化得适合控制台显示。作者将它描述为"GHC 再加上一点点 IDE"。

它的价值在于反馈回路的速度。由于 GHCi 常驻内存，重载只重新编译改动的部分，因此保存后通常不到一秒就能看到错误。输出会被刻意截断到终端高度：构建无误时显示 **All good**，出问题时第一条错误出现在顶部——恰好是你正在看的位置。

不带参数时，**ghcid** 会为项目选择一个合理的 repl 命令：检测到 **cabal repl** 或 **stack ghci** 就优先使用，否则退回普通的 **ghci**。**--test** 能把它变成持续测试运行器——每次成功加载后就求值一个表达式；再配合 **--warnings**，无需离开编辑器即可实现紧凑的红/绿循环。

这个工具刻意保持专一：它不与编辑器集成，不直接向你暴露 GHCi，不依赖 GHC API，也不运行 Web 服务器。**--outputfile** 的存在正是为了让编辑器改为消费它的结果。

# CAVEATS

**ghcid** 的可靠性取决于底层 repl。如果你手动运行 **cabal repl** 或 **ghci** 都无法加载项目，**ghcid** 也解决不了；请先直接测试该命令，然后用 **--command** 传入一条确实可用的命令。

重载只能感知 GHCi 自己能看到的改动。对 **.cabal** 文件、CPP include 或生成代码的修改往往需要完整重启，这正是 **--restart** 的用途。非 Haskell 资源则需要显式的 **--restart** 或 **--reload**。

在网络挂载、容器以及部分虚拟机中，文件系统通知可能不可靠；如果保存后似乎没有被发现，请改用 **--poll**。

**--test** 在同一个 GHCi 会话内运行，因此会无限循环或调用 **exitWith** 的表达式会挂起或杀死守护进程。

**--allow-eval** 会执行注释中发现的代码，因此对你没有读过的代码请不要启用。

# HISTORY

**ghcid** 由 **Neil Mitchell** 编写，**JP Moresmau** 做出了重要贡献，约于 **2014 年**发布。凭借快速且独立于编辑器的反馈，它成为许多 Haskell 开发环境的标准组成部分，并通过 **Hackage** 和 **Stackage** 分发。

# INSTALL

```dnf: sudo dnf install ghcid```

```brew: brew install ghcid```

```nix: nix profile install nixpkgs#ghcid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghci](/man/ghci)(1), [ghc](/man/ghc)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1), [hlint](/man/hlint)(1)

# RESOURCES

```[Source code](https://github.com/ndmitchell/ghcid)```

```[Documentation](https://hackage.haskell.org/package/ghcid)```

<!-- verified: 2026-07-16 -->
