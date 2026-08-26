# TAGLINE

Solidity 智能合约编译器

# TLDR

**编译 Solidity 文件**并输出字节码

```solc --bin [contract.sol]```

**编译并输出 ABI**

```solc --abi [contract.sol]```

在启用优化的情况下**编译**

```solc --optimize --bin [contract.sol]```

**输出到目录**

```solc -o [output_dir] --bin --abi [contract.sol]```

使用 Standard JSON **输入/输出编译**

```solc --standard-json < [input.json]```

**显示函数的预估 gas**

```solc --gas [contract.sol]```

**输出抽象语法树**

```solc --ast-compact-json [contract.sol]```

**重映射导入路径**

```solc [prefix]=[path] [contract.sol]```

# SYNOPSIS

**solc** [_options_] [_input-files_]

# PARAMETERS

**--bin**
> 输出合约的二进制（字节码）。

**--abi**
> 输出 ABI（应用二进制接口）规范。

**--optimize**
> 启用字节码优化器。

**--optimize-runs** _n_
> 按 n 次合约调用进行优化（默认：200）。

**-o**, **--output-dir** _path_
> 编译产物的输出目录。

**--standard-json**
> 使用 Standard JSON 输入/输出模式。未给出文件时从标准输入读取。

**--ast-compact-json**
> 以紧凑 JSON 格式输出 AST。

**--asm**
> 输出 EVM 汇编。

**--gas**
> 输出各函数的预估 gas 消耗。

**--metadata**
> 输出合约元数据。

**--userdoc**
> 输出用户文档（NatSpec）。

**--devdoc**
> 输出开发者文档（NatSpec）。

**--combined-json** _keys_
> 输出带指定键的组合 JSON（abi、bin、metadata 等）。

**--base-path** _path_
> 导入的基础路径。

**--include-path** _path_
> 导入的附加路径。

**--evm-version** _version_
> 目标 EVM 版本（homestead、tangerineWhistle、spuriousDragon、byzantium、constantinople、petersburg、istanbul、berlin、london、paris、shanghai）。

**--via-ir**
> 启用经由 Yul IR 的编译。

**--lsp**
> 作为语言服务器协议（LSP）后端运行。

**--version**
> 显示版本信息。

# DESCRIPTION

**solc** 是 Solidity 的命令行编译器。Solidity 是以太坊智能合约的主要编程语言。它将 Solidity 源代码编译为可部署到以太坊及兼容区块链的 EVM（以太坊虚拟机）字节码。

编译器可以产生多种输出，包括字节码、ABI 定义、汇编、抽象语法树、gas 估算和文档。优化器可以减小字节码体积并降低 gas 成本。Standard JSON 模式提供结构化的输入/输出，便于与构建工具集成。

导入路径可以使用 **context:prefix=path** 语法重映射，从而支持灵活的项目结构。编译器还支持 LSP 模式以便与 IDE 集成。

# CAVEATS

不同 Solidity 版本的语法可能不兼容；请使用 **solc-select** 管理多个版本。优化器有时可能引入细微问题，应当充分测试。gas 估算只是近似值，可能与实际执行成本不同。EVM 版本必须与目标区块链的能力匹配。

# HISTORY

**Solidity** 由 Gavin Wood 于 **2014 年**提出，由以太坊基金会的 Solidity 团队开发。首个版本于 **2015 年**随以太坊一同发布。语言和编译器已发生显著演进，主要版本引入了 ABIEncoderV2、自定义错误和用户自定义值类型等特性。开发工作持续活跃进行，不断提升安全性、效率和开发者体验。

# INSTALL

```nix: nix profile install nixpkgs#solc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[forge](/man/forge)(1), [hardhat](/man/hardhat)(1)
