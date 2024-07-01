import urllib.parse
import os
import shutil

def decode_filenames(directory):
    # ディレクトリ内のすべてのファイル名とサブディレクトリを取得
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        
        # ファイル名またはディレクトリ名をデコードする
        decoded_name = urllib.parse.unquote(filename)
        new_full_path = os.path.join(directory, decoded_name)
        
        # 元の名前とデコード後の名前が異なる場合にのみリネームする
        if full_path != new_full_path:
            if os.path.exists(new_full_path):
                if os.path.isdir(new_full_path):
                    # ディレクトリが既に存在する場合、その中にファイルを移動
                    for sub_filename in os.listdir(full_path):
                        shutil.move(os.path.join(full_path, sub_filename), os.path.join(new_full_path, sub_filename))
                    # 移動が終わったら空のディレクトリを削除
                    os.rmdir(full_path)
                else:
                    # 既存のファイルがある場合、エラーをスロー
                    raise OSError(f"File exists: {new_full_path}")
            else:
                os.rename(full_path, new_full_path)
                full_path = new_full_path  # リネーム後の新しいパスに更新
        
        # ディレクトリの場合、再帰的に処理を行う
        if os.path.isdir(full_path):
            decode_filenames(full_path)

# 現在のディレクトリを取得
current_dir = '.'

# 関数を呼び出してデコードを実行する
decode_filenames(current_dir)

