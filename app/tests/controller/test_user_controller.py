async def test_pytest_test_client(test_cli):
    resp = await test_cli.get('/')
    assert resp.status == 200
    assert (await resp.json()) == {"hello": "world"}