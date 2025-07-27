import os
import re

def rename_episodes(folder_path):
    # a와 b가 알파벳+숫자로 이루어진 1~5자리 문자열일 때 매칭
    pattern = re.compile(r"episode_([a-zA-Z0-9]{1,5})_([a-zA-Z0-9]{1,5})\.hdf5")

    files = []
    for fname in os.listdir(folder_path):
        match = pattern.fullmatch(fname)
        if match:
            a = match.group(1)
            b = match.group(2)
            files.append((b, a, fname))  # b → a 기준 정렬

    files.sort()  # 튜플 순으로 정렬 (b → a)

    print(files)
    import pdb; pdb.set_trace()

    for index, (_, _, fname) in enumerate(files):
        old_path = os.path.join(folder_path, fname)
        # 0~49: original episodes (cp -r), 50~1049: augmented episodes (indexing_data.py)
        new_name = f"episode_{index + 50}.hdf5"
        new_path = os.path.join(folder_path, new_name)
        print(f"Renaming {fname} → {new_name}")
        os.rename(old_path, new_path)

# 사용 예:
rename_episodes("../data/bag_augmented/aligned_episodes/")
rename_episodes("../data/towel_augmented/aligned_episodes/")