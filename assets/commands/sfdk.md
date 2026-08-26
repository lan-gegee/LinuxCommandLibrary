# TAGLINE

Sailfish OS 应用开发工具集

# TLDR

**构建软件包**

```sfdk build```

**部署到设备**

```sfdk deploy --device```

**在设备上运行**

```sfdk device exec [command]```

**创建项目**

```sfdk init --template [app] [project-name]```

**列出设备**

```sfdk device list```

**设置目标**

```sfdk config --target=[target-name]```

# SYNOPSIS

**sfdk** _command_ [_options_] [_args_]

# PARAMETERS

**build**
> 构建项目。

**deploy**
> 部署到设备。

**device**
> 设备操作。

**init**
> 创建项目。

**config**
> 配置。

**--device**
> 目标设备。

**--target** _NAME_
> 构建目标。

# DESCRIPTION

**sfdk** 是 Sailfish OS SDK 的命令行界面，提供用于开发、构建和部署 Sailfish OS 应用程序的工具。它负责基于模板生成项目骨架、面向 ARM 和 x86 目标的交叉编译，以及部署到物理设备或模拟器。

该工具集与 Qt/QML 构建系统（qmake、cmake）集成，并管理构建环境，包括目标 SDK 安装和构建依赖。应用程序可以在模拟设备上进行测试，无需物理硬件，从而简化开发周期。

# CAVEATS

需要 Sailfish SDK。与平台相关。需要 Qt/QML 知识。

# HISTORY

**sfdk** 是 Jolla 公司 **Sailfish OS SDK** 的一部分，为移动应用开发提供命令行工具。

# SEE ALSO

[qmake](/man/qmake)(1), [rpm](/man/rpm)(1)
