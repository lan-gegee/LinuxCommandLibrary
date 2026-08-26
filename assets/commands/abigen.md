# TAGLINE

以太坊智能合约 Go 绑定生成器

# TLDR

从 Solidity ABI **生成** Go 绑定

```abigen --abi [contract.abi] --pkg [packagename] --out [contract.go]```

从**编译后的合约**生成绑定

```abigen --bin [contract.bin] --abi [contract.abi] --pkg [packagename] --out [contract.go]```

直接从 **Solidity 源码**生成

```abigen --sol [contract.sol] --pkg [packagename] --out [contract.go]```

指定自定义的**结构体类型**名称

```abigen --abi [contract.abi] --pkg [packagename] --type [MyContract] --out [contract.go]```

# SYNOPSIS

**abigen** [_--abi file_] [_--bin file_] [_--sol file_] [_--pkg name_] [_--out file_] [_options_]

# DESCRIPTION

**abigen** 是一个以太坊工具，用于生成与智能合约交互所需的 Go 语言绑定。它接收合约的 ABI（应用二进制接口），并可选择接收字节码，从而生成类型安全的 Go 代码，用于部署合约和调用合约方法。

生成的代码会处理 ABI 编码/解码、交易创建和事件过滤，使 Go 应用程序与以太坊合约的交互变得简单直接。这免去了手动操作 ABI 的麻烦，并提供编译期类型检查。

# PARAMETERS

**--abi** _file_
> 合约 ABI JSON 文件的路径

**--bin** _file_
> 合约字节码的路径（生成部署代码时必需）

**--sol** _file_
> Solidity 源文件的路径（需要 solc 编译器）

**--pkg** _name_
> 生成的 Go 代码所用的软件包名称

**--out** _file_
> 生成代码的输出文件路径

**--type** _name_
> 合约绑定的结构体名称（默认为合约名）

**--lang** _language_
> 生成绑定的目标语言（默认：go）。

**--solc** _path_
> 使用 --sol 时 Solidity 编译器的路径。

**--combined-json** _file_
> solc 编译器 combined-json 输出文件的路径。

**--alias** _aliases_
> 以逗号分隔的标识符别名列表（原始名=替换名）。

# CAVEATS

使用 **--sol** 时必须安装 Solidity 编译器（solc）且可被访问。ABI 变更后需要重新生成绑定。复杂的 Solidity 类型可能产生冗长的 Go 代码。部署合约时请确保 ABI 与字节码相匹配。

# HISTORY

**abigen** 由以太坊基金会开发，是 **go-ethereum**（geth）的一部分，最早出现于 **2015** 年前后。它的诞生是为了给智能合约提供符合 Go 语言习惯的绑定，支撑起不断壮大的基于 Go 的以太坊工具与应用生态。

# INSTALL

```apk: sudo apk add geth-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[solc](/man/solc)(1), [geth](/man/geth)(1), [cast](/man/cast)(1)
