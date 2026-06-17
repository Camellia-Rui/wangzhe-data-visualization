import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import pdist, squareform
import json

# ============ 1. 读取你的Excel数据 ============
# 假设文件名为 "出场率和胜率.xlsx"，放在同目录下
df = pd.read_excel('出场率和胜率.xlsx', sheet_name='Sheet1')

# 查看数据结构
print(f"共读取 {len(df)} 个英雄")
print(df.head())

# ============ 2. 数据标准化 ============
scaler = MinMaxScaler()
# 用胜率、登场率、KDA三个维度
features = df[['胜率', '登场率', 'KDA']].values
features_norm = scaler.fit_transform(features)

# ============ 3. 计算相似度矩阵 ============
# 欧氏距离（距离越小越相似）
dist_matrix = squareform(pdist(features_norm, metric='euclidean'))
# 转换为相似度
similarity_matrix = 1 - dist_matrix

# ============ 4. 设置相似度阈值 ============
# 可以根据需要调整（0.85-0.95之间，值越大边越少）
threshold = 0.93

# ============ 5. 构建节点数据 ============
nodes = []
for i, row in df.iterrows():
    nodes.append({
        "name": row['英雄'],
        "winRate": float(row['胜率']),
        "pickRate": float(row['登场率']),
        "kda": float(row['KDA']),
        "category": 0  # 可后续根据聚类分配
    })

# ============ 6. 构建边数据 ============
links = []
hero_names = df['英雄'].tolist()
for i in range(len(df)):
    for j in range(i+1, len(df)):
        sim = similarity_matrix[i][j]
        if sim > threshold:
            links.append({
                "source": hero_names[i],
                "target": hero_names[j],
                "similarity": round(sim, 4)
            })

print(f"节点数: {len(nodes)}")
print(f"边数: {len(links)}")
print(f"平均每个英雄连接数: {len(links)*2/len(nodes):.1f}")

# ============ 7. 保存为JSON文件（供HTML使用） ============
with open('hero_similarity_data.json', 'w', encoding='utf-8') as f:
    json.dump({"nodes": nodes, "links": links}, f, ensure_ascii=False, indent=2)

print("数据已保存到 hero_similarity_data.json")

# ============ 8. 输出相似度TOP20的英雄对 ============
print("\n相似度最高的20对英雄:")
links_sorted = sorted(links, key=lambda x: x['similarity'], reverse=True)
for link in links_sorted[:20]:
    print(f"{link['source']} ↔ {link['target']}: {link['similarity']}")