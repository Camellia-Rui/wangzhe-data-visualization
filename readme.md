# 王者荣耀 · 数据可视化大屏

王者荣耀数据可视化项目，包含三个核心模块：英雄羁绊图谱、英雄皮肤关系网络、英雄数据关系网络图。

## 项目概览

| 模块 | 说明 | 技术栈 | 数据规模 |
|------|------|--------|----------|
| **英雄羁绊图谱** | 力导向图展示英雄间羁绊关系 | ECharts 5.5.0 | 126英雄 × 272羁绊 |
| **英雄皮肤关系网络** | 英雄-品质二部图 + 属性雷达图 | D3.js v7 | 全英雄皮肤数据 |
| **英雄数据关系网络图** | 基于数据特征的力导向聚类图 | ECharts 5.4.3 | 128英雄 × 数据相似度 |

## 截图演示  

| 页面 | 链接 |
|------|------|
| 总入口 | [wangzhe-data-visualization](c:\Users\Lenovo\Desktop\总入口.png) |
| 英雄羁绊 | [hero-bond](c:\Users\Lenovo\Desktop\英雄羁绊.png) |
| 英雄皮肤 | [hero-skin](c:\Users\Lenovo\Desktop\英雄皮肤.png) |
| 英雄数据关系 | [hero-battle](c:\Users\Lenovo\Desktop\英雄数据.png) |

## 项目结构
wangzhe-data-visualization/
├── index.html # 总入口（三模块导航）
├── README.md # 项目说明
├── .gitignore # Git忽略文件
│
├── hero-bond/ # 1. 英雄羁绊模块
│ ├── index.html # 力导向图主页面
│ ├── data.json # 126英雄 × 312 羁绊数据
│ ├── 峡谷.png # 背景图片
│ ├── 王者世界.png # 背景图片
│ ├── 稷下学宫.png # 背景图片
│ └── images/ # 126个英雄头像（.bmp）
│
├── hero-skin/ # 2. 英雄皮肤关系网络
│ ├── index.html # 二部图 + 雷达图
│ ├── skin_data.json # 皮肤数据
│ ├── data.json # 英雄属性雷达图数据
│ └── Images/ # 英雄头像及品质图标
│
└── hero-battle/ # 3. 英雄数据关系网络图
│ ├── index.html # 力导向聚类图
│ ├── 底图.jpg # 背景图片    
│ ├── images/ # 英雄头像（.bmp）
│ └── hero_similarity_data.json # 128英雄数据
└── 

## 模块功能

### 1. 英雄羁绊图谱

基于 ECharts 力导向图，展示英雄间的羁绊关系网络。

- **圆形头像**：SVG clipPath 实现真正的圆形头像 + 金色边框
- **6种关系筛选**：情侣、亲情、阵营、挚友、敌对、其他
- **双向关系描述**：点击连线查看 A→B 和 B→A 的不同描述
- **3种背景切换**：峡谷、王者世界、稷下学宫
- **英雄搜索**：输入英雄名，自动定位并高亮
- **拖拽/缩放**：支持节点拖拽和画布缩放

### 2. 英雄皮肤关系网络

基于 D3.js 的二部图，展示英雄与皮肤品质的关系。

- **英雄-品质二部图**：节点大小反映皮肤数量
- **英雄属性雷达图**：生存能力、攻击伤害、技能效果、上手难度、生命值
- **悬停交互**：查看皮肤品质分布详情
- **圆形头像**：英雄头像 + 品质图标展示
- **力导向布局**：支持拖拽和缩放

### 3. 英雄数据关系网络图

基于128位英雄的胜率（元流之子包括元坦，元法，元射）、登场率、KDA数据，通过欧氏距离计算相似度。

- **职业筛选**：按坦克/战士/刺客/法师/射手/辅助分类查看
- **阈值调节**：动态调整相似度阈值（0.85-0.98），控制连线密度
- **英雄搜索**：回车搜索，高亮显示目标英雄及其关联节点
- **悬停详情**：鼠标悬停显示英雄详细信息
- **头像展示**：128位英雄圆形头像，边框颜色反映胜率等级
- **数据驱动**：完全基于真实数据计算相似关系


## 技术栈

| 模块 | 可视化库 | 核心语言 |
|------|----------|----------|
| 英雄羁绊 | ECharts 5.5.0 | JavaScript (ES6) |
| 英雄皮肤 | D3.js v7 | JavaScript (ES6) |
| 英雄数据关系 | ECharts 5.4.3 | JavaScript (ES6) |
| 样式 | CSS3 | 渐变、毛玻璃效果、响应式 |


## 数据格式

### 英雄羁绊数据（hero-bond/data.json）

{
  "heroes": {
    "英雄名": { "role": "定位", "relations": ["关系英雄1", "关系英雄2"] }
  },
  "links": [
    { 
      "source": "英雄A", "target": "英雄B", "type": "couple",
      "description": "A→B的关系描述",
      "reverseDescription": "B→A的关系描述" 
    }
  ]
}

### 皮肤数据（hero-skin/skin_data.json）

{
  "hero": "英雄名",
  "totalSkins": 10,
  "limited": 3,
  "skinQuality": { "史诗": 2, "传说": 1 }
}

### 数据关系数据（hero-battle/hero_similarity_data.json）
{
  "nodes": [
    { "name": "英雄名", "winRate": 52.3, "pickRate": 15.6, "kda": 3.2, "class": "射手" }
  ],
  "links": [
    { "source": "英雄A", "target": "英雄B", "similarity": 0.95 }
  ]
}

### 本地运行
1. 克隆仓库
git clone https://github.com/Camellia-Rui/wangzhe-data-visualization.git
cd wangzhe-data-visualization

2. 启动本地服务器（避免跨域问题）
python -m http.server 8080

3. 浏览器访问
http://localhost:8080

## 声明
本项目仅供学习交流使用，王者荣耀素材版权归腾讯公司所有。

## 致谢
ECharts - 百度开源可视化库
D3.js - 数据驱动文档
王者荣耀官方 - 英雄数据与素材
课程老师