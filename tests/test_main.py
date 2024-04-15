from fastapi.testclient import TestClient

from app.main import app

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

# nが正の整数でない場合のテスト

def test_fibonacci_non_int():
    response = client.get("/fib?n=string")
    assert response.status_code == 422

def test_fibonacci_non_positive_int():
    response = client.get("/fib?n=-1")
    assert response.status_code == 400

    response = client.get("/fib?n=0")
    assert response.status_code == 400

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