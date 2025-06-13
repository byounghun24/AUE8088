import random
import os

input_txt_path = 'datasets/kaist-rgbt/train-all-04.txt'
output_dir = 'datasets/kaist-rgbt'
num_folds = 5

with open(input_txt_path, 'r') as f:
    all_lines = f.readlines()

random.seed(42)
random.shuffle(all_lines)

total_len = len(all_lines)
fold_size = total_len // num_folds
folds = [all_lines[i*fold_size : (i+1)*fold_size] for i in range(num_folds - 1)]
folds.append(all_lines[(num_folds - 1) * fold_size:])

for i in range(num_folds):
    val_lines = folds[i]
    train_lines = [line for j, fold in enumerate(folds) if j != i for line in fold]

    val_lines_sorted = sorted(val_lines)
    train_lines_sorted = sorted(train_lines)

    train_txt_path = os.path.join(output_dir, f'train_split_{i}.txt')
    val_txt_path   = os.path.join(output_dir, f'val_split_{i}.txt')

    with open(train_txt_path, 'w') as f:
        f.writelines(train_lines_sorted)

    with open(val_txt_path, 'w') as f:
        f.writelines(val_lines_sorted)

    print(f"[Fold {i}]")
    print(f"  train 이미지 수: {len(train_lines_sorted)}")
    print(f"  val 이미지 수: {len(val_lines_sorted)}")
