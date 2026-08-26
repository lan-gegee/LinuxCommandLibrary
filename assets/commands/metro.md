# TAGLINE

React Native 所用的 JavaScript 打包器

# TLDR

**启动 Metro 打包器**

```npx react-native start```

**重置缓存后启动**

```npx react-native start --reset-cache```

**在指定端口启动**

```npx react-native start --port [8082]```

**为生产环境打包**

```npx react-native bundle --platform [android] --dev false --entry-file [index.js] --bundle-output [bundle.js]```

**启用详细日志**

```npx react-native start --verbose```

# SYNOPSIS

**metro** [_options_]

# PARAMETERS

**--port** _port_
> 服务器端口。

**--reset-cache**
> 清空打包器缓存。

**--verbose**
> 详细输出。

**--config** _file_
> 配置文件路径。

**--entry-file** _file_
> 入口文件。

**--bundle-output** _file_
> 输出的 bundle 文件。

**--platform** _platform_
> 目标平台（ios、android）。

**--dev** _boolean_
> bundle 的开发模式标志（默认：true）。

**--host** _host_
> 监听的主机（默认：localhost）。

**--max-workers** _N_
> 指定用于并行处理的最大工作进程数。

# DESCRIPTION

**Metro** 是 React Native 所使用的 JavaScript 打包器。它编译并打包 JavaScript 代码和资源，处理模块解析，并在开发期间提供热重载。

Metro 针对 React Native 的需求进行了优化，具备快速的增量构建能力。

# CONFIGURATION

```javascript
// metro.config.js
module.exports = {
  resolver: {
    sourceExts: ['js', 'jsx', 'ts', 'tsx'],
  },
  transformer: {
    getTransformOptions: async () => ({
      transform: { experimentalImportSupport: false },
    }),
  },
};
```

# CAVEATS

React Native 专用。缓存问题可能需要重置。多个实例会产生端口冲突。

# HISTORY

Metro 由 **Facebook**（Meta）开发，是 React Native 的打包器，针对移动开发工作流进行了优化。

# SEE ALSO

[react-native](/man/react-native)(1), [webpack](/man/webpack)(1), [babel](/man/babel)(1), [expo](/man/expo)(1)
