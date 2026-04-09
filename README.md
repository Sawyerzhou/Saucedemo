# 🧪 SauceDemo Automation Project

> 一个针对 [SauceDemo](https://www.saucedemo.com/) 示例网站的自动化测试/演示项目。该项目旨在展示 UI 自动化测试框架的最佳实践，涵盖登录、商品筛选、购物车及下单全流程。

---

## 📖 目录

- [简介](#-简介)
- [技术栈](#-技术栈)
- [环境要求](#-环境要求)
- [安装与运行](#-安装与运行)
- [项目结构](#-项目结构)
- [测试用例覆盖](#-测试用例覆盖)
- [报告](#-报告)
- [贡献指南](#-贡献指南)
- [许可证](#-许可证)

---

## 🚀 简介

**SauceDemo** 是一个由 [Sauce Labs](https://saucelabs.com/) 提供的开源演示站点，常用于验证自动化测试工具的功能。本项目实现了对该站点的自动化端到端测试，特点如下：

- ✅ **模块化设计**：采用 Page Object Model (POM) 设计模式，提高代码可维护性。
- ✅ **多浏览器支持**：可配置运行于 Chrome、Firefox 或 Edge。
- ✅ **详细日志与报告**：生成可视化的测试执行报告。
- ✅ **CI/CD 就绪**：易于集成 GitHub Actions 或 Jenkins。

---

## 🛠 技术栈

| 类别         | 工具/库                              |
|--------------|--------------------------------------|
| 核心语言     | Python |
| 自动化框架   | Selenium WebDriver |
| 测试运行器   | pytest |
| 报告         | Allure |
| 依赖管理     | requirements.txt |

---

## ⚙️ 环境要求

- **Python** 3.9+ 
- 浏览器驱动（ChromeDriver, GeckoDriver 等）需与本地浏览器版本匹配。
- *(可选)* Docker（用于容器化执行）

---

## 📦 安装与运行

### 1. 克隆仓库
git clone https://github.com/Sawyerzhou/Saucedemo.git
cd Saucedemo

### 2. 安装依赖
pip install -r requirements.txt

或使用 WebDriverManager 自动管理驱动版本（本项目默认已集成）。

### 3. 配置浏览器驱动
确保 chromedriver 已添加至系统 PATH，或在项目配置文件中指定路径。

或使用 WebDriverManager 自动管理驱动版本（本项目默认已集成）。

### 4. 运行测试
运行所有测试：
pytest

运行指定标签的测试（如冒烟测试）：
pytest -m smoke

📁 项目结构
text
Saucedemo/
├── config/ # 配置文件（环境、浏览器等）
├── data/ # 测试数据（YAML）
├── pages/ # Page Object 层
├── testcases/ # 测试用例
├── utils/ # 工具函数（读取YAML、日志等）
├── conftest.py # pytest 全局 fixture
├── pytest.ini # pytest 配置
└── requirements.txt
└── README.md

🧪 测试用例覆盖
模块	测试场景
登录	标准用户/锁定用户/问题用户登录校验
商品列表	按名称(A-Z)/价格排序，商品详情页跳转
购物车	添加/移除商品，继续购物，数量变更
结账流程	填写收货信息，完成订单，返回首页
菜单导航	关于、重置应用状态、登出
具体用例可查阅 testcases 目录下的测试类文件。

📊 报告
测试执行后，报告会自动生成在 reports/ 目录下
Allure 报告：运行 allure serve allure-results 查看美观的 HTML 报告。
