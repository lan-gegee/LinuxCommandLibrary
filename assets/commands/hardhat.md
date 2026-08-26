# TAGLINE

以太坊开发环境

# TLDR

**创建新项目**

```npx hardhat init```

**编译合约**

```npx hardhat compile```

**运行测试**

```npx hardhat test```

**启动本地节点**

```npx hardhat node```

**运行部署脚本**

```npx hardhat run [scripts/deploy.js]```

**部署到网络**

```npx hardhat run [scripts/deploy.js] --network [sepolia]```

**打开控制台**

```npx hardhat console```

# SYNOPSIS

**npx hardhat** [_task_] [_options_]

# PARAMETERS

**compile**
> 编译 Solidity 合约。

**test**
> 运行测试套件。

**node**
> 启动本地以太坊节点。

**run** _script_
> 运行 JavaScript 脚本。

**console**
> 打开交互式控制台。

**clean**
> 清除缓存和构建产物。

**--network** _name_
> 目标网络。

**--config** _file_
> Hardhat 配置文件的路径。

**--verbose**
> 启用 Hardhat 详细日志。

**--show-stack-traces**
> 显示完整的堆栈跟踪。

**--max-memory** _size_
> Hardhat 可使用的最大内存量。

**--version**
> 显示 Hardhat 版本。

**--help**
> 显示帮助消息；若提供了任务名，则显示该任务的帮助。

# DESCRIPTION

**Hardhat** 是一个以太坊开发环境。它提供本地区块链、调试工具和插件生态，用于编译、测试和部署智能合约。

Hardhat 具备用于 Solidity 调试的 console.log、网络分叉以及 TypeScript 支持。它是专业以太坊开发中最流行的选择。

# CONFIGURATION

```javascript
// hardhat.config.js
module.exports = {
  solidity: "0.8.19",
  networks: {
    sepolia: {
      url: process.env.RPC_URL,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
```

# CAVEATS

需要 Node.js。网络配置需要 RPC URL。私钥应通过环境变量提供。Gas 估算结果可能与主网不同。

# HISTORY

Hardhat 由 **Nomic Foundation**（前身为 Nomic Labs）创建，是 Buidler 的继任者。它已成为领先的以太坊开发框架，以开发者体验和调试能力著称。

# INSTALL

```aur: yay -S hardhat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[truffle](/man/truffle)(1), [ganache](/man/ganache)(1), [forge](/man/forge)(1), [npx](/man/npx)(1)
