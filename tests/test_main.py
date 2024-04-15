from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# 成功ケース

def test_fibonacci_valid():
    response = client.get("/fib?n=1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    response = client.get("/fib?n=99")
    assert response.status_code == 200
    assert response.json() == {"result": 218922995834555169026}

# nが存在しない場合のテスト

def test_fibonacci_no_query():
    response = client.get("/fib")
    assert response.status_code == 422
    assert response.json() == {"status": 422, "message": "need query parameter n"}

# nが正の整数でない場合のテスト

def test_fibonacci_non_int():
    response = client.get("/fib?n=string")
    assert response.status_code == 422
    assert response.json() == {"status": 422, "message": "n must be PositiveInt"}

def test_fibonacci_non_positive_int():
    response = client.get("/fib?n=-1")
    assert response.status_code == 400
    assert response.json() == {"status": 422, "message": "n must be PositiveInt"}

    response = client.get("/fib?n=0")
    assert response.status_code == 400
    assert response.json() == {"status": 422, "message": "n must be PositiveInt"}

# 計算結果が桁数制限を超えた場合のテスト

def test_fibonacci_overflow():
    response = client.get("/fib?n=30000")
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "The number has exceeded the maximum allowed digits"}

# リクエストされたパスが見つからない場合のテスト

# def test_invalid_requests():
#     response = client.get("/")
#     assert response.status_code == 404

#     response = client.get("/notfound")
#     assert response.status_code == 404


# # GET以外のメソッドでリクエストされた場合のテスト

# def test_method_not_allowed():
#     response = client.post("/fib")
#     assert response.status_code == 405

#     response = client.put("/fib")
#     assert response.status_code == 405

#     response = client.delete("/fib")
#     assert response.status_code == 405

#     response = client.patch("/fib")
#     assert response.status_code == 405

#     response = client.head("/fib")
#     assert response.status_code == 405

#     response = client.options("/fib")
#     assert response.status_code == 405