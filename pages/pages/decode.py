import urllib.parse
import os

def decode_filenames(directory):
    # ディレクトリ内のすべてのファイル名とサブディレクトリを取得
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        
        # ファイル名またはディレクトリ名をデコードする
        decoded_name = urllib.parse.unquote(filename)
        new_full_path = os.path.join(directory, decoded_name)
        
        # 元の名前とデコード後の名前が異なる場合にのみリネームする
        if full_path != new_full_path:
            os.rename(full_path, new_full_path)
            full_path = new_full_path  # リネーム後の新しいパスに更新
        
        # ディレクトリの場合、再帰的に処理を行う
        if os.path.isdir(full_path):
            decode_filenames(full_path)

# 現在のディレクトリを取得
current_dir = '.'

# 関数を呼び出してデコードを実行する
decode_filenames(current_dir)
