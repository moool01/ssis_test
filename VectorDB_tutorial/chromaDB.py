import chromadb

client = chromadb.PersistentClient() # 데이터를 파일에 저장

# posts = client.create_collection(
#     name="posts"
# )

posts = client.get_collection("posts")

# post1 = '국민기초생활보장법에 따른 국민기초생활보장제도는 저소득층 수급권자에 대해 최저생활을 보장하고 자립을 유도하는 제도' # 맞춤형 기초생활보장제도
# post2 = '생계유지가 곤란한 저소득층으로 사전안내된 위기사유와 소득, 재산기준을 충족하는 가구에 대해 지원해주는 제도' # 긴급복지 지원제도
# post3 = '안정적 주거생활이 필요한 분들에 한해 보다 저렴하게 주택을 공급받을 수 있도록 지원하는 제도' # 주택임대 제도
# post4 = '주택수리, 노후시설교체 등 주거생활 개선이 필요한분들이 보다 쾌적한 주거환경에서 생활할 수 있도록 지원하는 제도' # 주거환경개선지원

# posts.add(
# 	documents=[post1, post2, post3, post4],
# 	ids=["1", "2", "3", "4"]
# )

result = posts.query(
	query_texts=['생계지원'],
	n_results=3
)

print(result)

result2 = posts.query(
	query_texts=['주택공급'],
	n_results=3
)

print(result2)

result3 = posts.query(
	query_texts=['배가 너무 고프고, 춥고, 졸리고, 돈도 벌고 싶어요... 그러려면 안락한 보금자리가 필요할 거 같아요...'],
	n_results=3
)

print(result3)