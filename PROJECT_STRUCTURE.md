# OpenCLAW 项目结构说明

## 目录结构

```
openclaw-emotional-skills/
├── openclaw.py                 # OpenCLAW核心实现
├── example_usage.py           # 示例使用脚本
├── README.md                  # 项目概述
├── SKILLS.md                  # 详细技能说明
├── USAGE.md                   # 使用指南
├── LICENSE                    # 项目许可证
├── requirements.txt           # 依赖包列表
└── PROJECT_STRUCTURE.md       # 本文件 - 项目结构说明
```

## 文件说明

### 核心文件

#### openclaw.py
- **功能**: OpenCLAW的主要实现文件，包含所有核心类和功能
- **主要内容**:
  - `EmotionState`: 情感状态数据类
  - `Memory`: 记忆管理系统
  - `EmotionalProcessor`: 情感处理逻辑
  - `EvolutionEngine`: 自我进化引擎
  - `OpenCLAW`: 主AI代理类，整合所有功能

#### example_usage.py
- **功能**: 展示OpenCLAW各项技能的使用示例
- **主要内容**:
  - 情感技能演示
  - 自我进化演示
  - 复杂场景演示
  - 技能总结

### 文档文件

#### README.md
- **功能**: 项目概述，包含简介、特性、安装指南、使用示例等

#### SKILLS.md
- **功能**: 详细说明OpenCLAW的各项技能和技术实现

#### USAGE.md
- **功能**: 简洁的使用指南，包含快速开始和高级功能

### 配置文件

#### requirements.txt
- **功能**: 列出项目依赖的Python包

#### LICENSE
- **功能**: 项目的许可协议

## 架构设计

### 设计原则
1. **模块化**: 将不同功能拆分为独立的类和模块
2. **可扩展性**: 易于添加新的技能和功能
3. **可维护性**: 清晰的代码结构和充分的注释

### 核心组件关系
```
OpenCLAW (主类)
├── Memory (记忆系统)
├── EmotionalProcessor (情感处理)
│   └── EmotionState (情感状态)
└── EvolutionEngine (进化引擎)
    ├── 行为模式库
    ├── 性能日志
    └── 改进建议系统
```

### 扩展指南
如需扩展新功能：
1. 在现有类中添加方法
2. 或创建新的功能类并将其集成到OpenCLAW主类中
3. 更新文档以反映新功能
4. 在example_usage.py中添加新功能的示例