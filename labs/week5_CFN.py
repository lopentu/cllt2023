import json

# If your data is stored in a file, load it like this:
with open("week5_CFN_LEX_ZHTW.json", "r", encoding="utf-8") as f:
    chinese_framenet = json.load(f)

# If you have the data directly in your script, load it like this:
chinese_framenet = {
  "Visiting": ['客人', '來訪者', '遊客', '視察', '到訪', '賓館', '招待所', '賓客', '審視', '訪問者', '住客', '做客', '顧客', '外國遊客', '迴訪', '招待', '主人', '貴賓', '旅遊', '探訪', '訪客', '來訪', '作客', '迴顧', '來客', '參觀', '客房', '旅客', '應邀', '邀請', '嘉賓', '外賓', '來賓']
  # Add more frames and lexical units here
}


import json
import jieba

# Load the Chinese FrameNet data
chinese_framenet = {
  "Visiting": ['客人', '來訪者', '遊客', '視察', '到訪', '賓館', '招待所', '賓客', '審視', '訪問者', '住客', '做客', '顧客', '外國遊客', '迴訪', '招待', '主人', '貴賓', '旅遊', '探訪', '訪客', '來訪', '作客', '迴顧', '來客', '參觀', '客房', '旅客', '應邀', '邀請', '嘉賓', '外賓', '來賓']
  # Add more frames and lexical units here
}

# Tokenize a sentence
sentence = "今天我去拜訪了我的朋友"
tokens = list(jieba.cut(sentence))

# Print the tokenized sentence
print("Tokenized sentence:", tokens)

# Frame identification
found_frames = set()

for token in tokens:
    for frame, lexical_units in chinese_framenet.items():
        if token in lexical_units:
            found_frames.add(frame)

print("Identified frames:", found_frames)
