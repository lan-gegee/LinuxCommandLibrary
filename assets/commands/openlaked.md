# TAGLINE

面向 LLM 推理和 GPU 工作负载的 OpenLake 存储守护进程

# TLDR

使用 **config** 文件启动存储服务

```openlaked --config [path/to/config.toml]```

从源码**构建**后启动

```./target/release/openlaked --config crates/openlake_server/configs/storage-tcp-local.toml```

安装 **vLLM 连接器**辅助软件包

```pip install openlake-vllm```

```openlaked```

# SYNOPSIS

**openlaked** [_--config_ _path_] [_options_]

# PARAMETERS

**--config** _path_
> OpenLake 服务器配置的路径（TCP 本地存储、RDMA KV 等）

# DESCRIPTION

**openlaked** 是 OpenLake 的服务器二进制程序：一个面向 GPU 中心型工作负载的高性能存储引擎，包括用于 LLM 推理的 KV 缓存卸载、检查点存储和 S3 兼容对象存储。它以 Rust 实现，并针对 Linux 进行了优化（`io_uring`、可选的 RDMA/GPUDirect 路径）。

典型用法：在 GPU 主机上运行 `openlaked`，然后让 vLLM（通过 `openlake-vllm` / OpenLakeConnector）指向节点列表，从而可以从主机内存/磁盘复用长上下文前缀。在对象存储模式下，它对外提供 S3 兼容端点，供 AWS CLI 等工具使用。

# CAVEATS

生产级 RDMA 和 GPUDirect 功能面向 Linux GPU 集群；macOS 仅用于开发。单节点默认配置使用你必须自行创建的本地数据目录。文档中的 S3 演示凭据仅用于本地测试——在任何共享部署中请务必修改。

# HISTORY

**OpenLake** 是一个采用 Apache-2.0 许可证的 AI 基础设施存储项目（KV 池 + 对象存储）。

# SEE ALSO

[vllm](/man/vllm)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/openlake-project/openlake)```

```[Homepage](https://theopenlake.com)```

```[Documentation](https://github.com/openlake-project/openlake/tree/main/docs)```

<!-- verified: 2026-07-28 -->
