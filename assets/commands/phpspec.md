# TAGLINE

用于设计和测试 PHP 代码的 SpecBDD 框架

# TLDR

**运行项目中所有规范**

```phpspec run```

**为某个类生成新规范**

```phpspec describe "[App\\Calculator]"```

**运行单个 spec 文件**

```phpspec run [spec/App/CalculatorSpec.php]```

**使用指定的输出格式器**（pretty、progress、junit、dot、tap、html）

```phpspec run --format [pretty]```

**不进行交互提示**，自动生成缺失的类/方法

```phpspec run --no-interaction```

**在首次失败时停止**

```phpspec run --stop-on-failure```

**显示完整回溯信息**，便于详细调试

```phpspec run -vvv```

# SYNOPSIS

**phpspec** _command_ [_arguments_] [_options_]

# COMMANDS

**run** [_spec_]
> 运行所有 spec（或单个 spec 文件/类），并以交互方式提供缺失代码的生成选项。

**describe** _CLASS_
> 为给定的完全限定类名创建新的 spec 文件。

**help** [_command_]
> 显示特定命令的帮助。

**list**
> 列出所有可用命令。

# PARAMETERS

**-c**, **--config** _FILE_
> 使用指定的配置文件（默认：phpspec.yml 或 phpspec.yml.dist）。

**-f**, **--format** _NAME_
> 输出格式器：progress（默认）、pretty、junit、dot、tap、html。

**--stop-on-failure**
> 一旦某个 spec 失败就立即中止运行。

**--fake**
> 使生成的哑方法返回逼真的伪造数据。

**-n**, **--no-interaction**
> 不询问任何交互式问题；采用默认值。

**-v** / **-vv** / **-vvv**
> 提高详细程度。**-vvv** 会打印异常堆栈跟踪。

**--ansi** / **--no-ansi**
> 强制启用或禁用 ANSI 彩色输出。

**-q**, **--quiet**
> 抑制所有输出。

**-V**, **--version**
> 显示 phpspec 版本。

# DESCRIPTION

**phpspec** 是一个面向 PHP 的 SpecBDD（规格化行为驱动开发）工具。与传统的单元测试运行器验证现有实现不同，它驱动对象的设计：你先编写描述类应如何表现的 spec，然后运行 phpspec，它会主动为你搭建缺失的类、方法和 return 语句的骨架代码。

Spec 是继承自 **PhpSpec\\ObjectBehavior** 的普通 PHP 类。每个 `it_*` / `its_*` 方法就是一个示例。协作者以类型提示参数的形式描述，phpspec 会自动为其提供基于 prophecy 的测试替身。

配置位于项目根目录的 `phpspec.yml`（或 `phpspec.yml.dist`），控制测试套件、引导文件、格式器以及匹配器/扩展。PhpSpec 的定位刻意比 PHPUnit 更窄——它专注于隔离的、设计优先的对象 spec，天然适合与 Behat 这类更高层级的验收工具搭配使用。

# CONFIGURATION

**phpspec.yml**
> 项目配置：声明套件、命名空间、源代码目录、格式器和扩展。

# CAVEATS

PhpSpec 不是 PHPUnit 的直接替代品——它无法测试静态方法、final 类（除非安装扩展），也无法执行框架级集成测试。生成的代码刻意保持最简；你需要在骨架代码之后填入真正的实现。

# HISTORY

PhpSpec 由 **Marcello Duarte** 于 2007 年启动，并在 **Konstantin Kudryashov** 和 Behat 社区的帮助下于 2014 年重写为 PhpSpec 2。它在 GitHub 上以 `phpspec` 组织的名义维护，可通过 Composer 安装。

# SEE ALSO

[phpunit](/man/phpunit)(1), [behat](/man/behat)(1), [composer](/man/composer)(1)
