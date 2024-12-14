# Remote_Procedure_Call
簡易的なRPCの実装です。
サーバー・クライアント間をjson形式でやりとりします。
現在対応している関数は、floorと文字列のsortです。
・floor
  10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
・sort
  文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。

入力例）{"method":"floor", "params":27.883, "param_type":"float", "id":1}
出力例）{'results': '27', 'result_type': "<class 'int'>", 'id': 1}

入力例）{"method":"sort", "params":"nbnejgjkna", "param_type":"str", "id":2}
出力例）{'results': 'abegjjknnn', 'result_type': "<class 'str'>", 'id': 2}

入力例）exit
出力例）プログラムの終了
