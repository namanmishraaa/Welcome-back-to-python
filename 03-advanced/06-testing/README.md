# 06-testing — pytest and Test-Driven Development

Write reliable, maintainable tests. Testing is a non-negotiable skill for professional developers.

**Official Docs:** https://docs.python.org/3/library/unittest.html
**pytest Docs:** https://docs.pytest.org/

## 📚 Topics Covered
- Why test? — confidence, regression prevention, design feedback
- `pytest` basics — test discovery, assertions
- `pytest.raises` — testing exceptions
- `pytest.approx` — floating-point comparisons
- **Fixtures** — `@pytest.fixture`, `scope` (function/class/module/session)
- **Parametrize** — `@pytest.mark.parametrize`
- **Marks** — `skip`, `skipif`, `xfail`, custom marks
- **Mocking** — `unittest.mock.patch`, `MagicMock`, `call`
- `tmp_path` fixture — file I/O testing
- `capfd` / `capsys` — capturing stdout/stderr
- `monkeypatch` — patching environment variables, functions
- `unittest.TestCase` — classic style
- Coverage — `pytest-cov`
- TDD workflow — Red → Green → Refactor

## 💡 Learning Objectives
- ✅ Write tests for every function you create
- ✅ Use fixtures to keep tests DRY
- ✅ Mock external dependencies (HTTP, DB, time)
- ✅ Achieve 80%+ coverage on your code
- ✅ Understand and practice TDD

## 🎯 Interview Tips
- The difference between a mock, stub, spy, and fake
- Why `pytest.approx` instead of `==` for floats
- `scope="module"` vs `scope="function"` fixtures — when to use each
- Parametrize reduces duplication; each set of params is an independent test

## 🛠️ Setup
```bash
uv add --dev pytest pytest-cov
pytest -v
pytest --cov=. --cov-report=html
```

## 📝 Files
1. **test_examples.py** — full pytest guide with fixtures, parametrize, mocking

---
**Difficulty: ⭐⭐⭐ Non-negotiable for professional code**
