# TAGLINE

运行 Zapier 集成测试

# TLDR

**运行所有测试**

```zapier test```

**运行匹配某模式的测试**

```zapier test --grep "[pattern]"```

**使用自定义超时运行**

```zapier test --timeout [5000]```

**带环境变量运行**

```CLIENT_ID=[1234] CLIENT_SECRET=[abcd] zapier test```

# SYNOPSIS

**zapier** **test** [_options_]

# PARAMETERS

**--grep** _pattern_
> 只运行匹配给定模式的测试。

**--timeout** _ms_
> 测试超时时间（毫秒）。

# DESCRIPTION

**zapier test** 使用 Mocha 测试运行器执行 test 目录中定义的集成测试。与直接运行 `npm test` 相比，它会为 Zapier 测试环境设置额外的变量。在部署集成之前可用它验证触发器、操作和身份认证。

# SEE ALSO

[zapier](/man/zapier)(1), [zapier-validate](/man/zapier-validate)(1)
