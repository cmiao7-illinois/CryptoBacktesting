import pandas as pd
import matplotlib.pyplot as plt

# 生成示例数据
data = {
    "Date": pd.date_range(start="2022-01-01", periods=100, freq="D"),
    "Price": [50 + i + 5 * (-1) ** i + 2 * (-1) ** (i // 7) for i in range(100)],
}
df = pd.DataFrame(data)
df.set_index("Date", inplace=True)

# 识别 Peaks 和 Troughs
df["Peak"] = df["Price"][
    (df["Price"].shift(1) < df["Price"]) & (df["Price"].shift(-1) < df["Price"])
]
df["Trough"] = df["Price"][
    (df["Price"].shift(1) > df["Price"]) & (df["Price"].shift(-1) > df["Price"])
]

# 支撑和阻力水平
support_levels = df["Trough"].dropna()
resistance_levels = df["Peak"].dropna()

# 画图
plt.figure(figsize=(10, 6))
plt.plot(df.index, df["Price"], label="Price")
plt.scatter(support_levels.index, support_levels.values, color="green", label="Support")
plt.scatter(
    resistance_levels.index, resistance_levels.values, color="red", label="Resistance"
)
plt.title("Support and Resistance Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
