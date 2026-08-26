# TAGLINE

基于 JavaScript 的 Solidity 编译器

# TLDR

**编译合约**

```solcjs [contract.sol]```

**输出二进制**

```solcjs --bin [contract.sol]```

**输出 ABI**

```solcjs --abi [contract.sol]```

**同时输出二进制和 ABI**

```solcjs --bin --abi [contract.sol]```

**自定义输出目录**

```solcjs --bin -o [build] [contract.sol]```

**优化代码**

```solcjs --bin --optimize [contract.sol]```

# SYNOPSIS

**solcjs** [_--bin_] [_--abi_] [_--optimize_] [_-o dir_] _files_

# PARAMETERS

**--bin**
> 输出字节码。

**--abi**
> 输出 ABI JSON。

**--optimize**
> 启用优化器。

**-o** _DIR_
> 输出目录。

**--base-path** _DIR_
> 导入的基础路径。

**--include-path** _DIR_
> 包含路径。

# DESCRIPTION

**solcjs** 是 Solidity 编译器的 JavaScript/WebAssembly 实现，可通过 npm 安装。它将 Solidity 智能合约编译为 EVM 字节码以及 ABI（应用二进制接口）定义，这些是在以太坊及兼容区块链上部署合约并与合约交互所必需的。

编译器生成用于部署的字节码（**--bin**）以及描述合约函数和事件、供客户端交互使用的 ABI JSON（**--abi**）。启用优化器后可减小字节码体积并降低 gas 成本。

solcjs 提供与原生 **solc** 编译器相同的核心编译功能，但运行在 Node.js 环境中，因此很容易集成到基于 JavaScript 的开发工作流以及 Truffle 和 Hardhat 等构建工具中。它比原生编译器略慢，并且可能缺少一些高级功能。

# CAVEATS

比原生 solc 慢。JavaScript 实现。缺少部分功能。

# HISTORY

**solcjs** 是 **solc**（以太坊智能合约 Solidity 编译器）的 JavaScript/WebAssembly 移植版。

# SEE ALSO

[solc](/man/solc)(1), [truffle](/man/truffle)(1), [hardhat](/man/hardhat)(1)
