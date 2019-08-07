import pickle

# f = open("usrs_info.pickle", "wb")
# pickle.dump({"admin": "admin"}, f) # 倒入“坛”中
# f.close()

with open("usrs_info.pickle", "rb") as f:
    print(pickle.load(f)) # “开坛”

