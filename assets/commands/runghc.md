# TAGLINE

无需编译即可运行 Haskell 程序

# TLDR

**运行 Haskell 脚本**

```runghc [script.hs]```

**带参数运行**

```runghc [script.hs] [arg1] [arg2]```

**指定 GHC 版本**

```runghc-[8.10] [script.hs]```

**附带 GHC 选项**

```runghc -- -O2 [script.hs]```

# SYNOPSIS

**runghc** [_options_] [_ghc-options_] _file_ [_args_]

# PARAMETERS

**--**
> 用于分隔 GHC 选项的分隔符。

**-f** _file_
> 使用不同的 GHC。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**runghc** 直接运行 Haskell 源文件而无需单独的编译步骤，非常适合脚本编写和快速原型开发。它在后台调用 GHC（Glasgow Haskell Compiler）把程序编译到临时位置并立即执行，为 Haskell 代码提供了类似脚本的体验。

该工具支持 shebang 行（#!/usr/bin/env runghc），使 Haskell 文件可以作为可执行脚本使用。文件名之后的命令行参数会传递给 Haskell 程序，GHC 选项可以在 **--** 分隔符之前指定。别名 **runhaskell** 同样可用。

# EXAMPLES

```bash
# Run script
runghc hello.hs

# With arguments
runghc calculator.hs 2 + 3

# Pass GHC options
runghc -- -Wall script.hs

# Shebang usage
#!/usr/bin/env runghc
```

# SCRIPT EXAMPLE

```haskell
#!/usr/bin/env runghc
import System.Environment

main = do
    args <- getArgs
    putStrLn $ "Hello, " ++ head args
```

# ALTERNATIVES

```bash
runhaskell  # Synonym
ghci        # Interactive (load with :load)
ghc -e      # One-liner
```

# CAVEATS

比编译后的代码慢。每次运行都要重新编译。若追求性能，请使用 ghc 编译。

# HISTORY

runghc 是 **GHC**（Glasgow Haskell Compiler）的一部分，GHC 是由 GHC 团队开发的主要 Haskell 编译器。

# INSTALL

```apt: sudo apt install ghc```

```dnf: sudo dnf install ghc```

```pacman: sudo pacman -S ghc```

```apk: sudo apk add ghc```

```zypper: sudo zypper install ghc```

```brew: brew install ghc```

```nix: nix profile install nixpkgs#ghc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [ghci](/man/ghci)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1)
