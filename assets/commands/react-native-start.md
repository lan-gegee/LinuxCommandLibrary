# TAGLINE

启动 React Native Metro 打包器服务器

# TLDR

**启动 Metro 打包器**

```react-native start```

**在指定端口启动**

```react-native start --port [8082]```

**启动并重置缓存**

```react-native start --reset-cache```

**以详细输出启动**

```react-native start --verbose```

**绑定到指定主机启动**

```react-native start --host [0.0.0.0]```

# SYNOPSIS

**react-native start** [_options_]

# PARAMETERS

**--port** _port_
> 服务器端口（默认 8081）。

**--reset-cache**
> 清除打包器缓存。

**--verbose**
> 详细输出。

**--host** _host_
> 服务器主机名。

**--https**
> 启用 HTTPS。

**--config** _path_
> Metro 配置文件。

**--experimental-debugger**
> 启用新的 JS 调试器（Hermes 调试器）。

# DESCRIPTION

**react-native start** 启动 Metro JavaScript 打包器，这是一个开发服务器，为在模拟器、仿真器或物理设备上运行的 React Native 应用编译并提供 JavaScript 包。它会监视源文件的变化，并通过热重载将更新推送到已连接的应用，从而无需完整重建即可快速开发。

打包器默认监听 8081 端口，可用 **--port** 自定义。**--reset-cache** 标志会清除打包器的转换缓存，在排查陈旧的模块解析问题或更改配置后很有用。使用 **--host 0.0.0.0** 可让服务器被网络上的其他设备访问，例如同一 Wi-Fi 下的实体手机。

# SEE ALSO

[react-native](/man/react-native)(1), [metro](/man/metro)(1)
