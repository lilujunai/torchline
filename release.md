
# Release

## v0.1

### 2019.12.12 更新信息
- 基本框架搭建完成
- 可正常运行cifar10_demo


### 2019.12.13 更新信息
- 实现setup安装
- 完善包之间的引用关系
- 完善各模块之间的关系
  - data
    - build_data
    - build_sampler
    - build_transforms
    - build_label_transforms
  - engine
    - build_module_template
  - losses
    - build_loss_fn
  - models
    - build_model

### todo list

- [ ] 弄清楚logging机制
- [ ] save和load模型，优化器参数
- [ ] skin数据集读取测试
- [ ] 构建skin project
- [ ] 能否预测单张图片？
- [ ] 构建一个简单地API接口
- [ ] 进一步完善包导入
- [ ] 完善使用文档
- [ ] 设置训练epoch数量